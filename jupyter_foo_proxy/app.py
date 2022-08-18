from flask import Flask
import sys


port = int(sys.argv[1])
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test')
def hello_world_test():
    return 'Hello, World! test'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
