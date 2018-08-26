# https://realpython.com/python-web-applications-with-flask-part-i/
from flask import Flask
import flask_read_data

app = Flask(__name__)

@app.route("/")
def hello():

	return "Hello World"

@app.route("/card")
def card():
	response = flask_read_data.scan_card()
		
	return response

@app.route("/page/<page_name>")
def page(page_name):
		
	return page_name

	
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)