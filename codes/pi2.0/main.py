import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QObject, Signal, Slot, QTimer, QThread

from main_window_ui import Ui_MainWindow
from dispenser import Dispenser
from rfid_reader import RFIDReader
from prescription_database import PrescriptionDatabase

class DispenserController(QObject):
    """分药机控制器，运行在单独的线程中"""
    rfid_detected = Signal(str)  # 信号：检测到RFID
    error_occurred = Signal(str)  # 信号：发生错误
    prescription_loaded = Signal(dict)  # 处方加载成功信号
    dispensing_started = Signal()  # 分药流程开始信号
    dispensing_progress = Signal(str, int, int)  # 分药进度信号 (药品名称, 当前索引, 总数)
    dispensing_completed = Signal()  # 分药流程完成信号

    def __init__(self, dispenser_port="COM6", rfid_port="COM9"):
        super().__init__()
        self.dispenser_port = dispenser_port
        self.rfid_port = rfid_port
        
        # 初始化组件
        self.dispenser = None
        self.rfid_reader = None
        self.database = PrescriptionDatabase("demo_prescriptions.csv")

        # 初始化当前状态
        self.current_rfid = None
        self.current_prescription = None
        self.current_medicines = []  # 添加这个
        self.current_pill_matrices = {}
        self.current_medicine_index = 0  # 添加这个
        self.is_dispensing = False  # 添加这个状态标志
        
        # 添加监控定时器
        self.monitor_timer = QTimer()
        self.monitor_timer.timeout.connect(self.monitor_dispensing_status)

    def initialize_hardware(self):
        """初始化硬件设备"""
        try:
            # 初始化分药机
            print("[初始化] 连接分药机...")
            self.dispenser = Dispenser(self.dispenser_port)
            if self.dispenser.ser is None:
                raise Exception("分药机连接失败")
            
            # 启动分药机反馈处理
            self.dispenser.start_dispenser_feedback_handler()
            
            # 初始化分药机
            init_result = self.dispenser.init()
            if init_result != 0:
                raise Exception(f"分药机初始化失败，错误码: {init_result}")
            
            # 初始化RFID读卡器
            print("[初始化] 连接RFID读卡器...")
            self.rfid_reader = RFIDReader(self.rfid_port)
            if not self.rfid_reader.connect():
                raise Exception("RFID读卡器连接失败")
            
            print("[成功] 硬件初始化完成")
            return True
            
        except Exception as e:
            print(f"[错误] 硬件初始化失败: {str(e)}")
            self.error_occurred.emit(f"硬件初始化失败: {str(e)}")
            return False
        
    def cleanup_hardware(self):
        """清理硬件资源"""
        try:
            if self.monitor_timer.isActive():
                self.monitor_timer.stop()
                
            if self.dispenser:
                self.dispenser.stop_dispenser_feedback_handler()
                self.dispenser.close_plate()  # 确保药盘关闭
            
            if self.rfid_reader:
                self.rfid_reader.disconnect()
                
            print("[清理] 硬件资源已释放")
        except Exception as e:
            print(f"[错误] 清理硬件资源时发生错误: {e}")

    def prepare_for_rfid_detection(self):
        """为RFID检测做准备"""
        try:
            if not self.dispenser:
                self.error_occurred.emit("分药机未初始化")
                return False
            
            print("[分药机] 正在打开药盘...")
            open_result = self.dispenser.open_plate()
            
            if open_result != 0:
                self.error_occurred.emit(f"打开药盘失败，错误码: {open_result}")
                return False
            
            print("[分药机] 药盘打开成功，准备检测RFID")
            return True

        except Exception as e:
            self.error_occurred.emit(f"准备RFID检测失败: {str(e)}")
            return False   
        
    def start_rfid_detection(self):
        """开始RFID检测"""
        try:            
            if not self.rfid_reader:
                self.error_occurred.emit("RFID读卡器未初始化")
                return
            
            print("[RFID] 开始检测RFID...")
            # 读取RFID
            result = self.rfid_reader.read_single(timeout=20.0)
            
            if result["error_code"] == 0 and result["epc"]:
                epc = result["epc"]
                print(f"[RFID] 检测到卡片: {epc}")
                
                # 将EPC转换为RFID（这里可能需要根据实际情况调整）
                rfid = epc  # 或者进行某种转换
                
                self.current_rfid = rfid
                self.rfid_detected.emit(rfid)
                
                # 自动加载药品矩阵
                self.load_pill_matrices(rfid)
                
            else:
                error_msg = result.get('error', '未知错误')
                print(f"[RFID] 读取失败: {error_msg}")
                self.error_occurred.emit(f"RFID读取失败: {error_msg}")
                
        except Exception as e:
            print(f"[错误] RFID检测异常: {str(e)}")
            self.error_occurred.emit(f"RFID检测异常: {str(e)}")

    def load_pill_matrices(self, rfid):
        """加载处方信息并生成分药矩阵"""
        try:
            # 从数据库获取处方信息和分药矩阵
            success, pill_matrices, error = self.database.generate_pill_matrices(rfid)
            
            if not success:
                self.error_occurred.emit(f"生成分药矩阵失败: {error}")
                return
            
            # 获取处方基本信息
            prescription_data = self.database.get_patient_prescription(rfid)
            
            if not prescription_data['success']:
                self.error_occurred.emit(f"未找到处方信息: {prescription_data['error']}")
                return
            
            # 保存处方信息和分药矩阵
            self.current_prescription = prescription_data
            self.current_medicines = prescription_data['medicines']
            self.current_pill_matrices = pill_matrices  # 新增：保存分药矩阵字典
            self.current_medicine_index = 0
            
            print(f"[处方] 加载成功: {prescription_data['patient_info']['patient_name']}")
            print(f"[处方] 药品数量: {len(self.current_medicines)}")
            print(f"[矩阵] 生成 {len(pill_matrices)} 个分药矩阵:")
            # 打印每种药品的矩阵信息
            for medicine_name, matrix in pill_matrices.items():
                total_pills = matrix.sum()
                print(f"  - {medicine_name}: 总药片数 {total_pills}")
            
            # 发送信号，包含处方信息和分药矩阵
            enhanced_prescription_data = prescription_data.copy()
            enhanced_prescription_data['pill_matrices'] = pill_matrices
            
            self.prescription_loaded.emit(enhanced_prescription_data)
        
        except Exception as e:
            print(f"[错误] 加载分药矩阵异常: {str(e)}")
            self.error_occurred.emit(f"加载分药矩阵异常: {str(e)}")

    def start_dispensing(self):
        """开始分药流程"""
        try:
            if not self.current_medicines:
                print("[错误] 没有药品需要分发")
                self.error_occurred.emit("没有药品需要分发")
                return
            
            if not self.dispenser:
                print("[错误] 分药机未初始化")
                self.error_occurred.emit("分药机未初始化")
                return
            
            self.is_dispensing = True
            self.current_medicine_index = 0
            
            print("[分药] 开始分药流程")
            self.dispensing_started.emit()
            
            # 开始分发第一种药品
            self.dispense_next_medicine()
            
        except Exception as e:
            print(f"[错误] 启动分药异常: {str(e)}")
            self.error_occurred.emit(f"启动分药异常: {str(e)}")

    def dispense_next_medicine(self):
        """分发下一种药品"""
        try:
            if self.current_medicine_index >= len(self.current_medicines):
                # 所有药品分发完成
                print("[分药] 所有药品已分发完成")
                self.complete_dispensing()
                return
            
            current_medicine = self.current_medicines[self.current_medicine_index]
            medicine_name = current_medicine['medicine_name']
            
            print(f"[分药] 开始分发第 {self.current_medicine_index + 1}/{len(self.current_medicines)} 种药品: {medicine_name}")
            
            # 直接从已生成的矩阵字典中获取该药品的矩阵
            if medicine_name not in self.current_pill_matrices:
                error_msg = f"未找到药品矩阵: {medicine_name}"
                print(f"[错误] {error_msg}")
                self.error_occurred.emit(error_msg)
                return
            
            pill_matrix = self.current_pill_matrices[medicine_name]

            # 打印当前分药矩阵信息
            print(f"[分药] {medicine_name} 分药矩阵:")
            time_labels = ["早上", "中午", "晚上", "夜间"]
            for i, label in enumerate(time_labels):
                print(f"  {label}: {' '.join(f'{x:2}' for x in pill_matrix[i])}")
            
            # 发送分药数据到分药机
            print(f"[分药] 发送分药数据到分药机...")
            ack = self.dispenser.send_data(pill_matrix)
            
            if not ack:
                error_msg = f"发送分药数据失败: {medicine_name}"
                print(f"[错误] {error_msg}")
                self.error_occurred.emit(error_msg)
                return
            
            print(f"[分药] 数据发送成功，等待分药完成...")
            
            # 发送进度信号
            self.dispensing_progress.emit(
                medicine_name, 
                self.current_medicine_index + 1, 
                len(self.current_medicines)
            )
            
            # 启动监控定时器
            self.monitor_timer.start(1000)  # 每秒检查一次

        except Exception as e:
            error_msg = f"分药异常: {str(e)}"
            print(f"[错误] {error_msg}")
            self.error_occurred.emit(error_msg)

    def monitor_dispensing_status(self):
        """监控分药状态"""
        try:
            if not self.dispenser or not self.is_dispensing:
                self.monitor_timer.stop()
                return
            
            # 检查分药机状态
            print(f"[监控] 分药机状态: {self.dispenser.state}, 错误码: {self.dispenser.err_code}")
            
            if self.dispenser.state == 3:  # 分药完成
                self.monitor_timer.stop()
                
                current_medicine = self.current_medicines[self.current_medicine_index]
                medicine_name = current_medicine['medicine_name']
                
                if self.dispenser.err_code == 0:
                    print(f"[分药] {medicine_name} 分发完成")
                    if hasattr(self.dispenser, 'pill_remain'):
                        print(f"[分药] 剩余药片: {self.dispenser.pill_remain}")
                    
                    # 准备分发下一种药品
                    self.current_medicine_index += 1
                    
                    # 等待一小段时间再分发下一种药品
                    QTimer.singleShot(2000, self.dispense_next_medicine)
                    
                else:
                    error_msg = f"{medicine_name} 分药错误，错误码: {self.dispenser.err_code}"
                    print(f"[错误] {error_msg}")
                    self.error_occurred.emit(error_msg)
                    
            elif self.dispenser.state == 2:  # 暂停状态
                print("[分药] 分药已暂停")
                
            elif self.dispenser.state == 1:  # 分药中
                print("[分药] 正在分药...")
                
        except Exception as e:
            error_msg = f"监控分药状态异常: {str(e)}"
            print(f"[错误] {error_msg}")
            self.error_occurred.emit(error_msg)

    def complete_dispensing(self):
        """完成分药流程"""
        try:
            self.is_dispensing = False
            self.monitor_timer.stop()
            
            # 关闭药盘
            print("[分药] 关闭药盘...")
            if self.dispenser.close_plate() != 0:
                print("[警告] 关闭药盘失败")
            
            print("[分药] 所有药品分发完成")
            self.dispensing_completed.emit()
            
        except Exception as e:
            error_msg = f"完成分药异常: {str(e)}"
            print(f"[错误] {error_msg}")
            self.error_occurred.emit(error_msg)

    def pause_dispensing(self):
        """暂停分药"""
        try:
            if self.dispenser and self.is_dispensing:
                result = self.dispenser.pause()
                if result == 0:
                    print("[分药] 分药已暂停")
                else:
                    self.error_occurred.emit("暂停分药失败")
        except Exception as e:
            self.error_occurred.emit(f"暂停分药异常: {str(e)}")

    def stop_dispensing(self):
        """停止分药"""
        try:
            self.is_dispensing = False
            self.monitor_timer.stop()
            
            if self.dispenser:
                self.dispenser.pause()
                
            print("[分药] 分药已停止")
            
        except Exception as e:
            self.error_occurred.emit(f"停止分药异常: {str(e)}")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.rignt_stackedWidget.setCurrentIndex(0)  # Set the initial page
        self.ui.RFID_msg.hide()  # Hide the RFID message initially
        self.ui.prescription_msg.hide()  # Hide the prescription message initially


