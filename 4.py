from flask import Flask, jsonify, request

"""
Este script crea una aplicación web simple con Flask que tiene dos endpoints de API.
Endpoints:
- GET /api/data: Devuelve un objeto JSON con atributos predefinidos.
- POST /api/data: Acepta un objeto JSON en el cuerpo de la solicitud y lo devuelve en la respuesta.
Módulos:
- flask: Un micro framework web para Python.
Uso:
Ejecuta este script para iniciar el servidor web Flask. El servidor será accesible en http://127.0.0.1:5000/.
Ejemplo:
1. Para obtener datos:
    Envía una solicitud GET a http://127.0.0.1:5000/api/data.
    Respuesta:
    {
         "atributo1": "valor1",
         "atributo2": "valor2"
    }
2. Para enviar datos:
    Envía una solicitud POST a http://127.0.0.1:5000/api/data con un cuerpo JSON.
    Ejemplo de cuerpo de solicitud:
    {
         "clave": "valor"
    }
    Respuesta:
    {
         "received": {
              "clave": "valor"
         }
    }
"""

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'atributo1': 'valor1',
        'atributo2': 'valor2'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
    @app.route('/api/data', methods=['POST'])
    def post_data():
        data = request.get_json()
        response = {
            'received': data
        }
        return jsonify(response)