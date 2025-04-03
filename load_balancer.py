# load_balancer.py
from flask import Flask, request
import itertools
import requests

app = Flask(__name__)

# Lista de servidores backend para distribución round-robin
BACKEND_SERVERS = [
    "http://flask-backend-service:5001"  # Nombre único del servicio backend en Kubernetes
]

# Iterador round-robin para distribuir las solicitudes
server_pool = itertools.cycle(BACKEND_SERVERS)

@app.route('/')
def load_balance():
    backend_url = next(server_pool)
    user_id = request.args.get("user_id", "Guest")
    response = requests.get(f"{backend_url}/", params={"user_id": user_id})
    return response.text

if __name__ == '__main__':
    # Se puede cambiar el puerto si es necesario (por defecto es 8080)
    app.run(host='0.0.0.0', port=8080)
