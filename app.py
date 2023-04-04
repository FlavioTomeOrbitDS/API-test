from flask import jsonify, Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return 'Server Online'



@app.route("/api/teste1", methods=['POST', 'GET'])
def teste1():
    
    return jsonify("teste1 OK!!")