#!venv/bin python
# -*- coding: utf-8 -*-

""" 
Using nxppy to interface with NXP Explore NFC Card and return NFC Card UID and NDEF data. 
"""

import nxppy
import ndef
import time

def scan_card():

	"""Return the uid and NDEF card as a response for jsonify and Flask API."""

	# Instantiate reader
	mifare = nxppy.Mifare()
	
	try:
		# Select tag
		uid = mifare.select()
	
		# Print card UIDs as they are detected

		if len(uid) == 8:
			
			try:
				# mifare classic not implemented in nxppy
				# can detect uid
				# requirement to authenticate for read / write access
				return {"uid":uid, "text":"", "status":"success"}


			except nxppy.ReadError:
				return {"error": "cannot read data"}

		if len(uid) == 14:
			try:
				# Read NDEF data
				ndef_data = mifare.read_ndef()
				
				# print(ndef_data)
				
				# Parse NDEF data
				ndef_records = list(ndef.message_decoder(ndef_data))	
				
				record = ndef_records[0]
						
				return {"uid":uid, "text":record.text, "status":"success"}
				
			except nxppy.ReadError:
				return {"error": "cannot read ndef_data"}	
		
			
	except nxppy.SelectError:
		# SelectError is raised if no card is in the field.
		return {"error": "card not found"}

if __name__ == "__main__":
	# run card scanning loop when run as file not a module
	while True:
		response = scan_card()
		print(response)
		time.sleep(5)