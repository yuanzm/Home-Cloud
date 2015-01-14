import datetime
from bson.objectid import ObjectId

class Comment(object):
	def __init__(self,myName, dataId, dataType, commentText):
		self.myName = myName
		self.dataId = dataId
		self.dataType = dataType
		self.commentText = commentText

	def addComment(self):
		if self.dataType == "pic":
			coll = db.pictures
		else:
			coll = db.videos

		comment = {
			"commenter": self.myName,
			"content": self.commentText
		}
		query ={"_id":ObjectId(self.dataId)}
		pic = coll.find_one(query)
		com = pic["comments"] 
		com.append(comment)
		pic["comments"] = com
		coll.save(pic)
