# backend.py
from flask import Flask, request
import socket
import uuid

app = Flask(__name__)

@app.route('/')
def hello_user():
    user_id = request.args.get("user_id", "Guest")
    instance = socket.gethostname()
    unique_id = str(uuid.uuid4())  # Genera un identificador único
    
    return f"Hello, {user_id}! This response is from instance: {instance} (ID: {unique_id})"

if __name__ == '__main__':
    # Se puede cambiar el puerto si es necesario (por defecto es 5001)
    app.run(host='0.0.0.0', port=5001)
