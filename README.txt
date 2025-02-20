                                            ////////////ESPAÑOL/////////////

Pasos para ejecutar la Enciclopedia online en tu ordenador:

Configuración Paso a Paso
1. Descarga los archivos en tú ordenador y guardalos en una carpeta.

2. Abre la terminal de sistema y abre la carpeta usando cd y copiando la ruta a la carpeta. Ejemplo:

cd C:\Users\Desktop\enciclopedia_online

3. Ejecuta el script initialize_db.py para crear la base de datos SQLite y agregar datos de ejemplo:

python initialize_db.py
Esto generará el archivo encyclopedia.db en la misma carpeta.

4. Inicia el Servidor HTTP

Ejecuta el servidor backend:

python backend.py
El servidor estará disponible en http://localhost:8000. (o el puerto que tengas configurado)

5. Carga el Frontend en el Navegador

Abre un navegador web y accede a http://localhost:8000/index.html. (cambia el número por el puerto que tengas abierto) Este archivo será servido automáticamente por el backend.

Conexión API + Frontend

El frontend hará solicitudes a la ruta /entries_by_letter proporcionada por el servidor (backend.py) para obtener las palabras y mostrarlas dinámicamente.

                                            ////////////ENGLISH/////////////

Steps to Run the Online Encyclopedia on Your Computer

Step-by-Step Setup

1️. Download the Files
Download the project files to your computer and save them in a folder.

2️. Open the System Terminal
Open the terminal and navigate to the folder using cd and the folder path. Example:

cd C:\Users\Desktop\enciclopedia_online

3️. Run the Database Initialization Script
Execute the initialize_db.py script to create the SQLite database and add sample data:

python initialize_db.py
This will generate the encyclopedia.db file in the same folder.

4️. Start the HTTP Server
Run the backend server:

python backend.py
The server will be available at http://localhost:8000 (or the port you have configured).

5️. Load the Frontend in the Browser

Open a web browser and go to http://localhost:8000/index.html (change the port number if needed). This file will be served automatically by the backend.

API + Frontend Connection
The frontend will send requests to the /entries_by_letter route provided by the server (backend.py) to fetch and display words dynamically.