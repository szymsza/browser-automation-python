from http.server import HTTPServer, BaseHTTPRequestHandler

hostname = '127.0.0.1'
port = 3000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        # TODO - return the same result as with Node
        self.wfile.write(b'Hello, World!')

print(f"Starting server at http://{hostname}:{port}/")
httpd = HTTPServer((hostname, port), SimpleHTTPRequestHandler)
httpd.serve_forever()