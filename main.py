from flask import Flask, jsonify

app = Flask(__name__)

from foo import Foo

@app.route('/api/hello', methods=['GET'])
def hello():
    f = Foo()
    f.bar()
    return jsonify({'message': 'Hello, this is a simple Flask API!'})

if __name__ == '__main__':
    app.run(debug=True)
