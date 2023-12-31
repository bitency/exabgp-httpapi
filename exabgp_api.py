import cgi
from http.server import SimpleHTTPRequestHandler, HTTPServer
from sys import stdout

PORT = 5001

class ServerHandler(SimpleHTTPRequestHandler):

    def createResponse(self, command):
        """ Send command string back as confirmation """
        self.send_response(200)
        self.send_header('Content-Type', 'application/text')
        self.end_headers()
        
        # Encode the string to bytes before writing
        response_bytes = command.encode('utf-8')
        self.wfile.write(response_bytes)

    def do_POST(self):
        """ Process command from POST and output to STDOUT """
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST'})
        
        command = form.getvalue('command')
        stdout.write('%s\n' % command)
        stdout.flush()
        self.createResponse('Success: %s' % command)

if __name__ == "__main__":
    handler = ServerHandler
    httpd = HTTPServer(('', PORT), handler)
    stdout.write('serving at port %s\n' % PORT)
    stdout.flush()
    httpd.serve_forever()
