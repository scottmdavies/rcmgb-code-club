import nxppy
import ndef
import time

import os
import psutil
import logging

PROCESS = psutil.Process(os.getpid())
MEGA = 10 ** 6

# Instantiate reader
mifare = nxppy.Mifare()

def print_memory_usage():
    """Prints current memory usage stats.
    See: https://stackoverflow.com/a/15495136

    :return: None
    """
    # option for function returning more items[2:4] slice, or *var_name
    total, available, percent, used, free, *others = psutil.virtual_memory()
    total, available, used, free = total / MEGA, available / MEGA, used / MEGA, free / MEGA
    proc = PROCESS.memory_info()[1] / MEGA
    print('process = %s total = %s available = %s used = %s free = %s percent = %s'
          % (proc, total, available, used, free, percent))

logname = "./nfc.log"

logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

attempts = 1
# Print card UIDs as they are detected
while True:

	try:
		# Select tag
		uid = mifare.select()
		print_memory_usage()

		if uid is not None:
			logging.info(attempts)
			logging.info(uid)
			print(uid)
			# Read NDEF data
			ndef_data = mifare.read_ndef()
			logging.info(ndef_data)
			print(ndef_data)
			# Need to review MemoryError
			# https://airbrake.io/blog/python-exception-handling/memoryerror

			# Parse NDEF data
			#ndef_records = list(ndef.message_decoder(ndef_data))
			
			#print(ndef_records[0])			
			uid is None
			del ndef_data
			logging.info("del ndef_data")
			attempts += 1

			
	except nxppy.SelectError:
		# SelectError is raised if no card is in the field.
		pass
	
	sleep_duration = 5
	time.sleep(sleep_duration)
	logging.info(sleep_duration)



