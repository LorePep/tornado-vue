import json
import os
from random import randint

import tornado.ioloop
import tornado.web

CURRENT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "."))
DATA_FOLDER = os.path.join(CURRENT_FOLDER, "data")


class GetFileList(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET')

    def get(self):
        response = dict(fileList=[f for f in os.listdir(DATA_FOLDER) if f.endswith(".txt")])
        self.write(json.dumps(response))


def make_app():
    return tornado.web.Application([
        (r"/v1/listfiles", GetFileList),],
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
