#!/usr/bin/env python
# coding=utf-8

from url import url 

import os.path
import tornado.web
import pymongo

from routes.uimodule import ui_modules

setting = dict(
    template_path=os.path.join(os.path.dirname(__file__),"template"),
    static_path=os.path.join(os.path.dirname(__file__),"public"),
    debug=True,
    cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    xsrf_cookies=True,
    ui_modules = ui_modules
)

class Application(tornado.web.Application):
    def __init__(self):
        handlers=url
        tornado.web.Application.__init__(self, handlers, **setting)