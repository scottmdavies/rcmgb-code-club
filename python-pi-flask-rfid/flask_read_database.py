#!venv/bin python
# -*- coding: utf-8 -*-

""" 
Using SQLite3 database to store radio equipment information. Returns json for Flask API. 
"""

import sqlite3

db = "test.db"

def get_page(page_id):

	conn = sqlite3.Connection(db)
	# https://docs.python.org/2/library/sqlite3.html#row-objects
	# Provide access to columns as keys
	conn.row_factory = sqlite3.Row
	c = conn.cursor()
	# Needs to be a tuple	
	page_id = (page_id,)
	
	c.execute('SELECT * FROM radios WHERE id = ?', page_id)
	row = c.fetchone()
	if row is not None:
		response = {
			"id" : row["ID"],
			"title" : row["TITLE"],
			"description" : row["DESCRIPTION"],
			"image_url" : "/img/" + row["IMAGEURL"]
		}	
	else:
		response = {
			"error" : "page not found"
		}


	return response
	conn.close()

if __name__ == "__main__":
	# query database when run as file not a module
	while True:
		page_id = input("Enter Page_id: ")
		response = get_page(page_id)
		print(response)