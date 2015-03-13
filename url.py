#!/usr/bin/env python
#coding:utf-8

#如果文件里面有汉字，避免出现乱码
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from routes.index import IndexHandler
from routes.index import HTTP404Error
from routes.index import RegistHandler
from routes.index import LoginHandler
from routes.index import LogoutHandler
from routes.index import PicHandler
from routes.index import PicDetailHandler
from routes.index import VideoHandler
from routes.index import VideoDetailHandler

from routes.picture import addLikeHandler
from routes.picture import addCommentHandler

url = [
    (r'/', IndexHandler),
    (r'/logout', LogoutHandler),
    (r'/regist', RegistHandler),
    (r'/login', LoginHandler),
    (r'/pic', PicHandler),
    (r'/pic/(\w+)', PicDetailHandler),
    (r'/video/(\w+)', VideoDetailHandler),
    (r'/video', VideoHandler),
    (r'/data/changelike', addLikeHandler),
    (r'/data/addcomment', addCommentHandler),
    (r'.*', HTTP404Error)
]