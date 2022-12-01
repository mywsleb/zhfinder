import os, easygui
import psutil
import datetime
import sys
import time
import threading
import win32api
from index_lib import *
import lib


def log_info(text):
    with open("index.log", 'a+', encoding='utf-8') as f:
        log_text = "[{0}] INFO:{1}".format(lib.get_time(), text)
        f.write(log_text)
        f.write('\n')
    f.close()


def run():
    log_info("开始执行索引任务")
    disk_list = get_disk_list()  # 获取磁盘列表，函数位置：index_lib.py
    log_info('获取磁盘完毕，结果:{0}'.format(disk_list))
    disk_num = len(disk_list)
    index_mode = 0  # index_mode:索引模式,1=1线程,2=2线程,3=3线程
    if disk_num == 1:  # 分区数量为1，单线程        index_mode = 1
        th1_disk = disk_list
    if disk_num == 2:  # 分区数量为2，2线程
        index_mode = 2
        th1_disk = disk_list[0]
        th2_disk = disk_list[1]
    if disk_num >= 3:  # 分区数量为>=3，3线程
        index_mode = 3
        th1_disk = []
        th2_disk = []
        th3_disk = []
    log_info('确定索引模式完毕. {0}线程建立'.format(index_mode))
    f = open('settings.cfg', 'r', encoding='utf-8')
    no_index_dirs = f.readlines()[4:]
    f.close()
    for i in range(len(no_index_dirs) - 1):
        no_index_dirs[i] = no_index_dirs[i].strip('\n')

    if index_mode == 1:
        t1 = threading.Thread(target=get_file_path, args=(th1_disk, no_index_dirs))
        t1.start()
        log_info("线程总数:1,线程1/1启动")
    if index_mode == 2:
        t1 = threading.Thread(target=get_file_path, args=(th1_disk, no_index_dirs))
        t2 = threading.Thread(target=get_file_path, args=(th2_disk, no_index_dirs))
        t1.start()
        log_info("线程总数:2，线程1/2启动")
        t2.start()
        log_info("线程总数:2，线程2/2启动")

    if index_mode == 3:
        fg = disk_num // 3
        for disk in range(fg):
            th1_disk.append(disk_list[0])  # 分配每个线程的索引任务
            disk_list.pop(0)
        for disk in range(fg):
            th2_disk.append(disk_list[0])
            disk_list.pop(0)
        th3_disk = disk_list
        log_info("线程任务分配完成，线程1:{0}，线程2:{1}，线程3:{2}".format(th1_disk, th2_disk, th3_disk))
        t1 = threading.Thread(target=get_file_path, args=(th1_disk, no_index_dirs))
        t2 = threading.Thread(target=get_file_path, args=(th2_disk, no_index_dirs))
        t3 = threading.Thread(target=get_file_path, args=(th3_disk, no_index_dirs))
        t1.start()
        log_info("线程总数:3，线程1/3启动")
        t2.start()
        log_info("线程总数:3，线程2/3启动")
        t3.start()
        log_info("线程总数:3，线程3/3启动")


def clean():
    log_info('开始备份索引')
    with open('index.index', 'r', encoding='utf8') as l:
        s = l.readlines()
        l.close()
    l = open('index.index', 'w', encoding='utf8')  # 清空索引
    l.close()
    log_info('索引已清空.')
    with open('index.index.bak', 'w', encoding='utf8') as l:
        for i in s:
            l.write(i)
    log_info('索引已完成备份.')


if __name__ == '__main__':
    log_info('index.exe启动')
    last_index_time = lib.read_config('config', 'last_index_time')
    if last_index_time != datetime.date.strftime(datetime.datetime.today(), '%Y-%m-%d'):  # 如果今天没有建立索引
        log_info('上次建立时间非今日，需要建立索引，开始建立.')
        clean()
        run()
        lib.write_config('config', 'last_index_time',
                         str(datetime.date.strftime(datetime.datetime.today(), '%Y-%m-%d')))

    while True:
        index_time = int(lib.read_settings(2).split('=')[-1])
        if index_time == -1:
            sys.exit(0)
        time.sleep(index_time)
        run()
