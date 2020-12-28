#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os
import random
import string
'''
    代码集:实现文件随机命名自动存储
'''

def make_txt(name, text):  # 定义函数名
    # b = os.getcwd() + '\\newdir\\'
    # if not os.path.exists(b):  # 判断当前路径是否存在，没有则创建new文件夹
    #     os.makedirs(b)
    target_path = os.getcwd()  # 目标路径
    b = target_path + '\\new\\'  # 目标文件夹
    if not os.path.exists(b):  # 判断目标路径下是否包含目标文件夹
        os.makedirs(b)  # 没有则新建该文件夹
    filename = b + name + '.txt'  # 在new文件中创建txt
    print(filename)
    file = open(filename, 'w')  # 打开该文件
    file.write(text)  # 写入内容信息
    file.close()
    print('ok')


def ran():
    # ascii_letters 方法的作用是生成全部字母，包括a-z A-Z  string.ascii_letters
    # digits 方法作用是生成数组，包括0-9 string.digits
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))  # 随机输出8位由英文字符和数字组成的字符串
    print(salt)
    return salt


def write_file():
    for i in range(10):
        make_txt(ran(), ran() * 3)  # 将生成的字符命名为txt名称，然后将名称*3写入该txt



write_file()

