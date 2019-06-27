import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler
import ssl
import socket

webdir = '.'
port = 9090

if len(sys.argv) > 1:
    webdir = sys.argv[1]
if len(sys.argv) > 2:
    port = int(sys.argv[2])
print('webdir \'%s\', port %s' % (webdir, port))

os.chdir(webdir)

srvaddr = ('', port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.socket = ssl.wrap_socket(srvobj.socket, certfile=os.getcwd()+'\\server.crt', keyfile=os.getcwd()+'\\server.key')
srvobj.serve_forever()
