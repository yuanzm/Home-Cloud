#!/usr/bin/env python
# coding=utf-8

from models.Picture import Picture
from models.Video import Video
from models.db import db

# remove records in database
db.pictures.remove()
db.videos.remove()

pictures = [
	{"author": "爸爸", "title": "今天天气真好", "link": "http://lorempixel.com/output/city-q-c-640-480-10.jpg"},
	{"author": "妈妈", "title": "记得回家吃饭", "link": "http://lorempixel.com/output/food-q-c-640-480-4.jpg"},
	{"author": "爷爷", "title": "常回家看看", "link": "http://lorempixel.com/output/food-q-c-640-480-8.jpg"},
	{"author": "妈妈", "title": "还是家里好", "link": "http://lorempixel.com/output/nightlife-q-c-640-480-7.jpg"},
	{"author": "妈妈", "title": "还是家里棒", "link": "http://lorempixel.com/output/nightlife-q-c-640-480-5.jpg"},
	{"author": "妈妈", "title": "真棒", "link": "http://lorempixel.com/output/sports-q-c-640-480-6.jpg"}
]

videos = [
	{"author": "爸爸", "title": "今天天气真好", "link": "http://video-js.zencoder.com/oceans-clip"},
	{"author": "妈妈", "title": "海鸥好漂亮", "link": "http://video-js.zencoder.com/oceans-clip"}
]


for picture in pictures:
	pic = Picture(picture["author"], picture["title"], picture["link"])
	pic.savePicture()

for video in videos:
	avideo = Video(video["author"], video["title"], video["link"])
	avideo.saveVideo()
	