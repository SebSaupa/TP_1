from flask import Flask, render_template, request
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  port=3307,
  user="root",
  password="root",
  database="TP1"
)

cursor = db.cursor()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("formCitats.html")

@app.route("/register")
def register():
    aut  = request.args.get('auteur', None)
    cit  = request.args.get('citation', None)

    reference = (aut, cit)
    cursor.execute("INSERT INTO citations (auteur, citation) VALUES(%s, %s)", reference)
    db.commit()

    return render_template("affichage.html", auteur=aut, citation=cit)

app.run(host="0.0.0.0", port=4000)
db.close()