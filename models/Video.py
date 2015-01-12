#!/usr/bin/env python
# coding=utf-8
import datetime
from bson.objectid import ObjectId

class Video(object):
	def __init__(self, db, author, title):
		self.db = db
		self.author = author
		self.title = title
		now = datetime.datetime.now()
		self.time = now.strftime("%Y-%m-%d %H:%M:%S")
		self.broadcast = 0
		self.likes = 0
		self.comments = []

	def objectSelf(self):
		video = {
			"author": self.author,
			"title": self.title,
			"broadcast": self.broadcast,
			"comments": self.comments,
			"time": self.time,
			"likes": self.likes
		}
		return video

	def saveVideo(self):
		self.db.videos.insert(self.objectSelf())

def loadVideos(db):
	coll = db.videos
	videos = coll.find()
	return videos

def getVideo(db, videoId):
	coll = db.videos
	query = {"_id": ObjectId(videoId)}
	video = coll.find_one(query)
	return video
