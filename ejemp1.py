

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/saludar', methods=['GET'])
def saludar():
    nombre = request.args.get('nombre', 'Mundo')
    return jsonify({'mensaje': f'Hola, {nombre}!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



    