from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from my portfolio web app!"


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.1')