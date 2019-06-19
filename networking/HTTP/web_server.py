import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

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
srvobj.serve_forever()