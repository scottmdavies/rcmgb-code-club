# Close Encounter

Python script for a RaspberryPi that controls Pimorni Blinkt! LEDs and synth keys in SonicPi 

# Background

## Famous Keyboard Sound and Light Sequence

```
 Start with the tone. (Pinkish-red) - G, 67
 Up a full tone. (Orange) - A, 69
 Down a major third. (Purple) - F, 65
 Now drop an octave. (Yellow) - F (an octave lower), 53
 Up a perfect fifth. (White) - C, 60
```
http://www.johnloomis.org/ece303L/notes/music/Close_Encounters.html

Information used to determine Blinkt! LED colours and SonicPi synth keys

## Python-Sonic

Send signals to open SonicPi via OSC messages

https://github.com/gkvoelkl/python-sonic 


# Required

+ RaspberryPi with SonicPi
+ Pimoroni Blinkt!

# Python Project Setup

```bash
sudo apt-get install python-virtualenv

virtualenv --python=python3 venv

source venv/bin/activate
```

# Install Python dependencies

```bash

pip install -r requirements.txt


```

# Open SonicPi

In SonicPi Preferences:
+ Tick Enable OSC server
+ Tick Receive remote OSC messages

# Check RaspberryPi Sound

+ Click Volume icon in task bar and check the Audio output: Analog (3.5mm Headphone jack) or HDMI
+ Adjust volume

# Run script

```bash

python3 close_encounter.py

```

# Optional

Make a mountain out of mashed potato
