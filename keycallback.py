import sys

ESCAPE = '\x1b'



class keyCallBack:

	def __init__(self):
		self.keyCache = ''

	def keyPressed (self, *args):
		key = args[0].decode('utf-8')
		if key == '\x08':
			self.keyCache = self.keyCache[:-1]
		elif key == ESCAPE:
			sys.exit()
		elif key == 'm':
			print ("You pressed m\n")
		else:
			self.keyCache += key
		sys.stdout.write(self.keyCache +"\r")
		sys.stdout.flush()