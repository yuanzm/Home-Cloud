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
        coll = self.application.db
        name = self.get_secure_cookie("user")
        # pic = Picture(coll, "yuanzm", "heihei","20100413")
        # pic.savePicture()
        # like = Like(coll, "yuanzm", "heihei", "20100413")
        # like.changeLike(1)
        self.render('index.html', title="HomeCloud", name=name, page=1)

class RegistHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_secure_cookie("user")
        if name:
            self.redirect('/')
        else:
            self.render('sign.html', title="Regist", signType="signup", name=name, page="signup")
    def post(self):
        coll = self.application.db
        name = self.get_argument("name", None)
        password = self.get_argument("password", None)
        if name:
            exist = getUser(coll, name)
            if exist is False:
                user = User(coll, name, password)
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
        coll = self.application.db
        name = self.get_argument("name", None)
        password = self.get_argument("password", None)
        user = User(coll, name, password)
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
        coll = self.application.db
        pictures = loadPicture(coll)
        name = self.get_secure_cookie("user")
        self.render('data-list.html', title="Picture", datalist=pictures, dataType="pic", name=name, page=1)


class PicDetailHandler(tornado.web.RequestHandler):
    def get(self, picId):
        coll = self.application.db
        picture = getPicture(coll, picId)
        name = self.get_secure_cookie("user")
        self.render('data-detail.html', title="pic",data=picture, dataType="pic",name=name, page=1)

class VideoHandler(tornado.web.RequestHandler):
    def get(self):
        coll = self.application.db
        videos = loadVideos(coll)
        name = self.get_secure_cookie("user")
        # video = Video(coll, "yuanzm", "真好看")
        # video.saveVideo()
        self.render('data-list.html', title="video",datalist=videos, dataType="video", name=name, page=1)

class VideoDetailHandler(tornado.web.RequestHandler):
    def get(self, videoId):
        coll = self.application.db
        video = getVideo(coll, videoId)
        name = self.get_secure_cookie("user")
        # print video["likes"]
        self.render('data-detail.html', title="Video-detail", data = video, dataType="video", name=name, page=1)