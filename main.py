import easygui
import win32api
import lib
import ui_core
import requests
import os
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox


def log_info(text):
    with open("log.log", 'a+', encoding='utf-8') as f:
        log_text = "[{0}] INFO:{1}".format(lib.get_time(), text)
        f.write(log_text)
        f.write('\n')
    f.close()


def log_error(text):
    with open("log.log", 'a+', encoding='utf-8') as f:
        log_text = "[{0}] ERROR:{1}".format(lib.get_time(), text)
        f.write(log_text)
    f.close()


if __name__ == "__main__":
    log_info('-------------------------------------------------------------------------')
    log_info('程序启动')
    if os.path.exists('updaten.exe'):  # 如果存在updaten.exe，更新update.exe
        os.system('move updaten.exe /Y update.exe')
        log_info('发现需要更新的update.exe')
        log_info(r'执行外部命令:move updaten.exe /Y update.exe')
        log_info('外部命令执行完成')

    if lib.read_config('config', 'updated') == 'True':
        log_info('发现程序已更新，打开发行说明')
        log_info(r'打开readme.html')
        os.system('readme.html')
        lib.write_config('config', 'updated', 'False')
        log_info(r'已前台打开readme.html')
    if lib.read_config('config', 'first_use') == 'True':
        log_info('发现首次使用')
        log_info("""执行弹窗:title='提示', msg='检测到安装完成后未重新启动，将开始建立索引！程序将自动关闭!'""")
        easygui.msgbox(title='提示', msg='检测到安装完成后未重新启动，将开始建立索引！程序将自动关闭!')
        log_info('将调起index.exe进行索引。')
        win32api.ShellExecute(0, 'open', 'index.exe', '', '', 0)
        log_info(r'已后台调起index.exe')
        log_info('打开发行说明readme.html')
        os.system('readme.html')
        log_info(r'已前台打开readme.html')
        lib.write_config('config', 'first_use', 'False')
        sys.exit()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ui_core.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
