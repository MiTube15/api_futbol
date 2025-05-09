from flask import Flask, jsonify # type: ignore
from scrapping import obtener_partidos

app = Flask(__name__)

@app.route('/api/partidos', methods=['GET'])
def api_partidos():
    datos = obtener_partidos()
    return jsonify(datos)

if __name__ == '__main__':
    if not os.phat.exists(app.confing['UPLOAD_FOLDER']):
        os.makedirs(app.confing['UPLOAD_FOLDER'])
    app.run(debug=True, host='0.0.0.0', port=5000)