if __name__ == "__main__":
    # 测试控制器
    app = QApplication(sys.argv)
    
    print("=== 分药机控制器测试 ===")
    controller = DispenserController()
    
    # 连接错误信号
    controller.error_occurred.connect(lambda msg: print(f"[UI错误] {msg}"))
    controller.prescription_loaded.connect(lambda data: print(f"[UI] 处方加载完成"))
    controller.dispensing_started.connect(lambda: print(f"[UI] 分药开始"))
    controller.dispensing_progress.connect(lambda name, cur, total: print(f"[UI] 分药进度: {name} ({cur}/{total})"))
    controller.dispensing_completed.connect(lambda: print(f"[UI] 分药完成"))
    
    if controller.initialize_hardware():
        print("硬件初始化成功，开始测试流程...")
        
        # 手动测试流程
        if controller.prepare_for_rfid_detection():
            print("药盘打开成功，开始RFID检测...")
            controller.start_rfid_detection()
            
            # 如果检测成功，会自动加载处方和分药矩阵
            # 然后可以开始分药
            if controller.current_medicines:
                print("开始分药...")
                controller.start_dispensing()
            else:
                print("没有找到药品，无法分药")
        else:
            print("药盘打开失败")
    else:
        print("硬件初始化失败")
    
    # 清理资源
    def cleanup():
        controller.cleanup_hardware()
        app.quit()
    
    # 设置5分钟后自动退出（防止程序挂死）
    QTimer.singleShot(300000, cleanup)
    
    sys.exit(app.exec())