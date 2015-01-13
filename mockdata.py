#!/usr/bin/env python
# coding=utf-8

from models.Picture import Picture

pictures = [
	{"author": "爸爸", "title": "今天天气真好"},
	{"author": "妈妈", "title": "记得回家吃饭"},
	{"author": "爷爷", "title": "常回家看看"},
	{"author": "妈妈", "title": "还是家里好"},
	{"author": "妈妈", "title": "还是家里棒"},
	{"author": "妈妈", "title": "真棒"}
]

for picture in pictures:
	pic = Picture(picture["author"], picture["title"])
	pic.savePicture()
