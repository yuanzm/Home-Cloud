import datetime
from bson.objectid import ObjectId

class Comment(object):
	def __init__(self, db, _id, content, commenter):
		self.db = db
		self._id = _id
		self.commenter = commenter
		self.content = content
		now = datetime.datetime.now()
		self.time = now.strftime("%Y-%m-%d %H:%M:%S")

	def addComment(self):
		coll = self.db.pictures
		comment = {
			"commenter": self.commenter,
			"time": self.time,
			"content": self.content
		}
		query ={"_id":ObjectId(self._id)}
		pic = coll.find_one(query);
		pic["comments"].append(comment)
		coll.save(pic)

def loadComments(db, _id):
	coll = self.pictures
	query = {"_id": ObjectId(_id)}
	pic = coll.find(query)
	if pic:
		if len(comments):
			comments = pic["comments"]
			return comments
	return None
