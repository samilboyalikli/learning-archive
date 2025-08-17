# ---------------- Flask Application ----------------

from flask import Flask, request

app = Flask(__name__)

# flask --app listener run

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello():
    return "<p>Hello!</p>"


@app.route("/triggerpoint", methods=["POST"])
def triggerpoint():
    if request.method == "POST":
        return f"<p>File is triggered.</p>", 200
    else:
        return "<p>File did not trigger.</p>", 400


# ---------------- HTTP Application ----------------

from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<p>Hello, World!</p>")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"<p>Not Found</p>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)
