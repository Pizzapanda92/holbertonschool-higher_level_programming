import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


class GestionRequete(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"ok")

        else:
            self.send_error(404, "Endpoint not found")


def run(server_class=HTTPServer, handler_class=GestionRequete, port=8000):

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serveur démarré sur le port {port}...")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
