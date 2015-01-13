#!/usr/bin/env python
# coding=utf-8

import os.path
import tornado.web

import sys
sys.path.append("./..")

from models.Picture import Like

class addLikeHandler(tornado.web.RequestHandler):
	def post(self):
		db = self.application.db
		myName = self.get_argument("myName")
		dataId = self.get_argument("dataId")
		dataType = self.get_argument("dataType")
		likeChange = self.get_argument("likeChange")

		like = Like(myName, dataId, dataType, likeChange)
		like.changeLike()
				