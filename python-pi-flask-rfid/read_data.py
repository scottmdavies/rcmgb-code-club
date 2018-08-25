import nxppy
import ndef
import time

# Instantiate reader
mifare = nxppy.Mifare()

# Print card UIDs as they are detected
while True:
	try:
		# Select tag
		uid = mifare.select()
		if uid is not None:
			print(uid)
			# Read NDEF data
			ndef_data = mifare.read_ndef()
			
			print(ndef_data)
			# Need to review MemoryError
			# https://airbrake.io/blog/python-exception-handling/memoryerror

			# Parse NDEF data
			#ndef_records = list(ndef.message_decoder(ndef_data))
			
			#print(ndef_records[0])			
			uid is None
			
	except nxppy.SelectError:
		# SelectError is raised if no card is in the field.
		pass

	time.sleep(1)




