import sqlite3
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer

DATABASE = 'encyclopedia.db'

class EncyclopediaHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/entries_by_letter":
            self.handle_entries_by_letter()
        else:
            super().do_GET()  # Servir archivos estáticos normalmente

    def handle_entries_by_letter(self):
        # Conectar a la base de datos
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Consultar las palabras agrupadas por letra inicial
        cursor.execute("SELECT word, definition FROM entries")
        rows = cursor.fetchall()

        grouped_entries = {}
        for word, definition in rows:
            first_letter = word[0].upper()
            if first_letter not in grouped_entries:
                grouped_entries[first_letter] = []
            grouped_entries[first_letter].append({"word": word, "definition": definition})

        # Responder con los datos en formato JSON
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(grouped_entries).encode())

        conn.close()

def run(server_class=HTTPServer, handler_class=EncyclopediaHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor iniciado en el puerto {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()