import datetime
import sqlite3

conn = sqlite3.connect('cfg.db')
cur = conn.cursor()


def write_config(table_name, column_name, value):
    sql = "UPDATE {0} SET {1}='{2}'".format(table_name, column_name, value)
    print(sql)
    cur.execute(sql)
    conn.commit()


def read_config(table_name, column_name):
    sql = "SELECT {0} FROM {1}".format(column_name, table_name)
    print(sql)
    cur.execute(sql)
    return cur.fetchall()[0][0]


def read_settings(line):
    f = open('settings.cfg', 'r', encoding='utf-8')
    tmp = f.readlines()
    f.close()
    return tmp[line - 1]


def get_time():
    now = datetime.datetime.now()
    return now
