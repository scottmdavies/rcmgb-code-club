
# QR Scanner

## Summary

Use mobile phone or tablet to scan QR code
QR Code could be printed on business card or on an e-ink display
Mobile phone or tablet connect to Wifi
Navigate to museum server
Server generates QR Code for database items
Server hosts JS for QR Scanner and handles routing of QR data to fetch database items
Note HTTPS required for accessing Camera through Chrome

## Technologies:

+ HTML5 based app
+ Javascript packages for QR Code Scanning and Generation
+ Pyton Flask Server for routing
+ 

## Installation

```bash
git clone <repo>

virtualenv venv
pip install -r requirements.txt
source venv/bin activate
python server.py

```

## Complete Setup Guide

Checking npm is installed and up to date
```bash
node -v

npm -v

npm install npm@latest -g

```
https://www.npmjs.com/get-npm

Building dependencies and packages.json file


```bash
mkdir ./static/js

```

``` bash
npm install -save qrious
cp ./node_modules/qrious/dist/qrious.min.js ./static/js
cd ./static/js

curl -L https://github.com/schmich/instascan/releases/download/1.0.0/instascan.min.js --output instascan.min.js
```
Note curl -L allows redirect


```bash
cd ..
mkdir templates
cd templates/
touch scan-qr.html
touch generate-qr.html

```

