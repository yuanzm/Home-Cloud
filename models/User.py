#!/usr/bin/env python
# coding=utf-8

from db import db

class User:
	""" Add a user to the collection `user`

	Attributes:
        name: A String indicating the user's name
        password: A String indicating the user's password
	"""
	def __init__(self, name, password):
		""" init the User """
		self.userInstance = {
			"name": name,
			"password": password
		}

	def saveUser(self):
		""" Insert a `User` instance into database """
		db.user.insert(self.userInstance)

	def getUser(self):
		""" Before inserting a user into database, we need to check whether the user is already in the database """
		coll = db.user
		userData = coll.find_one({"name":self.userInstance["name"],"password": self.userInstance["password"]})
		if userData:
			return True
		else:
			return False 

def getUser(name):
	""" check whether a user is already in the database """
	coll = db.user
	query = {"name": name}
	name = coll.find_one(query)
	if name:
		return True
	return False
