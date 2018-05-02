#!/usr/bin/python2.7
import commands
class Greeter:
	def __init__(self):
		status, output = commands.getstatusoutput("/usr/bin/python2.7 --version")
		self.message = output
if __name__ == "__main__":
	obj = Greeter()
	print obj.message
