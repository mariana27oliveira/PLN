from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "<p>Hello, World!</p>" #fazer o html no mesmo ficheiro


@app.route("/homepage")

def home():
    return render_template ("home.html", title="DICIONÁRIO MÉDICO")



@app.route("/creditos")

def creditos():
    return render_template("creditos.html")

app.run(host="localhost", port=3000, debug=True)
#o debug permite-me fazer alterações e a página atualizar automaticamente, sem ter de correr novamente
