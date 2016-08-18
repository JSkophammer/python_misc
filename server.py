import http.server
import os
import sys

server_dir = sys.argv[1]
os.chdir(server_dir)


def start_server(port=8000, bind="", cgi=False):
    if cgi:
        http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler, port=port, bind=bind)
    else:
        http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=port, bind=bind)


start_server()
