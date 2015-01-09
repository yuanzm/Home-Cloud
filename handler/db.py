class User:
	def __init__(self, db, name, password):
		self.db = db
		self.name = name
		self.password = password
	def saveUser(self):
		coll = self.db.users
		admin = coll.find_ond({"name": "admin"});
		print admin

