from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

PORT = 8000
ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)

class CorsHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

print(f"Servidor del tablero: http://localhost:{PORT}/tablero.html")
print(f"Base de datos:        http://localhost:{PORT}")
ThreadingHTTPServer(("0.0.0.0", PORT), CorsHandler).serve_forever()
