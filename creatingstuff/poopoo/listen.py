import http.server
import socketserver
import threading
import os
import time
from urllib.parse import urlparse

PORT = 8080
SAVE_DIR = "requests"
os.makedirs(SAVE_DIR, exist_ok=True)

seen_paths = set()
lock = threading.Lock()
counter = 0

NONCE = "deadbeefdeadbeef"  # static for simplicity

class DigestSimHandler(http.server.BaseHTTPRequestHandler):
    def _save_request(self):
        global counter
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length) if content_length else b""

        with lock:
            counter += 1
            filename = f"{SAVE_DIR}/request_{counter}_{int(time.time()*1000)}.txt"
        with open(filename, "wb") as f:
            f.write(f"{self.command} {self.path} {self.request_version}\n".encode())
            for k, v in self.headers.items():
                f.write(f"{k}: {v}\n".encode())
            f.write(b"\n")
            f.write(body)

    def do_PUT(self):
        path = urlparse(self.path).path
        auth = self.headers.get("Authorization", "")

        with lock:
            first_time = path not in seen_paths

        if first_time:
            with lock:
                seen_paths.add(path)
            self.send_response(401)
            self.send_header("WWW-Authenticate", f'Digest realm="DAV-upload", nonce="{NONCE}", algorithm=MD5, qop="auth"')
            self.send_header("Content-Length", "0")
            self.end_headers()
        else:
            self._save_request()
            self.send_response(201)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"PUT accepted")

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"This is a test server")

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

if __name__ == "__main__":
    with ThreadedHTTPServer(("0.0.0.0", PORT), DigestSimHandler) as httpd:
        print(f"Listening on port {PORT}...")
        httpd.serve_forever()
