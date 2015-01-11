#!/usr/bin/env python
# coding=utf-8

class Picture:
	def __init__(self, db, author,title, time):
		self.db = db
		self.author = author
		self.title = title
		self.time = time
		self.likes = 0
		self.pv = 0
		self.comments = []
	def objectSelf(self):
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
		self.db.pictures.insert(self.objectSelf())

def getPicture(db, author, title, time):
	coll = db.pictures
	query = {
		"author": author,
		"title": title,
		"time": time
	}
	pic = coll.find_one(query)
	if pic:
		return pic
	else:
		return None