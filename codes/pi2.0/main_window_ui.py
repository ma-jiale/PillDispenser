# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(920, 540)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_widget = QWidget(self.centralwidget)
        self.left_widget.setObjectName(u"left_widget")
        self.left_widget.setMinimumSize(QSize(215, 0))
        self.left_widget.setMaximumSize(QSize(215, 16777215))
        self.left_widget.setStyleSheet(u"#left_widget {\n"
"background: rgb(239, 244, 249);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.left_widget)
        self.verticalLayout.setSpacing(14)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 28)
        self.init_widget = QWidget(self.left_widget)
        self.init_widget.setObjectName(u"init_widget")
        self.init_widget.setMinimumSize(QSize(0, 75))
        self.init_widget.setMaximumSize(QSize(16777215, 75))
        self.init_widget.setStyleSheet(u"#init_widget\n"
"{\n"
"border-radius: 5px;\n"
"background: #2B68F6;\n"
"}")
        self.label = QLabel(self.init_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 61, 16))
        self.label.setStyleSheet(u"QLabel\n"
"{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_2 = QLabel(self.init_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 61, 16))
        self.label_2.setStyleSheet(u"QLabel\n"
"{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame = QFrame(self.init_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 40, 180, 2))
        self.frame.setStyleSheet(u"QFrame\n"
"{\n"
"background: #D9D9D9;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.comboBox = QComboBox(self.init_widget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 10, 68, 22))
        self.comboBox_2 = QComboBox(self.init_widget)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(100, 50, 68, 22))

        self.verticalLayout.addWidget(self.init_widget)

        self.process_widget = QWidget(self.left_widget)
        self.process_widget.setObjectName(u"process_widget")
        self.process_widget.setMaximumSize(QSize(16777215, 500))
        self.process_widget.setStyleSheet(u"#process_widget\n"
"{\n"
"border-radius: 5px;\n"
"border: 1px solid #DCDCDC;\n"
"background: #FFF;\n"
"}")
        self.gridLayout = QGridLayout(self.process_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.taskwidget = QWidget(self.process_widget)
        self.taskwidget.setObjectName(u"taskwidget")
        self.verticalLayout_3 = QVBoxLayout(self.taskwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.taskwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_8 = QLabel(self.taskwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.label_8)

        self.label_9 = QLabel(self.taskwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.label_9)

        self.label_10 = QLabel(self.taskwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_3.addWidget(self.label_10)

        self.label_11 = QLabel(self.taskwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 30))
        self.label_11.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.label_11)

        self.label_12 = QLabel(self.taskwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 30))
        self.label_12.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.label_12)

        self.label_13 = QLabel(self.taskwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 30))
        self.label_13.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.label_13)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.taskwidget, 1, 1, 1, 1)

        self.title_widget = QWidget(self.process_widget)
        self.title_widget.setObjectName(u"title_widget")
        self.title_widget.setMinimumSize(QSize(0, 30))
        self.title_widget.setMaximumSize(QSize(16777215, 30))
        self.title_widget.setStyleSheet(u"QWidget\n"
"{\n"
" Border: None\n"
"}")
        self.title = QLabel(self.title_widget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 6, 81, 20))

        self.gridLayout.addWidget(self.title_widget, 0, 0, 1, 2)

        self.progressBar_widget = QWidget(self.process_widget)
        self.progressBar_widget.setObjectName(u"progressBar_widget")
        self.progressBar_widget.setMaximumSize(QSize(30, 16777215))
        self.task_progressBar = QProgressBar(self.progressBar_widget)
        self.task_progressBar.setObjectName(u"task_progressBar")
        self.task_progressBar.setGeometry(QRect(7, 16, 10, 190))
        self.task_progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #C0C0C0;\n"
"    border-radius: 5px;\n"
"    background-color: #F0F0F0;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #4CAF50;\n"
"    border-radius: 3px;\n"
"}")
        self.task_progressBar.setMaximum(7)
        self.task_progressBar.setValue(0)
        self.task_progressBar.setTextVisible(False)
        self.task_progressBar.setOrientation(Qt.Vertical)
        self.task_progressBar.setInvertedAppearance(True)
        self.task_progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout.addWidget(self.progressBar_widget, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.process_widget)


        self.horizontalLayout.addWidget(self.left_widget)

        self.rignt_stackedWidget = QStackedWidget(self.centralwidget)
        self.rignt_stackedWidget.setObjectName(u"rignt_stackedWidget")
        self.rignt_stackedWidget.setMaximumSize(QSize(16677215, 16777215))
        self.rignt_stackedWidget.setStyleSheet(u"QFrame {\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-top: 0.5px solid #DCDCDC;\n"
"    border-left: 0.5px solid #DCDCDC;\n"
"    background-color: #FFF;\n"
"}")
        self.put_pan_in_page = QWidget()
        self.put_pan_in_page.setObjectName(u"put_pan_in_page")
        self.put_pan_in = QLabel(self.put_pan_in_page)
        self.put_pan_in.setObjectName(u"put_pan_in")
        self.put_pan_in.setEnabled(True)
        self.put_pan_in.setGeometry(QRect(160, 110, 421, 131))
        self.put_pan_in.setStyleSheet(u"QLabel\n"
"{\n"
"color: #2B68F6;\n"
"font-size: 64px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;\n"
"}")
        self.put_pan_in.setFrameShape(QFrame.NoFrame)
        self.put_pan_in.setLineWidth(1)
        self.put_pan_in.setTextFormat(Qt.AutoText)
        self.put_pan_in.setAlignment(Qt.AlignCenter)
        self.RFID_msg = QLabel(self.put_pan_in_page)
        self.RFID_msg.setObjectName(u"RFID_msg")
        self.RFID_msg.setGeometry(QRect(300, 250, 121, 16))
        self.prescription_msg = QLabel(self.put_pan_in_page)
        self.prescription_msg.setObjectName(u"prescription_msg")
        self.prescription_msg.setGeometry(QRect(300, 280, 121, 16))
        self.begin_dispense_ = QPushButton(self.put_pan_in_page)
        self.begin_dispense_.setObjectName(u"begin_dispense_")
        self.begin_dispense_.setGeometry(QRect(240, 320, 241, 51))
        self.begin_dispense_.setLayoutDirection(Qt.LeftToRight)
        self.begin_dispense_.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;\n"
