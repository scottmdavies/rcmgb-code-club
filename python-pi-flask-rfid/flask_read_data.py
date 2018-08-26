import nxppy
import ndef
import time

# Instantiate reader
mifare = nxppy.Mifare()

def scan_card():
		try:
			# Select tag
			uid = mifare.select()
			
			if uid is not None:
				
				# Print card UIDs as they are detected

				try:
					# Read NDEF data
					ndef_data = mifare.read_ndef()
					

					# Parse NDEF data
					ndef_records = list(ndef.message_decoder(ndef_data))	
					
					record = ndef_records[0]
					
					#card = (uid, record)
					
					return record.text
					
				except:
					return "cannot read ndef_data"	
			
				
		except nxppy.SelectError:
			# SelectError is raised if no card is in the field.
			return "card not found"
			
