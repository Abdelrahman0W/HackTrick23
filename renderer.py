#!/usr/bin/env python3
import os
import sys
import time
import threading
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler, test


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)


class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)


def has_changed(dir_path, interval=.5):
    last_modified = {}

    while True:
        for root, dirs, files in os.walk(dir_path):
            for f in files:
                path = os.path.join(root, f)
                last_modified[path] = os.path.getmtime(path)

        time.sleep(interval)

        for root, dirs, files in os.walk(dir_path):
            for f in files:
                path = os.path.join(root, f)

                try:
                    if os.path.getmtime(path) != last_modified[path]:
                        print(f"File Changed: {path}")

                        return True
                except Exception:
                    continue


def run_server(port):
    httpd = HTTPServer(('', port), CORSRequestHandler)
    print(
        f"Serving HTTP on localhost port 8000 (http://localhost:{port}/) ..."
    )
    webbrowser.open(f"http://localhost:{port}/hacktrick23_maze_renderer")
    httpd.serve_forever()


def hot_reload(port):
    while True:
        if has_changed(BASE_DIR):
            print("Reloading...")
            webbrowser.open(
                f"http://localhost:{port}/hacktrick23_maze_renderer"
            )


def run(reload=True):
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    server = threading.Thread(target=run_server, args=(port,))
    reopen = threading.Thread(target=hot_reload, args=(port,))
    server.start()
    if reload:
        reopen.start()


if __name__ == "__main__":
    run(False)
