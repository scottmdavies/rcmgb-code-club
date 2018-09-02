from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/scan/')
def scan_qr():
    return render_template("scan-qr.html")

@app.route('/generate/')
def generate_qr():
    return render_template("generate-qr.html")

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")