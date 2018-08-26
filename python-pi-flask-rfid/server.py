# https://realpython.com/python-web-applications-with-flask-part-i/
from flask import Flask, jsonify, render_template
import flask_read_data

app = Flask(__name__)

@app.route("/")
def hello():

	return render_template("home.html")

@app.route("/scan-card")
def card():
	response = flask_read_data.scan_card()
	return jsonify(response)

@app.route("/page/<page_name>")
def page(page_name):
		
	return page_name

if __name__ == '__main__':
	app.debug = True
	app.run()
