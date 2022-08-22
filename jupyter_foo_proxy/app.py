from flask import Flask
import sys
import requests

port = int(sys.argv[1])
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test')
def hello_world_test():
    response = requests.get('https://www.google.com')
    return response.content


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
