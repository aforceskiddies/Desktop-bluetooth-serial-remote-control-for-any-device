#!/usr/bin/env python3
import http.server, webbrowser, os, threading

PORT = 8080
DIR  = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DIR, **kw)
    def log_message(self, *_): pass  # silent

def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")

print(f"LadyBug Remote → http://localhost:{PORT}")
print("Press Ctrl+C to stop.")
threading.Timer(0.5, open_browser).start()
http.server.HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
