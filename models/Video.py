#!/usr/bin/env python
# coding=utf-8
import datetime
from bson.objectid import ObjectId
from db import db

class Video(object):
	def __init__(self, author, title, link):
		self.author = author
		self.title = title
		self.link = link
		now = datetime.datetime.now()
		self.time = now.strftime("%m-%d %H:%M:%S")
		self.pv = 0
		self.likes = 0
		self.comments = []
		self.likeperson = []

	def objectSelf(self):
		video = {
			"author": self.author,
			"title": self.title,
			"comments": self.comments,
			"time": self.time,
			"likes": self.likes,
			"link": self.link,
			"likeperson": self.likeperson,
			"pv": self.pv
		}
		return video

	def saveVideo(self):
		db.videos.insert(self.objectSelf())

def loadVideos():
	coll = db.videos
	videos = coll.find()
	return videos

def getVideo(videoId):
	coll = db.videos
	query = {"_id": ObjectId(videoId)}
	video = coll.find_one(query)
	if video:
		video["pv"] += 1
		coll.save(video)
		return video
