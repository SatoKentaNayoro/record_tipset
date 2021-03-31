"""
_*_ coding:utf-8 _*_
_*_ author:iron_huang _*_
_*_ blog:https://www.dvpos.com/ _*_
"""
from parse import start_parse
from download_log import start_copy


if __name__ == '__main__':
    pwd = input("please input your shh password:")
    try:
        err = start_copy(pwd)
        if err != None:
            print(err)
            exit()
        else:
            start_parse()
    except Exception as e:
        print(e)
