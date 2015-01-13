#!/usr/bin/env python
# coding=utf-8

import os.path
import tornado.web

import sys
sys.path.append("./..")

from models.User import User
from models.User import getUser
from models.Picture import Picture
from models.Picture import getPicture
from models.Picture import loadPicture
from models.Video import Video
from models.Video import getVideo
from models.Video import loadVideos
from models.Comment import Comment

class HTTP404Error(tornado.web.ErrorHandler):
    def initialize(self):
        tornado.web.ErrorHandler.initialize(self, 404)

    def prepare(self):
        self.render('404.html')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_secure_cookie("user")
        self.render('index.html', title="HomeCloud", name=name, page=1)

class RegistHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_secure_cookie("user")
        if name:
            self.redirect('/')
        else:
            self.render('sign.html', title="Regist", signType="signup", name=name, page="signup")
    def post(self):
        name = self.get_argument("name", None)
        password = self.get_argument("password", None)
        if name:
            exist = getUser(name)
            if exist is False:
                user = User(name, password)
                user.saveUser()
                self.set_secure_cookie("user", name)
                self.redirect('/')
            else:
                self.redirect('/regist')
                
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_secure_cookie("user")
        print name
        if name:
            self.redirect('/')
        else:
            self.render('sign.html', title="Login", signType="login", name=name, page=1)
    def post(self):
        name = self.get_argument("name", None)
        password = self.get_argument("password", None)
        user = User(name, password)
        if user.getUser():
            self.set_secure_cookie("user", name)
            self.redirect('/')
        else:
            self.redirect('/login')

class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_secure_cookie("user", '')
        self.redirect('/')

class PicHandler(tornado.web.RequestHandler):
    def get(self):
        pictures = loadPicture()
        name = self.get_secure_cookie("user")
        self.render('data-list.html', title="Picture", datalist=pictures, dataType="pic", name=name, page=1)

class PicDetailHandler(tornado.web.RequestHandler):
    def get(self, picId):
        picture = getPicture(picId)
        name = self.get_secure_cookie("user")
        self.render('data-detail.html', title="pic",data=picture, dataType="pic",name=name, page=1)

class VideoHandler(tornado.web.RequestHandler):
    def get(self):
        videos = loadVideos()
        name = self.get_secure_cookie("user")
        self.render('data-list.html', title="video",datalist=videos, dataType="video", name=name, page=1)

class VideoDetailHandler(tornado.web.RequestHandler):
    def get(self, videoId):
        video = getVideo(videoId)
        name = self.get_secure_cookie("user")
        self.render('data-detail.html', title="Video-detail", data = video, dataType="video", name=name, page=1)