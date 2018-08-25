# https://andymurkin.files.wordpress.com/2012/01/midi-int-midi-note-no-chart.jpg
# http://www.johnloomis.org/ece303L/notes/music/Close_Encounters.html

#Start with the tone. (Pinkish-red) - G, 67
#Up a full tone. (Orange) - A, 69
#Down a major third. (Purple) - F, 65
#Now drop an octave. (Yellow) - F (an octave lower), 53
#Up a perfect fifth. (White) - C, 60

# https://github.com/gkvoelkl/python-sonic 

import time
import psonic
import blinkt

# define colour RGB values
white = (255, 255, 255)
orange = (255, 127, 0)
pink = (255, 182, 193)
purple = (128, 0, 128)
yellow = (255, 255, 0) 

# delay in seconds for LED and playing sound
delays = [0.5, 0.25, 0.2, 0.15, 0.1]

# turning on the LEDs
def show_led(led_num, led_colour, delay):
	r,g,b = led_colour
	blinkt.clear()
	blinkt.set_brightness(0.1)
	blinkt.set_pixel(led_num, r,g,b)
	blinkt.show()
	time.sleep(d)

notes = [psonic.G4,psonic.A4,psonic.F4,psonic.F3,psonic.C4]
colours = [pink,orange,purple,yellow,white]

# Mapping the 8 pixels to notes
# FXCDEFGA
# 01234567
order = [6,7,5,0,2]

# loop
for d in delays:
	for i, note in enumerate(notes):
		psonic.use_synth(psonic.SAW)
		psonic.play(note)
		psonic.sleep(d)
		show_led(led_num=order[i],led_colour=colours[i],delay=d)

