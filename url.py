#!/usr/bin/env python
#coding:utf-8

#如果文件里面有汉字，避免出现乱码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from handler.models import IndexHandler
from handler.models import HTTP404Error
from handler.models import RegistHandler
from handler.models import LoginHandler
from handler.models import PicHandler

url = [
    (r'/', IndexHandler),
    (r'/regist', RegistHandler),
    (r'/login', LoginHandler),
    (r'/pic', PicHandler),
    (r'.*', HTTP404Error)
]