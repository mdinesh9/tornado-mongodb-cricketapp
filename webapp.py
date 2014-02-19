import tornado.ioloop
import tornado.web
import webbrowser
import tornado.options
from tornado import escape
import os
import time

from pymongo import Connection
db = Connection().cricket

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        results = [cricketer for cricketer in db.cricket.find()]
        self.render("index.html", results = results)

def launcher():
    application = tornado.web.Application([
        (r"/", MainHandler),
        ],
            debug=True,
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
        )
    application.listen(8888)
    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    launcher()