"    background-color: #2B68F6;\n"
"    border: none;\n"
"    color: #FFF;\n"
"    font-size: 26px;\n"
"    font-weight: 400;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E4FD6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1A3FB8;\n"
"}")
        self.rignt_stackedWidget.addWidget(self.put_pan_in_page)
        self.dispense_page = QWidget()
        self.dispense_page.setObjectName(u"dispense_page")
        self.gridLayout_2 = QGridLayout(self.dispense_page)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.drug_info_widget = QWidget(self.dispense_page)
        self.drug_info_widget.setObjectName(u"drug_info_widget")
        self.drug_info_widget.setMinimumSize(QSize(400, 0))
        self.drug_info_widget.setMaximumSize(QSize(1677215, 16777215))
        self.drug_info_widget.setStyleSheet(u"QWidget\n"
"{\n"
"border: none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.drug_card = QWidget(self.drug_info_widget)
        self.drug_card.setObjectName(u"drug_card")
        self.drug_card.setGeometry(QRect(40, 40, 306, 276))
        self.drug_card.setStyleSheet(u"QWidget\n"
"{\n"
"border-radius: 15px;\n"
"background-color: rgb(239, 244, 249);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.drug_card)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.current_drug_img = QLabel(self.drug_card)
        self.current_drug_img.setObjectName(u"current_drug_img")
        self.current_drug_img.setPixmap(QPixmap(u"../../../../Downloads/drug_test.jpg"))
        self.current_drug_img.setScaledContents(False)
        self.current_drug_img.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.current_drug_img)

        self.current_drug = QLabel(self.drug_card)
        self.current_drug.setObjectName(u"current_drug")
        self.current_drug.setStyleSheet(u"QLabel\n"
"{\n"
"color: #2E344F;\n"
"font-size: 28px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}")
        self.current_drug.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.current_drug)


        self.gridLayout_2.addWidget(self.drug_info_widget, 1, 0, 1, 2)

        self.patient_info_widget = QWidget(self.dispense_page)
        self.patient_info_widget.setObjectName(u"patient_info_widget")
        self.patient_info_widget.setMaximumSize(QSize(16777215, 40))
        self.patient_info_widget.setStyleSheet(u"QWidget\n"
"{\n"
"	border: none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.patient_name = QLabel(self.patient_info_widget)
        self.patient_name.setObjectName(u"patient_name")
        self.patient_name.setGeometry(QRect(30, 10, 54, 16))
        self.prescription_data = QLabel(self.patient_info_widget)
        self.prescription_data.setObjectName(u"prescription_data")
        self.prescription_data.setGeometry(QRect(90, 10, 241, 16))

        self.gridLayout_2.addWidget(self.patient_info_widget, 0, 0, 1, 3)

        self.drugs_lists_widget = QWidget(self.dispense_page)
        self.drugs_lists_widget.setObjectName(u"drugs_lists_widget")
        self.drugs_lists_widget.setMaximumSize(QSize(16777215, 120))
        self.drugs_lists_widget.setStyleSheet(u"QWidget\n"
"{\n"
"border: none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")

        self.gridLayout_2.addWidget(self.drugs_lists_widget, 2, 0, 1, 3)

        self.operate_widget = QWidget(self.dispense_page)
        self.operate_widget.setObjectName(u"operate_widget")
        self.operate_widget.setMinimumSize(QSize(300, 0))
        self.operate_widget.setStyleSheet(u"QWidget\n"
"{\n"
"border: none;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.guide_msg = QLabel(self.operate_widget)
        self.guide_msg.setObjectName(u"guide_msg")
        self.guide_msg.setGeometry(QRect(10, 70, 141, 41))
        self.guide_msg.setStyleSheet(u"QLabel\n"
"{\n"
"color: #000;\n"
"font-size: 30px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}")
        self.cam_detection_info = QLabel(self.operate_widget)
        self.cam_detection_info.setObjectName(u"cam_detection_info")
        self.cam_detection_info.setGeometry(QRect(10, 120, 181, 41))
        self.cam_detection_info.setStyleSheet(u"QLabel\n"
"{\n"
"color: #000;\n"
"font-size: 30px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}")
        self.tip_to_put_drug_in = QLabel(self.operate_widget)
        self.tip_to_put_drug_in.setObjectName(u"tip_to_put_drug_in")
        self.tip_to_put_drug_in.setGeometry(QRect(0, 220, 271, 71))
        self.tip_to_put_drug_in.setStyleSheet(u"QLabel\n"
"{\n"
"color: #000;\n"
"font-size: 30px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}")
        self.dispense_progressBar = QProgressBar(self.operate_widget)
        self.dispense_progressBar.setObjectName(u"dispense_progressBar")
        self.dispense_progressBar.setGeometry(QRect(10, 170, 191, 34))
        self.dispense_progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #C0C0C0;\n"
"    border-radius: 16px;\n"
"    background-color: #F0F0F0;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #4CAF50;\n"
"    border-radius: 14px;\n"
"}")
        self.dispense_progressBar.setValue(24)
        self.dispense_progressBar.setTextVisible(False)
        self.progressBar_percentage = QLabel(self.operate_widget)
        self.progressBar_percentage.setObjectName(u"progressBar_percentage")
        self.progressBar_percentage.setGeometry(QRect(210, 166, 61, 41))
        self.progressBar_percentage.setStyleSheet(u"QLabel\n"
"{\n"
"color: #000;\n"
"font-size: 30px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"}")

        self.gridLayout_2.addWidget(self.operate_widget, 1, 2, 1, 1)

        self.rignt_stackedWidget.addWidget(self.dispense_page)
        self.finish_dispense_page = QWidget()
        self.finish_dispense_page.setObjectName(u"finish_dispense_page")
        self.finish_all = QLabel(self.finish_dispense_page)
        self.finish_all.setObjectName(u"finish_all")
        self.finish_all.setEnabled(True)
        self.finish_all.setGeometry(QRect(80, 120, 541, 131))
        self.finish_all.setStyleSheet(u"QLabel\n"
"{\n"
"color: #2B68F6;\n"
"font-size: 64px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"border: none;\n"
"}")
        self.finish_all.setFrameShape(QFrame.NoFrame)
        self.finish_all.setLineWidth(1)
        self.finish_all.setTextFormat(Qt.AutoText)
        self.finish_all.setAlignment(Qt.AlignCenter)
        self.exit = QPushButton(self.finish_dispense_page)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(220, 320, 241, 51))
        self.exit.setLayoutDirection(Qt.LeftToRight)
        self.exit.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;\n"
