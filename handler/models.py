#!/usr/bin/env python
# coding=utf-8

import os.path
import tornado.web

class HTTP404Error(tornado.web.ErrorHandler):
    def initialize(self):
        tornado.web.ErrorHandler.initialize(self, 404)

    def prepare(self):
        self.render('404.html')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')