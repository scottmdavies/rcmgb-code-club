#!/usr/bin/env python

"""close_encounter.py: Plays sequence of notes and lights LEDs."""

import time
import psonic
import blinkt

# defines Blinkt RGB values for range of colours in sequence
white = (255, 255, 255)
orange = (255, 127, 0)
pink = (255, 182, 193)
purple = (128, 0, 128)
yellow = (255, 255, 0) 

# delay in seconds for LED and playing sound, controls overall loop
delays = [0.5, 0.25, 0.2, 0.15, 0.1]

# list of colours
colours = [pink,orange,purple,yellow,white]

# turns on the Blinkt LEDs with relevant colour

def show_led(led_num, led_colour, delay):
	r,g,b = led_colour
	blinkt.clear()
	blinkt.set_brightness(0.1)
	blinkt.set_pixel(led_num, r,g,b)
	blinkt.show()
	time.sleep(d)

# order of synth notes being played in the sequence
notes = [psonic.G4,psonic.A4,psonic.F4,psonic.F3,psonic.C4]

# limited by the 8 pixels so mapping synth notes to index
# FXCDEFGA
# 01234567

order = [6,7,5,0,2]

# overall loop
for d in delays:
	# iterate through notes in synth sequence
	for i, note in enumerate(notes):
		psonic.use_synth(psonic.SAW)
		psonic.play(note)
		psonic.sleep(d)
		show_led(led_num=order[i],led_colour=colours[i],delay=d)

