from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime
import argparse


parser = argparse.ArgumentParser(description="Simple web app",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--host", default="0.0.0.0")
parser.add_argument("--port", type=int, default=8080)
args = parser.parse_args()
config = vars(args)

hostName = config.get('host')
serverPort = config.get('port')


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path == "/":
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>This is root page.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        elif self.path == "/hello":
            self.wfile.write(bytes("hello world!", "utf-8"))
        elif self.path == "/date":
            self.wfile.write(bytes("Current Date: " + str(datetime.datetime.now().isoformat()), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
