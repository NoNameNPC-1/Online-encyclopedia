import sqlite3

DATABASE = 'encyclopedia.db'

def initialize_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Crear tabla de entradas
    #cursor.execute('''
    #    CREATE TABLE IF NOT EXISTS entries (
    #        id INTEGER PRIMARY KEY AUTOINCREMENT,
    #        word TEXT NOT NULL,
    #        definition TEXT NOT NULL
    #    )
    #''')

    # Insertar datos de ejemplo
    #cursor.executemany('''
    #    INSERT INTO entries (word, definition) VALUES (?, ?)
    #''', [
    #    ("Amor", "Sentimiento de cariño."),
    #    ("Arte", "Expresión creativa."),
    #    ("Bala", "Proyectil disparado por un arma."),
    #    ("Bravo", "Valiente o animado."),
    #])

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
