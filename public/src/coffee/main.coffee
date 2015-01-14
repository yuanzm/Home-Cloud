Like = require "./add-like.coffee"
Comment = require "./comment.coffee"

like = new Like('data-list')
like.init()

like2 = new Like('data-detail')
like2.init()

comment = new Comment()
comment.bindHandler()
