from flask import Flask, render_template, request
import json
import re
app = Flask(__name__)

file = open("final.json", encoding="utf-8")
db = json.load(file) 
file.close()

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/main_info")
def main_info():
    return render_template("main_info.html", dic=db)


@app.route("/specific_info/<s>")
def specific(s):
    return render_template("specific_info.html", designation = s, value= db.get(s,"None"))



@app.route("/main_info/search")
def search():

    text = request.args.get("text")
    lista = []
    if text:
        for designation, definicao in db.items():
            if re.search(text,designation,flags=re.I) or re.search(text,definicao["definição"],flags=re.I): 
                lista.append((designation,definicao))
    return render_template("search.html",matched = lista)



@app.route("/specific_info/<s>", methods=["POST","DELETE"])
def addNota(s):
    if request.method == "DELETE":
        if "nota" in db[s]:
            del db[s]["nota"]
            file = open("final.json", "w")
            json.dump(db, file, ensure_ascii=False, indent=4)
            file.close()
            info_message = "Note deleted correctly!"
        else:
            info_message = "Couldn't delete!"

        return render_template("specific_info.html", designation=s, value=db.get(s, "None"))
    else:
        nota = request.form.get("nota", "")
        if s in db:
            if "nota" in db[s]:
                info_message = "Note Added correctly"
            else:
                info_message = "Note Updated correctly!"
        else:
            info_message = "erro!!"

        db[s]["nota"] = nota
        file = open("final.json", "w", encoding="utf-8")
        json.dump(db, file, ensure_ascii=False, indent=4)
        file.close()

        return render_template("specific_info.html", designation=s, value=db.get(s, "None"), message=info_message)





app.run(host="localhost", port=3000, debug=True)
