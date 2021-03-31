"""
_*_ coding:utf-8 _*_
_*_ author:iron_huang _*_
_*_ blog:https://www.dvpos.com/ _*_
"""
from datetime import datetime
import time
from logger import logger
import base64
import binhex
import codecs

def printlog():
   logger.error("asdadasd")

if __name__ == '__main__':


   hex = "cde2c5046c918e0888ec04268d33502ef231946da9a550c0d03f8ccf1a980c30"
   mid = codecs.decode(hex, 'hex')
   print(mid)
   b64 = codecs.encode(mid, 'base64')
   print(type(b64))
   b = b64.decode()
   print(type(b))
