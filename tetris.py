import logging
logging.basicConfig(format='%(message)s', level=logging.INFO)

import math
import random

import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from util import *
from shapes import *
from objects import *
from lights import Light

PIXEL_PER_UNIT = 32

state = Singleton()


ESCAPE = '\x1b'
X_LIMIT = 5
Y_LIMIT = 9


class Block:
	def __init__(self):
		pass

	def draw(self):
		pass

class iBlock(Block):
	def __init__(self):
		super().__init__()

	def draw(self):
		glPushMatrix()
		glTranslatef(-2, 0, 0)
		glutSolidCube(.95)
		glTranslatef(1, 0, 0)
		glutSolidCube(.95)
		glTranslatef(1, 0, 0)
		glutSolidCube(.95)
		glTranslatef(1, 0, 0)
		glutSolidCube(.95)
		glPopMatrix()


class tBlock(Block):
	def __init__(self):
		super().__init__()

	def draw(self):
		glPushMatrix()
		glTranslatef(-1, 0, 0)
		glutSolidCube(.95)
		glTranslatef(1, 0, 0)
		glutSolidCube(.95)
		glTranslatef(1, 0, 0)
		glutSolidCube(.95)
		glTranslatef(-1, 1, 0)
		glutSolidCube(.95)
		glPopMatrix()

class lBlock(Block):
	def __init__(self):
		super().__init__()

	def draw(self):
		glPushMatrix()
		glTranslatef(-1, 0, 0)
		glutSolidCube(.95)
		glTranslatef(1, 0, 0)
		glutSolidCube(.95)
		glTranslatef(1, 0, 0)
		glutSolidCube(.95)
		glTranslatef(0, 1, 0)
		glutSolidCube(.95)
		glPopMatrix()


class oBlock(Block):
	def __init__(self):
		super().__init__()

	def draw(self):
		glPushMatrix()
		glTranslatef(-1, 0, 0)
		glutSolidCube(.95)
		glTranslatef(1, 0, 0)
		glutSolidCube(.95)
		glTranslatef(0, 1, 0)
		glutSolidCube(.95)
		glTranslatef(-1, 0, 0)
		glutSolidCube(.95)
		glPopMatrix()


def getNewBlock():
	n = random.randint(0, 3)
	if n == 0:
		return iBlock()
	elif n == 1:
		return tBlock()
	elif n == 2:
		return lBlock()
	else:
		return oBlock()


class CallBack:

	def __init__(self):
		self.rotation = 0
		self.height = 10
		self.delay = 10
		self.timer = self.delay
		self.offset = 0
		self.stackHeight = -Y_LIMIT
		self.moving = True
		self.activeBlock = None

	def resetActive(self):
		self.activeBlock = getNewBlock()
		self.height = 10
		self.offset = 0

	def checkContact(self):
		if self.height <= self.stackHeight:
			self.moving = False

	def cycle(self):
		if self.moving:
			self.timer -= 1
			if self.timer == 0:
				self.height -= .1
				self.timer = self.delay
		else:
			self.activeBlock = None
		self.checkContact()


	def keyPressed (self, *args):

		key = args[0].decode('utf-8')
		if key == ESCAPE:
			logging.info('Program ending')
			sys.exit()

	def specialKey(self, key, x, y):
		if key == GLUT_KEY_UP:
			self.rotation -= 90
			if self.rotation < 0:
				self.rotation = 270
		elif key == GLUT_KEY_DOWN:
			self.rotation += 90
			if self.rotation == 360:
				self.rotation = 0
		elif key == GLUT_KEY_LEFT:
			if self.offset > -X_LIMIT:
				self.offset -= 1
		elif key == GLUT_KEY_RIGHT:
			if self.offset < X_LIMIT:
				self.offset += 1
		else:
			pass

	def mouse(self, button, state, x, y):
		if state == GLUT_UP:
			logging.info('{}: ({}, {})'.format(button, state, x, y))


state = CallBack()





def ReSizeGLScene(Width, Height):
	global state

	x, y = Width/(2.*PIXEL_PER_UNIT), Height/(2.*PIXEL_PER_UNIT)
	z = 2*max(x, y) #approx z
	state.x, state.y, state.z = x, y, z
	# state.bounds.set(x, y, z)
	logging.info("Window: {} x {} ".format(Width, Height))
	if Height == 0:           # Prevent A Divide By Zero If The Window Is Too Small
		Height = 1
	glViewport(0, 0, Width, Height)   # Reset The Current Viewport And Perspective Transformation
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho (-x, x, -y, y, -z, z)
	glMatrixMode(GL_MODELVIEW)

def InitGL(Width, Height):        # We call this right after our OpenGL window is created.

	glClearColor(0.0, 0.0, 0.0, 0.0)  # This Will Clear The Background Color To Black
	glClearDepth(1.0)         # Enables Clearing Of The Depth Buffer
	glDepthFunc(GL_LESS)        # The Type Of Depth Test To Do
	glEnable(GL_DEPTH_TEST)       # Enables Depth Testing
	glShadeModel(GL_SMOOTH)       # Enables Smooth Color Shading
	glEnable(GL_NORMALIZE)

	#Set up material properties
	materials['brass'].set()

	# Set up lighting
	Light.default()
	glEnable(GL_LIGHTING);
	glEnable(GL_DEPTH_TEST);

	ReSizeGLScene(Width, Height)

	state.pos = 5

def DrawGLScene():
	global state, lite0

	if state.activeBlock == None:
		state.resetActive()

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	#  Draw your o1ject here
	glPushMatrix()
	glTranslate(state.offset, state.height, 0)
	glRotatef(state.rotation, 0, 0, 1)
	state.activeBlock.draw()
	# iBlock()
	# tBlock()
	# lBlock()
	# oBlock()
	glPopMatrix()
	glutSwapBuffers()

	state.cycle()

def main():
	global window, state
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowSize(480, 640)
	glutInitWindowPosition(0, 0)
	window = glutCreateWindow("My OpenGL Canvas")
	glutDisplayFunc(DrawGLScene)    # Register the drawing function with glut
	glutIdleFunc(DrawGLScene)   # When we are doing nothing, redraw the scene.
	glutReshapeFunc(ReSizeGLScene)
	glutKeyboardFunc(state.keyPressed)  # Registered keyboard callback function
	glutSpecialFunc(state.specialKey)
	glutMouseFunc(state.mouse)
	InitGL(480, 640)      # Initialize our window.
	glutMainLoop()


main()