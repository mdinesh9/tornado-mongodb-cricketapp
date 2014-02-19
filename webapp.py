import tornado.ioloop
import tornado.web
import tornado.options
import os

# Connect with pymongo client
from pymongo import Connection
db = Connection().cricket

# This handler class will work when the user hits http://localhost:8888
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Since the data is very less here. I used a list here.
        results = [cricketer for cricketer in db.cricket.find()]
        self.render("index.html", results = results)  # Render the html page with the results

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

# Call the launcher function.
if __name__ == "__main__":
    launcher()