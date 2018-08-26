import nxppy
import ndef
import time

# Instantiate reader
mifare = nxppy.Mifare()

Scanned = False
# Print card UIDs as they are detected

def scan_card():
	while not Scanned == True:
		print("Scanning")
		try:
			# Select tag
			uid = mifare.select()
			
			if uid is not None:
				
				print("Scanned")
				print(uid)			
		
				try:
					# Read NDEF data
					ndef_data = mifare.read_ndef()
					print(ndef_data)

					# Parse NDEF data
					ndef_records = list(ndef.message_decoder(ndef_data))	
					print(ndef_records[0])

				except:
					print("Cannot read ndef_data")	
				
				Scanned == True
				
				
		except nxppy.SelectError:
			# SelectError is raised if no card is in the field.
			pass
	
		time.sleep(1)
		
	
scan_card()