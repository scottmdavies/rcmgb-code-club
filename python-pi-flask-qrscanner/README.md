
# QR Scanner Prototype

## Summary

+ Use mobile phone or tablet to scan QR code
+ QR Code could be printed on business card or on an e-ink display
+ Mobile phone or tablet with camera connects to museum Wifi
+ Redirect to RaspberryPi server, alternatively turn RPi into a hotspot
+ Server hosts JS for QR Scanner and handles routing of QR data to fetch database items
+ Server can also generate QR Codes for expnading the database

Note accessing the camera requires HTTPS in Chrome/Chromium, however localhost is considered safe:
https://sites.google.com/a/chromium.org/dev/Home/chromium-security/deprecating-powerful-features-on-insecure-origins

## Technologies:

**Front End**
+ HTML5 / CSS / JS
+ Javascript packages for QR Code Scanning and Generation:
    + Instascan
    + QRious


**Backend**
+ Pyton Flask Server for routing
+ SQLite3

## Installation

```bash
git clone <this repo>
virtualenv venv --python=python3
pip install -r requirements.txt
source venv/bin activate
python3 server.py

```

## Complete Build Guide

Using two Javascript packages to provide the QR Code functionality. Both are available in ```npm ```.

+ instascan contained src but no build files unless cloning repo directly

+ QRious contained dist folder allowing "../node_modues/qrious/dist/<file>.js"

Checking npm is installed and up to date
```bash
# https://www.npmjs.com/get-npm

node -v

npm -v

npm install npm@latest -g

```


Created ```/static``` folder for storing JS and CSS to be served by ```Flask```:
```bash
mkdir ./static/js

```

Used ``` npm ``` for qrious.js and ``` curl ``` for compiled instascan.min.js files

``` bash
npm install -save qrious
# copy from node_modules into static/js folder
cp ./node_modules/qrious/dist/qrious.min.js ./static/js
cd ./static/js

# Note curl -L swtich to allow redirect
curl -L https://github.com/schmich/instascan/releases/download/1.0.0/instascan.min.js \ 
--output instascan.min.js
```

Created ```/template``` folder for storing ```html``` files to be served by ```Flask```:

```bash
cd ..
mkdir templates
cd templates/
touch scan-qr.html
touch generate-qr.html

```

Used examples from ```README.md``` for each JS package ```repo``` page to start ```scan-qr.html``` and ```generate-qr.html``` based on ```README.md``` examples from each 

Added simple formatting and additional functions to return data generated and checked using ```console.log(variable)``` to return variables to the console in Chrome/Chromium for debugging

```html

function showQRcode(content) {
    document.getElementById('scannedQRcode').innerHTML=content;
}
```

Modified file path of static files,
```html
<link rel="stylesheet" href="../static/css/qr-scanner.css">
``` 
In future this can be changed in ```Flask``` to ```url_for('static','css/qr-scanner.css')

Often useful in Chrome/Chromium to ```Disable Cache``` in ```Developer tools``` when modifying CSS / JS to see changes.


Modified ```server.py``` to generate URL routes for the two functions ```/generate``` and ```/scan``` , which return ```HTML``` pages in the ```/templates``` folder with the respective ```Javascript``` QR Code functions

```python
@app.route('/generate/', defaults={'qr_code': 'GB2RCM'})
@app.route('/generate/<qr_code>')
def generate_qr(qr_code):
    return render_template("generate-qr.html", qr_code=qr_code)
```

Check out the code to learn more.

## Todo

+ Update ```HTML``` UI with ```bootstrap```
+ Add ```SQLite3``` database and return specific pages
+ Fix schema for QR Code generate ```/generate/<uuid>``` fetches page with ```<uuid>``` from database
+ Testing