"    background-color: #2B68F6;\n"
"    border: none;\n"
"    color: #FFF;\n"
"    font-size: 26px;\n"
"    font-weight: 400;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1E4FD6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1A3FB8;\n"
"}")
        self.rignt_stackedWidget.addWidget(self.finish_dispense_page)

        self.horizontalLayout.addWidget(self.rignt_stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.rignt_stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u5206\u836f\u673a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u672a\u8054\u7f51", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u5206\u836f\u673a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u7f51\u7edc", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u653e\u5165\u7a7a\u836f\u76d8", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6RFID", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u5904\u65b9", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u5206\u836f\u54c1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u836f\u76d8", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u5206\u836f\u4efb\u52a1\u6d41\u7a0b", None))
        self.put_pan_in.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u653e\u5165\u7a7a\u836f\u76d8", None))
        self.RFID_msg.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u836f\u76d8RFID\u6210\u529f", None))
        self.prescription_msg.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u5904\u65b9\u6210\u529f", None))
        self.begin_dispense_.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5206\u836f", None))
        self.current_drug_img.setText("")
        self.current_drug.setText(QCoreApplication.translate("MainWindow", u"\u963f\u83ab\u897f\u6797", None))
        self.patient_name.setText(QCoreApplication.translate("MainWindow", u"\u85cf\u4f59\u6d01", None))
        self.prescription_data.setText(QCoreApplication.translate("MainWindow", u"\u5904\u65b9\u65e5\u671f\uff1a2025\u5e743\u670824\u65e5-2025\u5e743\u670830\u65e5", None))
        self.guide_msg.setText(QCoreApplication.translate("MainWindow", u"\u5171\u9700\u89817\u7247", None))
        self.cam_detection_info.setText(QCoreApplication.translate("MainWindow", u"\u672a\u8fde\u63a5\u6444\u50cf\u5934", None))
        self.tip_to_put_drug_in.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5c06\u836f\u7247\u6295\u5165\u5206\u836f\u673a", None))
        self.progressBar_percentage.setText(QCoreApplication.translate("MainWindow", u"32%", None))
        self.finish_all.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u7ecf\u5206\u5b8c\u6240\u6709\u836f\u54c1", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u836f\u76d8", None))
    # retranslateUi

