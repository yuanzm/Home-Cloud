class User:
	def __init__(self, db, name, password):
		self.db = db
		self.name = name
		self.password = password
	def saveUser(self):
		coll = self.db
		admin = coll.find_one({"name": "admin"});
		print admin
