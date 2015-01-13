#!/usr/bin/env python
# coding=utf-8

from db import db

class User:
	def __init__(self, name, password):
		self.userInstance = {
			"name": name,
			"password": password
		}

	def saveUser(self):
		self.db.user.insert(self.userInstance)

	def getUser(self):
		coll = db.user
		userData = coll.find_one({"name":self.userInstance["name"],"password": self.userInstance["password"]})
		if userData:
			return True
		else:
			return False 

def getUser(name):
	coll = db.user
	query = {"name": name}
	name = coll.find_one(query)
	if name:
		return True
	return False
