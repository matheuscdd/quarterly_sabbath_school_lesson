import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from lesson import lesson

class ServerHandler(BaseHTTPRequestHandler):
    UTF_8 = 'utf-8'
    URL = 'url'
    MSG = 'msg'
    BASE_PATH = '/lesson/'
    
    
    def _return_response(self, status: int = 200, data = None):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode(self.UTF_8))

    def _convert_request(self):
        content_length = int(self.headers['Content-Length']) 
        read_data = self.rfile.read(content_length).decode(self.UTF_8)
        data_handle = json.loads(read_data)
        return data_handle

    def serializer(self, data: dict):
        REQUIRED_KEYS = [self.URL]
        result = list(filter(lambda k: k not in REQUIRED_KEYS, data.keys()))
        if len(result):
            self._return_response(400, {self.MSG: 'invalid body'})
            return False
        return True
    
    def do_POST(self):
        if self.BASE_PATH == self.path:
            self.create()
    
    def create(self):
        data = self._convert_request()
        is_valid = self.serializer(data)
        if is_valid:
            lesson(data["url"])
            self._return_response(201, data)


def run():
    PORT = 8000
    print(f'Server is running on http://localhost:{PORT}/')
    server = HTTPServer(('0.0.0.0', PORT), ServerHandler)
    server.serve_forever()

if __name__ == '__main__':
    run()