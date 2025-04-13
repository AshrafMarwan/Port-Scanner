#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else:
	print("invalid amount of arguments")
	print("syntax: scanner.py <ip>")
	print("-" * 50)
	print("scanning target: "+target)
	print("Time started: "+str(datetime.now()))
	print("-" * 50)

try: 
	for port in range(1,250):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target , port))
		if result == 0:
			print(" Port {} is open".format(port))
		s.close()
except KeyboardInterrupt :
	print("\nexiting program.")
	sys.exit()
except socket.gaierror :
	print("Host name could not be resolved")
	sys.exit()
except socket.error :
	print("could not connect to server")
	sys.exit()
