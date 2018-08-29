# https://realpython.com/python-web-applications-with-flask-part-i/
from flask import Flask, jsonify, render_template, send_from_directory
import flask_read_card
import flask_read_database

UPLOAD_FOLDER = './static/img/'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route("/")
def hello():

	return render_template("home.html")

@app.route("/scan-card")
def card():
	response = flask_read_card.scan_card()
	return jsonify(response)

@app.route("/page/<page_id>")
def page(page_id):
	
	response = flask_read_database.get_page(page_id)
	return jsonify(response)

@app.route('/img/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=False)

if __name__ == '__main__':
	app.debug = True
	app.run()
