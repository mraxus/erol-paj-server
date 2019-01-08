#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get('PORT', '5500'))
FILE_PATH = os.environ.get('JSON_PATH', '/home/pi/data.json')


def read_file(path):
    fil = open(path)
    text = fil.read()
    fil.close()
    return text


class RestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data = read_file(FILE_PATH)
        print "  Response: '%s'" % data
        self.wfile.write(data)
        return


try:
    # Create web server with custom handler to manage the incoming request
    server = HTTPServer(('', PORT), RestHandler)
    print 'Started http-server on port ', PORT

    # Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
