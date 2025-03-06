import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from lesson import Lesson
from traceback import print_exc
from console import Console
from config import Config
from threading import Thread


class Server:
    def __init__(self):
        Console.log(
            Console.blue, f"Server is running on http://localhost:{Config.SERVER_PORT}"
        )
        server = HTTPServer(("0.0.0.0", Config.SERVER_PORT), self.ServerHandler)
        server.serve_forever()

    class ServerHandler(BaseHTTPRequestHandler):
        UTF_8 = "utf-8"
        URL = "url"
        EMAIL = "email"
        MSG = "msg"
        BASE_PATH = "/lesson/"

        def _return_response(self, status: int = 200, data=None):
            self.send_response(status)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode(self.UTF_8))

        def _convert_request(self):
            content_length = int(self.headers["Content-Length"])
            read_data = self.rfile.read(content_length).decode(self.UTF_8)
            data_handle = json.loads(read_data)
            return data_handle

        def serializer(self, data: dict):
            REQUIRED_KEYS = [self.URL, self.EMAIL]
            result = list(filter(lambda k: k not in REQUIRED_KEYS, data.keys()))
            if len(result):
                self._return_response(400, {self.MSG: "invalid body"})
                return False
            return True

        def do_POST(self):
            if self.BASE_PATH == self.path:
                self.create()

        def create(self):
            data = self._convert_request()
            is_valid = self.serializer(data)
            if is_valid:
                try:
                    Thread(
                        target=Lesson, args=[data[self.URL], data[self.EMAIL]]
                    ).start()
                    self._return_response(
                        202, {"msg": "Track the request in the console"}
                    )
                except Exception as err:
                    print_exc()
                    self._return_response(500, {"msg": str(err)})


if __name__ == "__main__":
    Server()
