from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate-zakat', methods=['POST'])
def calculate_zakat():
    data = request.get_json()
    wealth = data.get('wealth', 0)
    nisab = 612.36 * 0.8  # Silver price as an example
    zakat = 0

    if wealth >= nisab:
        zakat = wealth * 0.025

    return jsonify({ 'zakat': round(zakat, 2) })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
