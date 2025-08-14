from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    return "<p>Hello!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)
