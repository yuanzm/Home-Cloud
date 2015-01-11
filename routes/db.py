#!/usr/bin/env python
# coding=utf-8

class User:
	def __init__(self, db, name, password):
		self.userInstance = {
			"name": name,
			"password": password
		}
		self.db = db
	def saveUser(self):
		self.db.user.insert(self.userInstance)
	def getUser(self):
		coll = self.db.user
		userData = coll.find_one({"name":self.userInstance["name"],"password": self.userInstance["password"]})
		if userData:
			return True
		else:
			return False 

def getUser(db, name):
	coll = db.user
	query = {"name": name}
	name = coll.find_one(query)
	if name:
		return True
	return False
