# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import zhfinder, win32api
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Search_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Search_Button.setGeometry(QtCore.QRect(510, 170, 75, 23))
        self.Search_Button.setObjectName("Search_Button")
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(220, 170, 231, 20))
        self.name_input.setObjectName("name_input")
        self.filename_label = QtWidgets.QLabel(self.centralwidget)
        self.filename_label.setGeometry(QtCore.QRect(140, 170, 54, 12))
        self.filename_label.setObjectName("filename_label")
        self.Setting_button = QtWidgets.QPushButton(self.centralwidget)
        self.Setting_button.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.Setting_button.setObjectName("Setting_button")
        self.cert_button = QtWidgets.QPushButton(self.centralwidget)
        self.cert_button.setGeometry(QtCore.QRect(90, 10, 75, 23))
        self.cert_button.setObjectName("cert_button")
        self.About_Button = QtWidgets.QPushButton(self.centralwidget)
        self.About_Button.setGeometry(QtCore.QRect(250, 10, 75, 23))
        self.About_Button.setObjectName("About_Button")
        self.help_Button = QtWidgets.QPushButton(self.centralwidget)
        self.help_Button.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.help_Button.setObjectName("help_Button")
        self.welcome_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.welcome_text.setGeometry(QtCore.QRect(190, 50, 256, 81))
        self.welcome_text.setObjectName("welcome_text")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # --------------------------------------------------------------------------------------- #
        self.Search_Button.clicked.connect(lambda: self.run(self.name_input.text()))
        self.About_Button.clicked.connect(lambda: self.about())
        self.Setting_button.clicked.connect(lambda: self.setting())
        self.help_Button.clicked.connect(lambda: self.help())
        self.cert_button.clicked.connect(lambda: self.cert())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "zhfinder"))
        self.Search_Button.setText(_translate("MainWindow", "搜索"))
        self.filename_label.setText(_translate("MainWindow", "文件名:"))
        self.Setting_button.setText(_translate("MainWindow", "设置"))
        self.cert_button.setText(_translate("MainWindow", "导入根证书"))
        self.About_Button.setText(_translate("MainWindow", "关于此软件"))
        self.help_Button.setText(_translate("MainWindow", "帮助"))
        self.welcome_text.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#00aaff;\">  zhfinder V1.0.0</span></p>\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#00aaff;\">请在下面输入搜索内容</span></p></body></html>"))

    def run(self, text):
        if text != "":
            zhfinder.start_search(text)
        else:
            QMessageBox.information(None, "提示", "文件名不能为空！",
                                    QMessageBox.Ok)

    def setting(self):
        win32api.ShellExecute(0, 'open', 'notepad.exe', 'settings.cfg', '', 1)

    def about(self):
        QMessageBox.about(None, "关于",
                          "zhfinder v1.0.0\nCopyright (C) 2022 Mywslzh \n自由软件,遵循MIT开源协议\n使用条款:\nhttp://119.91.97.178/software/zhfinder/License.html")

    def help(self):
        QMessageBox.information(None, "帮助", "1.直接输入文件名前缀，如:测试\n2.输入全文件名，如:测试.docx\n3.输入通配符，如:*.docx", QMessageBox.Ok)

    def cert(self):
        QMessageBox.information(None, "提示", "暂不支持导入!，请等待1.0.1版本！", QMessageBox.Ok)
