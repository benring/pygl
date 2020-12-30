# Set up logging
import traceback
from datetime import datetime as dt
import logging

import numpy as np
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


# Set up Logging
startTime = dt.now()
timestamp = lambda : (dt.now() - start).total_seconds()
# logging.basicConfig(level=logging.INFO)

class LogFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        return '{:.3f}'.format((dt.now() - startTime).total_seconds())

handler = logging.StreamHandler()
handler.setFormatter(LogFormatter('%(asctime)s > %(message)s'))
log = logging.getLogger('main')
log.addHandler(handler)
log.setLevel(logging.INFO)

PIXEL_PER_UNIT = 32

state = Singleton()


ESCAPE = '\x1b'
X_LIMIT = 12
Y_LIMIT = 24
SPEED = 1
DELAY = 1

# GameBoard
class GameBoard:
	def __init__(self):
		self.board = np.zeros([X_LIMIT, Y_LIMIT])
		# self.maxHeight = 0

	def store(self, block, x, y):
		log.info("STORING!")
		try:
			target = block.getMask(x, y)
			log.info("Target is : {}".format(target))
			for i in target:
				# log.info('storing at  {}'.format(i))
				self.board[tuple(i)] = 1.  # set to true for now
			print(self.board)
		except Exception as e:
			log.error(traceback.format_exc())
			log.error('Target=> {},  i: {}'.format(target, i))
			sys.exit()

	def collision(self, indexList):
		# log.info("Check coll at: {}".format(indexList))
		try:
			for i, slot in enumerate(indexList):
				# log.info(f'Checking: {slot}, {type(slot)}')
				if slot < (0,0) or slot >= (X_LIMIT, Y_LIMIT):
					continue
				if self.board[slot]:
					return True
			return False
		except Exception as e:
			log.error(traceback.format_exc())
			sys.exit()

	def draw(self):
		glPushMatrix()
		glLoadIdentity()
		try:
			for row in range(Y_LIMIT):
				for i, slot in enumerate(self.board[:,row]):
					if slot:
						glutSolidCube(.95)
					glTranslatef(1, 0, 0)
				glTranslatef(-X_LIMIT, 1, 0)
		except Exception as e:
			log.error(traceback.format_exc())
			log.error('row=> {},  i: {}, slot: {}'.format(row, i, slot))
			sys.exit()
		glPopMatrix()



# Tetris Blocks
class Block:
	def __init__(self):
		self.mask = None		# List of indices
		self.title = "block"
		# self.height = Y_LIMIT*2-1
		# self.offset = X_LIMIT
		self.position = 0

	def getMask(self, x, y):
		# log.info("GETMASK: pos: {}, X: {}, Y: {}".format(self.position,x,y))
		return [tuple(i) for i in (self.mask[self.position] + [x, y])]

	def draw(self):
		pass

class iBlock(Block):
	def __init__(self):
		super().__init__()
		self.title = "i-Block"
		self.mask = np.array([
					[[-2, 0], [-1, 0], [0,0], [1,0]],
					[[-1, 0], [-1, 1], [-1,2], [-1,3]]]*2)

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
		self.mask = np.array([
					[[-2, 0], [-1, 0], [0,0], [1,0]],
					[[-1, 0], [-1, 1], [-1,2], [-1,3]]])

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
		self.mask = np.array([
					[[-2, 0], [-1, 0], [0,0], [1,0]],
					[[-1, 0], [-1, 1], [-1,2], [-1,3]]]*2)

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
		self.title = "o-Block"
		self.mask = np.array([[[-1, 0], [1, 0], [0,1], [1,1]]]*4)

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
		return iBlock()
	elif n == 2:
		return oBlock()
	else:
		return oBlock()

def debugGrid():

	materials['whiteplastic'].set()
	for i in range(X_LIMIT):
		glBegin(GL_LINES)
		glVertex3f(i, 0, 0)
		glVertex3f(i, Y_LIMIT, 0)
		glEnd()

	for i in range(Y_LIMIT):
		glBegin(GL_LINES)
		glVertex3f(0, i, 0)
		glVertex3f(X_LIMIT, i, 0)
		glEnd()



