#!/usr/bin/env python
# coding=utf-8
import datetime
from bson.objectid import ObjectId
from db import db

class Video(object):
	""" Database operation on a video

	Before inserting a picture to the database,we need to add some attributes on the picture.
	Some attributes maybe private,some maybe public.
	
	Attributes:
        author: A String indicating the video's author
        title: A String descrip the video briefly
		"link": A String indicating the video's link
	"""
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
		"""Encapsulate all the attributes of the video into a dict"""
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
		""" Insert a video into the database """
		db.videos.insert(self.objectSelf())

def loadVideos():
	""" Load all videos in the database """
	coll = db.videos
	videos = coll.find()
	return videos

def getVideo(videoId):
	""" Check a video is in the database according to the id of the video,
		if exist, return all the fields of the video.
	"""
	coll = db.videos
	query = {"_id": ObjectId(videoId)}
	video = coll.find_one(query)
	if video:
		video["pv"] += 1
		coll.save(video)
		return video
