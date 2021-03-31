"""
_*_ coding:utf-8 _*_
_*_ author:iron_huang _*_
_*_ blog:https://www.dvpos.com/ _*_
"""
import os
from datetime import date, timedelta

BASE_PATH = os.path.abspath(".")
DOCS_PATH = os.path.join(BASE_PATH, "docs")
TARGET_IP = "192.168.99.162"
USER_NAME = "abm"
LOCAL_MINER_NAME = "minerlog.txt"
LOCAL_DAEMON_NAME = "deamonlog.txt"
REMOTE_MINER_PATH = "minerlog.log"
REMOTE_DAEMON_PATH = "daemonlog.log"
PORT = 22

URL = "http://xxx.xxx.xxx.xxx:1234/rpc/v0" # lotus damon ListenAddress
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBbGxvdyI6WyJyZWFkIiwid3JpdGUiXX0.rKaekHx8ZjG1t0xeEWSL6q2-7ECegQg6sjMb1RqJedI"
DATE_TO_RECORD = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")
RECORDER_LOCATION = os.path.join(DOCS_PATH, DATE_TO_RECORD + ".xlsx")
FILE_TYPE = '.xlsx'

LOC_BEFORE_REMOTE = "本地早于远端"
LOC_AFTER_REMOTE = "本地晚于远端"
LOC_EQU_REMOTE = "本地等于远端"