# Callback / UI management & global state
class CallBack:

	def __init__(self):
		self.rotation = 0
		self.height = Y_LIMIT
		self.X = int(X_LIMIT/2)
		self.Y = Y_LIMIT - 1
		self.delay = DELAY  #10
		self.speed = SPEED  #1
		self.timer = self.delay
		# self.offset = 0
		# self.stackHeight = 0
		self.falling = True
		self.activeBlock = None
		self.gameboard = GameBoard()


	def resetActive(self):
		self.activeBlock = getNewBlock()
		self.height = Y_LIMIT-1
		# self.offset = 0
		self.falling = True
		self.X = int(X_LIMIT/2)
		self.Y = Y_LIMIT - 1

	def cycle(self):
		log.debug("Cycle")
		if self.falling:
			self.timer -= self.speed
			if self.timer <= 0:
				self.height -= .25
				self.Y = int(np.floor(self.height))
				self.timer = self.delay
				# log.info("Falling: {}, {}, {}".format(self.X, self.Y, self.height))
				if self.Y < 0:
					self.Y = 0
					self.falling = False
				elif self.gameboard.collision(self.activeBlock.getMask(self.X, self.Y)):
					self.Y -= 1
					self.falling = False
		else:
			self.gameboard.store(self.activeBlock, self.X, self.Y)
			log.info('X: {}, Y:{}, coll {}'. format(self.X, self.Y, self.gameboard.collision(self.activeBlock.getMask(self.X, self.Y))))
			self.resetActive()
			log.info('X: {}, Y:{}, coll {}'. format(self.X, self.Y, self.gameboard.collision(self.activeBlock.getMask(self.X, self.Y))))


	def keyPressed (self, *args):

		key = args[0].decode('utf-8')
		if key == ESCAPE:
			log.info('Program ending')
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
			if self.X > 0:
				self.X -= 1
				if self.gameboard.collision(self.activeBlock.getMask(self.X, self.Y)):
					self.X += 1
					log.info('COLLISION')
		elif key == GLUT_KEY_RIGHT:
			if self.X < X_LIMIT-1:
				self.X += 1
				if self.gameboard.collision(self.activeBlock.getMask(self.X, self.Y)):
					self.X -= 1
					log.info('COLLISION')
		else:
			pass

	def mouse(self, button, state, x, y):
		if state == GLUT_UP:
			log.info('{}: ({}, {})'.format(button, state, x, y))

state = CallBack()


def ReSizeGLScene(Width, Height):
	global state

	x, y = Width/(2.*PIXEL_PER_UNIT), Height/(2.*PIXEL_PER_UNIT)
	z = 2*max(x, y) #approx z
	state.x, state.y, state.z = x, y, z
	# state.bounds.set(x, y, z)
	log.info("Window: {} x {} ".format(Width, Height))
	if Height == 0:           # Prevent A Divide By Zero If The Window Is Too Small
		Height = 1
	glViewport(0, 0, Width, Height)   # Reset The Current Viewport And Perspective Transformation
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	# glOrtho (-x, x, -y, y, -z, z)
	glOrtho (0, X_LIMIT, 0, Y_LIMIT, -10, 10)
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
	glEnable(GL_LIGHTING)
	glEnable(GL_DEPTH_TEST)

	ReSizeGLScene(Width, Height)

	state.pos = 5

def DrawGLScene():
	global state, lite0

	if state.activeBlock == None:
		state.resetActive()

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	materials['pearl'].set()
	glutSolidSphere(.5, 120, 120)
	materials['brass'].set()

	state.gameboard.draw()

	#  Draw your o1ject here
	glPushMatrix()
	glTranslate(state.X, state.Y, 0)
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

	debugGrid()

	w, h = X_LIMIT*PIXEL_PER_UNIT, Y_LIMIT*PIXEL_PER_UNIT
	glutInitWindowSize(w, h)
	glutInitWindowPosition(0, 0)
	window = glutCreateWindow("Ben's Tetris")
	glutDisplayFunc(DrawGLScene)    # Register the drawing function with glut
	glutIdleFunc(DrawGLScene)   # When we are doing nothing, redraw the scene.
	glutReshapeFunc(ReSizeGLScene)
	glutKeyboardFunc(state.keyPressed)  # Registered keyboard callback function
	glutSpecialFunc(state.specialKey)
	glutMouseFunc(state.mouse)
	InitGL(w, h)      # Initialize our window.
	glutMainLoop()


main()