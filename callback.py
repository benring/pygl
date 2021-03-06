import logging
logging.basicConfig(format='%(message)s', level=logging.INFO)

from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

ESCAPE = '\x1b'

class CallBack:

	def __init__(self):
		pass

	def keyPressed (self, *args):
		key = args[0].decode('utf-8')
		if key == ESCAPE:
			logging.info('Program ending')
			sys.exit()

	def specialKey(self, key, x, y):
		if key == GLUT_KEY_UP:
			pass
		elif key == GLUT_KEY_DOWN:
			pass
		elif key == GLUT_KEY_LEFT:
			pass
		elif key == GLUT_KEY_RIGHT:
			pass
		else:
			pass

	def mouse(self, button, state, x, y):
		if state == GLUT_UP:
			logging.info('{}: ({}, {})'.format(button, state, x, y))

