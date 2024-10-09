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


def start_serveur():

    adresse_serveur = ("localhost", 8000)
    mon_serveur = HTTPServer(adresse_serveur, GestionRequete)

    print("Serveur démarré sur le port 8000...")

    mon_serveur.serve_forever()


start_serveur()
