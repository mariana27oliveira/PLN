import json
from flask import Flask, render_template

app = Flask(__name__)

file = open ("terms.json", encoding="utf-8")

db = json.load(file)


@app.route("/")

def home():
    return render_template ("home.html", title="WELCOME!!")


@app.route("/terms")

def terms():
    return render_template("terms.html", designations=db.keys())


@app.route("/term/<t>")

def term(t):
    return render_template("term.html", designation = t, value=db.get(t, "None"))

app.run(host="localhost", port=3000, debug=True)
#o debug permite-me fazer alterações e a página atualizar automaticamente, sem ter de correr novamente
