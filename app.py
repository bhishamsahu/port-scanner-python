from flask import Flask, render_template, request
from scanner import scan_ports

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    ports = []
    target = ""

    if request.method == "POST":
        target = request.form["target"]
        ports = scan_ports(target)

    return render_template("index.html", ports=ports, target=target)

app.run(debug=True)

