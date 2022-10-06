from flask import Flask, render_template
import requests

app = Flask(__name__) # Crea la aplicación Flask.

@app.route('/')
def index():
    respuesta = requests.get("https://rickandmortyapi.com/api/character").json()
    personajes = respuesta["results"]
    return render_template("index.html", personajes=personajes)
    
if __name__ == "__main__":
    app.run() # Ejecuta la aplicación Flask facilmente desde la terminal.