#!/usr/bin/python
from http.server import BaseHTTPRequestHandler,HTTPServer
import urllib.request

PORT_NUMBER = 8080
from urllib.parse import urlparse

class myHandler(BaseHTTPRequestHandler):
#Handler for the GET requests
    def do_GET(self):
        query = urlparse(self.path)
        query = query.geturl()
        print(query)
        query_components = query.split("/url=")
        url = query_components[1]
        request_url = urllib.request.urlopen(url)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(request_url.read())
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print ('HTTP server running on port ' , PORT_NUMBER)
    #Wait forever for incoming http requests
    server.serve_forever()
except KeyboardInterrupt:
    print ('^C received, shutting down')
    server.socket.close()
