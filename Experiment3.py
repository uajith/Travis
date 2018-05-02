#!/usr/bin/python3.4
import subprocess
import os
class Greeter:
	def __init__(self):
		self.message = "This is a message"
if __name__ == "__main__":
	obj = Greeter()
	print (obj.message)
	x = subprocess.getoutput("ls")
	print (x)
