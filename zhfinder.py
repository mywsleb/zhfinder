import lib
from easygui import msgbox
import os, sys
import win32api
from PyQt5 import QtCore, QtGui, QtWidgets
from easygui import textbox


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


def start_search(keyword):
    try:
        with open('index.index', 'r', encoding='utf-8') as f:
            index = f.readlines()
            f.close()
    except Exception as err:
        msgbox(title='错误', msg='无法读取索引文件:{0}'.format(str(err)))
        log_error('无法读取索引文件:{0}'.format(str(err)))

    if not index:  # 如果索引是空的
        with open('index.index.bak', 'r', encoding='utf-8') as f:
            index = f.readlines()
            log_info('发现index.index为空，使用备份索引')

    index_fine = []
    for i in index:
        tmp = i.strip('\n')
        index_fine.append(tmp)
    lines = []
    log_info('索引添加完毕')
    log_info('共读取了{0}索引。'.format(len(index_fine)))
    keyword_str = keyword
    keyword = keyword.split('.')
    keyword_len = len(keyword)
    search_type = 0
    if keyword_len == 1:
        search_type = 1
    elif keyword_len >= 2:
        if '*' not in keyword[0] and keyword[1] == '*':  # filename.*
            search_type = 2
        elif keyword[0] == '*' and keyword[1] != '*':  # *.name
            search_type = 3
        elif keyword[0] != "*" and keyword[1] != '*':
            search_type = 4
    results = []
    if search_type == 1 or search_type == 2:
        for i in index_fine:
            temp = i.split('\\')[-1].split('.')[0]
            if temp.upper() == keyword[0].upper():
                results.append(i)
                results.append('\n')
    if search_type == 3:
        for i in index_fine:
            temp = i.split('\\')[-1].split('.')[-1]
            if temp.upper() == keyword[-1].upper():
                results.append(i)
                results.append('\n')
    if search_type == 4:
        for i in index_fine:
            temp = i.split('\\')[-1]
            if temp == keyword_str:
                results.append(i)
                results.append('\n')
    textbox(title='搜索结果-zhfinder', msg='搜索结果如下', text=''.join(results))

