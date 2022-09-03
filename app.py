from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import TCPServer
from threading import Thread
import time


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes('{"status": "OK"}', "utf-8"))


def server(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


def shark():
    while True:
        print("ASDASDASDA")
        time.sleep(5)

def main():
    thread = Thread(target=shark)
    thread.start()
    server()
    thread.join()


main()