"""
_*_ coding:utf-8 _*_
_*_ author:iron_huang _*_
_*_ blog:https://www.dvpos.com/ _*_
"""
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
terminal_handler = logging.StreamHandler()
terminal_handler.setLevel(logging.DEBUG)
fmt = logging.Formatter("%(asctime)s-%(module)s(%(lineno)d) %(levelname)s-%(message)s")
terminal_handler.setFormatter(fmt)
logger.addHandler(terminal_handler)
