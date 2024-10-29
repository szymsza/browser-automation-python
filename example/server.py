from http.server import HTTPServer, BaseHTTPRequestHandler

hostname = '127.0.0.1'
port = 3000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if (self.path == '/redirected'):
            print('Link clicked!')

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(f'<a href="http://{hostname}:{port}/redirected" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background-color: red;">CLICK</a>'.encode())

    # Ignore request logs
    def log_request(self, code):
        pass

print(f"Starting server at http://{hostname}:{port}/")
httpd = HTTPServer((hostname, port), SimpleHTTPRequestHandler)
httpd.serve_forever()