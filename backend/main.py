import json
from random import randint

import tornado.ioloop
import tornado.web


class GenerateRandom(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET')

    def get(self):
        response = dict(randomNumber=randint(1, 100))
        self.write(json.dumps(response))


def make_app():
    return tornado.web.Application([
        (r"/v1/random", GenerateRandom),],
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
