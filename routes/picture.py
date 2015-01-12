#!/usr/bin/env python
# coding=utf-8

import os.path
import tornado.web

import sys
sys.path.append("./..")

from models.Picture import Like

class addLikeToPictureHandler(tornado.web.RequestHandler):
	def post(self):
		coll = self.application.db
		likeNum = int(self.get_argument("likeNum", None))
		author = self.get_argument("author", None)
		title = self.get_argument("title", None)
		time = self.get_argument("time", None)
		like = Like(coll, author, title, time)
		like.changeLike(likeNum)
