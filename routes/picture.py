#!/usr/bin/env python
# coding=utf-8

import os.path
import tornado.web

import sys
sys.path.append("./..")

from models.Picture import Like
from models.Picture import Comment

class addLikeHandler(tornado.web.RequestHandler):
	"""  A class handler for the url `/data/changelike` request """
	def post(self):
		myName = self.get_argument("myName")
		dataId = self.get_argument("dataId")
		dataType = self.get_argument("dataType")
		likeChange = self.get_argument("likeChange")

		like = Like(myName, dataId, dataType, likeChange)
		like.changeLike()
				
class addCommentHandler(tornado.web.RequestHandler):
	"""  A class handler for the url `/data/addcomment` request """
	def post(self):
		myName = self.get_argument("myName")
		dataId = self.get_argument("dataId")
		dataType = self.get_argument("dataType")
		commentText = self.get_argument("commentText")
		print myName
		comment = Comment(myName, dataId, dataType, commentText)
		comment.addComment()