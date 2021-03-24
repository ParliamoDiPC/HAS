from flask import Flask, render_template
from threading import Thread
from replit import db

app = Flask("app")

@app.route("/")
def index():
	return render_template("404.html")

@app.route("/announcement/<id>")
def announcement(id):
	try:
		message = db["message_" + id]
		send_date = db["date_" + id]
		author = db["author_" + id]

		return render_template("announcement.html", message = message, send_date = send_date, id = id, author = author)
	except:
		return render_template("404.html")

@app.route("/announcement/<id>/")
def announcement2(id):
	try:
		message = db["message_" + id]
		send_date = db["date_" + id]
		author = db["author_" + id]

		return render_template("announcement.html", message = message, send_date = send_date, author = author, id = id)
	except:
		return render_template("404.html")

@app.errorhandler(404)
def error404(error):
	return render_template("404.html")

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()