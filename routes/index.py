#!/usr/bin/env python
# coding=utf-8

import os.path
import tornado.web

import sys
sys.path.append("./..")


from models.User import User
from models.User import getUser
from models.Picture import Picture

class HTTP404Error(tornado.web.ErrorHandler):
    def initialize(self):
        tornado.web.ErrorHandler.initialize(self, 404)

    def prepare(self):
        self.render('404.html')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # coll = self.application.db
        # pic = Picture(coll, "yuanzm", "heihei","20100413")
        # pic.savePicture()
        self.render('index.html', title="HomeCloud")

class RegistHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('regist.html', title="Regist")
    def post(self):
        coll = self.application.db
        name = self.get_argument("name", None)
        password = self.get_argument("password", None)
        if name:
            exist = getUser(coll, name)
            if exist is False:
                user = User(coll, name, password)
                user.saveUser()
                self.redirect('/')
            else:
                self.redirect('/regist')
                
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html', title="Login")
    def post(self):
        coll = self.application.db
        name = self.get_argument("name", None)
        password = self.get_argument("password", None)
        user = User(coll, name, password)
        if user.getUser():
            self.redirect('/')
        else:
            self.redirect('/login')

class PicHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('pic.html', title="Picture")

class PicDetailHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('pic-detail.html', title="pic")

