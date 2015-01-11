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
    autoescape=None,
    debug=True,
    cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    ui_modules = ui_modules
)

# application = tornado.web.Application(
#     handlers=url,
#     **setting
# )

class Application(tornado.web.Application):
    def __init__(self):
        handlers=url
        conn = pymongo.Connection("localhost", 27017)
        self.db = conn["Home-Cloud"]
        # self.db.user.insert({"name":"admin","password": "123456"})
        tornado.web.Application.__init__(self, handlers, **setting)