import http.server
import socketserver

PORT = 5000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at 127.0.0.1:" + str(PORT))
    httpd.serve_forever()
