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

class HTTP404Error(tornado.web.ErrorHandler):
    """ A class handler the not existed url request"""

    def initialize(self):
        tornado.web.ErrorHandler.initialize(self, 404)

    def prepare(self):
        """ Return `404` page for all the not existed url request """
        self.render('404.html')

class IndexHandler(tornado.web.RequestHandler):
    """  A class handler for the url `/` request """
    def get(self):
        """ load home page """
        name = self.get_secure_cookie("user")
        self.render('index.html', title="HomeCloud", name=name, page=1)

class RegistHandler(tornado.web.RequestHandler):
    """  A class handler for the url `/regist` request """
    def get(self):
        """Return `regist` page for the `/regist` get request """
        name = self.get_secure_cookie("user")
        if name:
            self.redirect('/')
        else:
            self.render('sign.html', title="Regist", signType="signup", name=name, page="signup")
    def post(self):
        """handler for the submit of from in `regist` page """
        name = self.get_argument("name", None)
        password = self.get_argument("password", None)
        if name:
            exist = getUser(name)
            if exist is False:
                user = User(name, password)
                user.saveUser()
                self.set_secure_cookie("user", name, httponly = True, secure = True)
                self.redirect('/')
            else:
                self.redirect('/regist')
                
class LoginHandler(tornado.web.RequestHandler):
    """  A class handler for the url `/login` request """
    def get(self):
        """Return `login` page for the `/login` get request """
        name = self.get_secure_cookie("user")
        if name:
            self.redirect('/')
        else:
            self.render('sign.html', title="Login", signType="login", name=name, page=1)

    def post(self):
        """handler for the submit of from in `login` page """
        name = self.get_argument("name", None)
        password = self.get_argument("password", None)
        user = User(name, password)
        if user.getUser():
            self.set_secure_cookie("user", name, httponly = True, secure = True)
            self.redirect('/')
        else:
            self.redirect('/login')

class LogoutHandler(tornado.web.RequestHandler):
    """  A class handler for the url `/logout` request """
    def get(self):
        self.set_secure_cookie("user", '', httponly = True, secure = True)
        self.redirect('/')

class PicHandler(tornado.web.RequestHandler):
    """  A class handler for the url `/pic` request """
    def get(self):
        """ Return all the pictures for the request """
        pictures = loadPicture()
        name = self.get_secure_cookie("user")
        self.render('data-list.html', title="Picture", datalist=pictures, dataType="pic", name=name, page=1)

class PicDetailHandler(tornado.web.RequestHandler):
    """  A class handler for the url `/pic/(\w+)` request """
    def get(self, picId):
        """ Return a specific picture according the id of picture """
        picture = getPicture(picId)
        name = self.get_secure_cookie("user")
        self.render('data-detail.html', title="pic",data=picture, dataType="pic",name=name, page=1)

class VideoHandler(tornado.web.RequestHandler):
    """  A class handler for the url `/video` request """
    def get(self):
        """ Return all the videos for the request """
        videos = loadVideos()
        name = self.get_secure_cookie("user")
        self.render('data-list.html', title="video",datalist=videos, dataType="video", name=name, page=1)

class VideoDetailHandler(tornado.web.RequestHandler):
    """  A class handler for the url `/video/(\w+)` request """
    def get(self, videoId):
        """ Return a specific video according the id of video """
        video = getVideo(videoId)
        name = self.get_secure_cookie("user")
        self.render('data-detail.html', title="Video-detail", data = video, dataType="video", name=name, page=1)
