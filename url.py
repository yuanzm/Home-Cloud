#!/usr/bin/env python
#coding:utf-8

#如果文件里面有汉字，避免出现乱码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from handler.models import IndexHandler
from handler.models import HTTP404Error

url = [
    (r'/', IndexHandler),
    (r'.*', HTTP404Error)
]