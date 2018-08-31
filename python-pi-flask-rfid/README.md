# Great British Radio Commnunication Museum - Visitor Information System [Prototype]

Using Radio Communication technology to provide information on Radio Communication technology with a RaspberryPi and Near Field Communication (NFC) Tags

## Project Objectives

+ The Great British Radio Communication Museum features a wide range of radio devices
+ This project aims to allow museum visitors to find more information about each of these devices as they walk around the museum exhibits
+ Provide a longer-term project for the volunteers and kids attending the Code Clubs at the Museum 
+ The option considered here would be to use Near Field Communication (NFC) tags on each device, allowing the visitors to scan the device in front of them and be presented with information either on a screen or handheld device

## Near Field Communication

"NFC devices are used in contactless payment systems, similar to those used in credit cards and electronic ticket smartcards and allow mobile payment to replace/supplement these systems." 

"NFC employs electromagnetic induction between two loop antennas when NFC-enabled devices—for example a smartphone and a printer—exchange information, operating within the globally available unlicensed radio frequency ISM band of 13.56 MHz on ISO/IEC 18000-3 air interface at rates ranging from 106 to 424 kbit/s." 

"NFC always involves an initiator and a target; the initiator actively generates an RF field that can power a passive target. This enables NFC targets to take very simple form factors such as unpowered tags, stickers, key fobs, or cards. NFC peer-to-peer communication is possible, provided both devices are powered."

Source: https://en.wikipedia.org/wiki/Near_field_communication

In the museum the NFC Tags may have to adhere to a variety of surface including:
+ Plastic
+ Metal
+ Glass


## Initial Prototype

The initial prototype has been built using the following hardware:

+ RaspberryPi 3 B+
+ NXP Explore-NFC-WW PN512

and the following software:

+ **Backend**
	+ Python - platform for system backend
	+ Flask - Python webserver used to built API, serve 
	+ nxppy - NXP NFC Explore card wrapper
	+ ndeflib - library for managing NDEF records stored on NFC Tags (NTAGs)
	+ SQLite3 - local database storage

+ **Frontend**
	+ Javascript - consume Flask API

# Installation


Setup the Serial Interface for the NXP Explore Card: 

```bash
sudo raspi-config

Select [Enter] Option 5 Inferacing Options
Select [Enter] P4 SPI
Enable the SPI Interface <Yes> [Enter]
<OK> [Enter]
<Finish> [Enter]

sudo shutdown now
```

Attach the NXP Explore Card to the RaspberryPi GPIO Header pins.

Power-up the RaspberryPi.

On the RaspberryPi navigate to a new folder and open a Terminal window.

_Note: Pressing F4 will open a Terminal in the current working directory_

Clone the repo:

```bash

git clone https://github.com/scottmdavies/rcmgb-code-club/tree/master/python-pi-flask-rfid

```

[Optional] Install python-virtualenv, if not installed:

```bash

sudo apt-get install python-virtualenv

```

Setup a virtual-env for Python:

```bash

virtualenv --python=python3 venv

source venv/bin/activate

pip3 install -r requirements.txt

```

# Checking

Check the NXP Card Reader detects cards:

```bash

python3 flask_read_card.py

```

Check the SQLite3 database returns pages:

```bash

python3 flask_read_database.py

```

# Updating the database

[Optional] Install the SQLite3 package:

```bash

sudo apt-get install sqlite3

```

Open in the SQLite3 in a Terminal:

```bash

sqlite3

```
Modify the SQLite3 database:

```sql

.open test.db

.tables 

.schema

SELECT * FROM radios;

SELECT * FROM radios WHERE ID=1;

UPDATE radios SET IMAGEURL = 'nokia-3310.png' WHERE ID = 1;

```

# Running

Start the Flask webserver:

```bash

python3 server.py


```

Evaluate the API, right-click links below and open in new Tab:

+ Open the Developer Inspector in Chromium ``` Ctrl+Shift+I ``` to review Javascript Console
+ Main page: http://127.0.0.1:5000/
+ Scan card: http://127.0.0.1:5000/scan-card
+ Pages: http://127.0.0.1:5000/page/1



## To Do

+ Update HTML Layout
+ Use Bootstrap for formatting HTML elements
+ Test RC522 Sets using [MFRC522-python](https://github.com/mxgxw/MFRC522-python)
+ Evaluate Cordova / PhoneGap native app (using HTML, JS and CSS) for visitors to use phone / tablet accessing radio communication equipment database

## Notes

### Mifare Classic Tags

UID detected for item. Authetnication required to access specific blocks. 

https://www.nxp.com/docs/en/application-note/AN1304.pdf , See Page 7 for data structure

### Resources

https://www.tutorialspoint.com/sqlite/