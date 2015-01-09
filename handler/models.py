#!/usr/bin/env python
# coding=utf-8

import os.path
import tornado.web

from db import User

class HTTP404Error(tornado.web.ErrorHandler):
    def initialize(self):
        tornado.web.ErrorHandler.initialize(self, 404)

    def prepare(self):
        self.render('404.html')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', title="HomeCloud")

class RegistHandler(tornado.web.RequestHandler):
	def get(self):
        # coll = self.application.db.users
        user=User(local, "admin", "123456")
        user.saveUser()
		self.render('regist.html', title="Regist")

class LoginHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('login.html', title="Login")

class PicHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('pic.html', title="相册")