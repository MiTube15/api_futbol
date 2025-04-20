from flask import Flask, jsonify # type: ignore
from scrapping import obtener_partidos

app = Flask(__name__)

@app.route('/api/partidos', methods=['GET'])
def api_partidos():
    datos = obtener_partidos()
    return jsonify(datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
