import nxppy
import ndef

def scan_card():
	# Instantiate reader
	mifare = nxppy.Mifare()

	try:
		# Select tag
		uid = mifare.select()
				
		# Print card UIDs as they are detected

		try:
			# Read NDEF data
			ndef_data = mifare.read_ndef()
			
			# Parse NDEF data
			ndef_records = list(ndef.message_decoder(ndef_data))	
			
			record = ndef_records[0]
					
			return {"uid":uid, "text":record.text, "status":"success"}
			
		except:
			
			return {"text": "cannot read ndef_data", "status":"error"}	
		
			
	except nxppy.SelectError:
		# SelectError is raised if no card is in the field.
		return {"text": "card not found", "status":"error"}