import http.server
import socketserver

class manejador(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
       if self.path =='/saludo':
           self.path='saludo.html'
       return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
   # def do_POST(self):
        

PORT = 8000
handler = manejador
myserver = socketserver.TCPServer(("",PORT), handler)
print(f"server start on port: {PORT}")
myserver.serve_forever()
