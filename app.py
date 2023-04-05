from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/teste")
def teste():
    return jsonify("Hello TESTE")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
