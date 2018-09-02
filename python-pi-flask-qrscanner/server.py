from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('scan_qr'))

@app.route('/scan/')
def scan_qr():
    return render_template("scan-qr.html")

@app.route('/generate/', defaults={'qr_code': 'GB2RCM'})
@app.route('/generate/<qr_code>')
def generate_qr(qr_code):
    return render_template("generate-qr.html", qr_code=qr_code)

''' ToDo 
    Add Page functionality and SQLite3 database

@app.route('/page/', defaults={'page_uuid': 'GB2RCM'})
@app.route('/page/<page_uuid>')
def show_page(page_uuid):
    return render_template("page.html", page_uuid=page_uuid)
'''

# HTTPS is required for instascan.min.js
# Temporary fix, need to click advanced on Chrome to proceed with page
# Consider nginx reverse proxy
# https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0", ssl_context="adhoc")