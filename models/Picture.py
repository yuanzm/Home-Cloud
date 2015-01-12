#!/usr/bin/env python
# coding=utf-8

from bson.objectid import ObjectId

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

	def __init__(self, db, author,title, time):
		"""Inits Picture."""
		self.db = db
		self.author = author
		self.title = title
		self.time = time
		self.likes = 0
		self.pv = 0
		self.comments = []

	def objectSelf(self):
		""" Package attributes into an dict """
		pic = {
			"author": self.author,
			"title": self.title,
			"time": self.time,
			"likes": self.likes,
			"pv": self.pv,
			"comments": self.comments
		}
		return pic

	def savePicture(self):
		""" Insert the picture into database """
		self.db.pictures.insert(self.objectSelf())

def getPicture(db, picId):
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

def loadPicture(db):
	coll = db.pictures
	pics = coll.find()
	return pics

class Like(object):
	def __init__(self, db, picId):
		self.db = db
		self.picid = picId
	def changeLike(self, likeNum):
		coll = self.db.pictures
		pic = coll.find_one({"_id":ObjectId(picId)})
		pic['likes'] += likeNum
		coll.save(pic)
