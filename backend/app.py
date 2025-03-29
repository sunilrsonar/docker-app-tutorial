from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/process', methods=['POST'])
def process_data():
    data = request.get_json()   
    response = {
        'data': data
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)