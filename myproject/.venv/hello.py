from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f"<p>Hello,  World!</p>"

@app.route('/hello/<name>')
def hello_name(name):
    return f"<p>Hello, {name}  World!</p>"

if __name__ == '__main__':
    app.run(debug=True)