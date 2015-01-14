#!/usr/bin/env python
# coding=utf-8

import datetime
from bson.objectid import ObjectId

from db import db

class Picture(object):
	""" Database operation on a picture

	Before inserting a picture to the database,we need to add some attributes on the picture.
	Some attributes maybe private,some maybe public.
	
	Attributes:
        db: The database we operate
        author: A String indicating the picture's author
        title: A String descrip the picture briefly
        time: A String indicating the picture's shooting time 

	"""

	def __init__(self, author,title, link):
		"""Inits Picture."""
		self.author = author
		self.title = title
		self.link = link
		now = datetime.datetime.now()
		self.time = now.strftime("%Y-%m-%d %H:%M:%S")
		self.likes = 0
		self.pv = 0
		self.comments = []
		self.likeperson = []

	def objectSelf(self):
		""" Package attributes into an dict """
		pic = {
			"author": self.author,
			"title": self.title,
			"time": self.time,
			"likes": self.likes,
			"pv": self.pv,
			"comments": self.comments,
			"likeperson": self.likeperson,
			"link": self.link
		}
		return pic

	def savePicture(self):
		""" Insert the picture into database """
		db.pictures.insert(self.objectSelf())

def getPicture(picId):
	""" Query a picture from the database through _id """
	coll = db.pictures
	query = {"_id": ObjectId(picId)}
	pic = coll.find_one(query)
	if pic:
		pic["pv"] += 1
		coll.save(pic)
		return pic
	else:
		return None

def loadPicture():
	coll = db.pictures
	pics = coll.find()
	return pics

class Like(object):
	def __init__(self, myName, dataId, dataType, likeChange):
		self.myName = myName
		self.dataId = dataId
		self.dataType = dataType
		self.likeChange = likeChange

	def changeLike(self):
		""" Change the likes number for a picture or a video """
		if self.dataType == "pic":
			coll = db.pictures
		else:
			coll = db.videos
		
		query = {"_id":ObjectId(self.dataId)}
		data = coll.find_one(query)
		data["likes"] += int(self.likeChange)
		name = self.myName
		likePerson = data["likeperson"]
		if int(self.likeChange) == 1:
			likePerson.append(self.myName)
		else:
			likePerson.remove(self.myName)
		data["likeperson"] = likePerson
		coll.save(data)

class Comment(object):
	def __init__(self,myName, dataId, dataType, commentText):
		self.myName = myName
		self.dataId = dataId
		self.dataType = dataType
		self.commentText = commentText

	def addComment(self):
		if self.dataType == "pic":
			coll = db.pictures
		else:
			coll = db.videos

		comment = {
			"commenter": self.myName,
			"content": self.commentText
		}
		query ={"_id":ObjectId(self.dataId)}
		pic = coll.find_one(query)
		com = pic["comments"] 
		com.append(comment)
		pic["comments"] = com
		coll.save(pic)
