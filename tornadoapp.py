import os
from tornado import ioloop,web
from tornado.escape import json_encode
from pymongo import MongoClient
import json
from bson import json_util
from bson.objectid import ObjectId
from url import url
from mockdata import restart

from routes.uimodule import ui_modules

# settings = {
#     "template_path": os.path.join(os.path.dirname(__file__), "templates"),
#     "static_path": os.path.join(os.path.dirname(__file__), "public"),
#     "debug" : True,
#     'cookie_secret': "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
#     'ui_modules':ui_modules
# }

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__),"templates"),
    static_path=os.path.join(os.path.dirname(__file__),"public"),
    debug=True,
    cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    xsrf_cookies=False,
    ui_modules = ui_modules
)

restart()
application = web.Application(url,**settings)

if __name__ == "__main__":
	restart()
	application.listen(8888)
	ioloop.IOLoop.instance().start()
