# Set up logging
import traceback
from datetime import datetime as dt
import logging
import argparse

import numpy as np
import math
import random
from enum import Enum

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

# Command Line Arguemnt Hanlding
def parseArgs():
	parser = argparse.ArgumentParser(description="Ben's Tetris Program")
	# parser.add_argument('-f','--foo', help='Description for foo argument', required=True)
	# parser.add_argument('-b', '--bar', default='foobar')
	# parser.add_argument('--no-foo', action='store_false')
	parser.add_argument('--test', action='store_true')
	return parser.parse_args()



PIXEL_PER_UNIT = 32

game = Singleton()


ESCAPE = '\x1b'
X_LIMIT = 12
Y_LIMIT = 24
SPEED = 2
DELAY = 1

boundCheck = lambda a: a[0]>=0 and a[1]>=0 and a[0]<X_LIMIT and a[1]<Y_LIMIT




class STATE(Enum):
	INIT=0; PAUSE=1; FALL=2; LAND=3; COLLAPSE=4; REMOVE=5


# GameBoard
class GameBoard:
	def __init__(self):
		self.board = np.zeros([X_LIMIT, Y_LIMIT])
		self.cleared = []
		self.clearing = False
		self.timer = 0
		self.boardColor = colors['blue']
		self.flashColor = {True: 'darkkhaki', False: 'yellow'}

	def store(self, block, x, y):
		log.info(f"STORING! at {(x,y)}")
		try:
			target = block.getMask(x, y)
			log.info("Target is : {}".format(target))
			for i in target:
				# log.info('storing at  {}'.format(i))
				self.board[tuple(i)] = 1.  # set to true for now
			print(np.rot90(self.board))
		except Exception as e:
			log.error(traceback.format_exc())
			log.error('Target=> {},  i: {}'.format(target, i))
			sys.exit()

	def collapse(self):
		self.clearing = False
		for i, row in enumerate(range(Y_LIMIT)):
			if (self.board[:,i]).all():
				self.cleared.append(i)
				self.clearing = True
				self.timer = 10
		return self.clearing

	def remove(self):
		self.cleared.sort(reverse=False)
		while len(self.cleared) > 0:
			row = self.cleared.pop()
			log.info(f'Removing row:  {row}')
			for i in range(row, Y_LIMIT-1):
				self.board[:,i] = self.board[:,i+1]
			self.board[:,Y_LIMIT-1] = 0
		self.clearing = False

	def collision(self, indexList):
		# log.info("Check coll at: {}".format(indexList))
		try:
			for i, slot in enumerate(indexList):
				# log.info("Check slot  {}   :  {}   bounds: {}".format(slot, self.board[slot], boundCheck(slot)))
				if boundCheck(slot) and self.board[slot] == 1:
					log.info(f'Collision at {slot}')
					return True
			return False
		except Exception as e:
			log.error(traceback.format_exc())
			log.info(f'Checking: {slot}  >=  {(X_LIMIT, Y_LIMIT)}  check {slot >= (X_LIMIT, Y_LIMIT)}')
			sys.exit()

	def draw(self, state=STATE.FALL):
		try:
			glPushMatrix()
			glTranslatef(.5, .5, 0)
			for row in range(Y_LIMIT):
				if row in self.cleared:
					color = self.flashColor[self.timer % 2]
					log.info('Flash color:  {:10}    gbtimer= {}'.format(color, self.timer))
					glColor3f(*colors[color])
					self.timer -= 1
				else:
					glColor3f(*self.boardColor)
				for i, slot in enumerate(self.board[:,row]):
					if slot:
						glutSolidCube(.95)
					glTranslatef(1, 0, 0)
				glTranslatef(-X_LIMIT, 1, 0)
			glPopMatrix()
		except Exception as e:
			log.error(traceback.format_exc())
			# log.error('row=> {},  i: {}, slot: {}'.format(row, i, slot))
			sys.exit()


# Tetris Blocks
class Block:
	def __init__(self):
		self.mask = None		# List of indices
		self.title = "block"
		self.id = -1
		# self.height = Y_LIMIT*2-1
		# self.offset = X_LIMIT
		self.position = 0

	def rotateLeft(self):
		self.position = 3 if self.position == 0 else self.position-1

	def rotateRight(self):
		self.position = 0 if self.position == 3 else self.position+1


	def inBound(self, x, y):
		mask = self.getMask(x, y)
		for slot in mask:
			if not boundCheck(slot):
				return False
		return True

	def getMask(self, x, y):
		# log.info("GETMASK: pos: {}, X: {}, Y: {}".format(self.position,x,y))
		return [tuple(i) for i in (self.mask[self.position] + [x, y])]

	def draw(self, x, y):
		glPushMatrix()
		for t in self.transMask[self.position]:
			glTranslatef(*t)
			glutSolidCube(.95)
		glPopMatrix()

class iBlock(Block):
	def __init__(self):
		super().__init__()
		self.title = "i-Block"
		self.id = 0
		self.mask = np.array([
					[[-2, 0], [-1, 0], [0,0], [1,0]],
					[[0, 0], [0, 1], [0,2], [0,3]]]*2)
		self.transMask=[[(-2,0,0),(1,0,0),(1,0,0),(1,0,0)],
						[(0,0,0),(0,1,0),(0,1,0),(0,1,0)]]*2

class tBlock(Block):
	def __init__(self):
		super().__init__()
		self.title = "t-Block"
		self.id = 1
		self.mask = np.array([
					[[-1, 0], [0, 0], [1,0], [0,1]],
					[[0, 0], [0, 1], [0,2], [-1,1]],
					[[-1, 1], [0, 1], [1,1], [0,0]],
					[[0, 0], [0, 1], [0,2], [1,1]]])
		self.transMask=[[(-1,0,0),(1,0,0),(1,0,0),(-1,1,0)],
						[(0,0,0),(0,1,0),(0,1,0),(-1,-1,0)],
						[(-1,1,0),(1,0,0),(1,0,0),(-1,-1,0)],
						[(0,0,0),(0,1,0),(0,1,0),(1,-1,0)]]

class lBlock(Block):
	def __init__(self):
		super().__init__()
		self.title = "l-Block"
		self.id = 2
		self.mask = np.array([
					[[-1, 0], [0, 0], [1,0], [1,1]],
					[[0, 0], [0, 1], [0,2], [-1,2]],
					[[-1, 1], [0, 1], [1,1], [-1,0]],
					[[0, 0], [0, 1], [0,2], [1,0]]])
		self.transMask=[[(-1,0,0),(1,0,0),(1,0,0),(0,1,0)],
						[(0,0,0),(0,1,0),(0,1,0),(-1,0,0)],
						[(-1,1,0),(1,0,0),(1,0,0),(-2,-1,0)],
						[(0,0,0),(0,1,0),(0,1,0),(1,-2,0)]]

class rBlock(Block):
	def __init__(self):
		super().__init__()
		self.title = "r-Block"
		self.id = 3
		self.mask = np.array([
					[[-1, 0], [0, 0], [1,0], [-1,1]],
					[[0, 0], [0, 1], [0,2], [-1,0]],
					[[-1, 0], [0, 0], [1,0], [1,-1]],
					[[0, 0], [0, 1], [0,2], [1,2]]])
		self.transMask=[[(-1,0,0),(1,0,0),(1,0,0),(-2,1,0)],
						[(0,0,0),(0,1,0),(0,1,0),(-1,-2,0)],
						[(-1,0,0),(1,0,0),(1,0,0),(0,-1,0)],
						[(0,0,0),(0,1,0),(0,1,0),(1,0,0)]]

class oBlock(Block):
	def __init__(self):
		super().__init__()
		self.title = "o-Block"
		self.id = 4
		self.mask = np.array([[[-1, 0], [0, 0], [-1, 1], [0,1]]]*4)
		self.transMask=[[(-1,0,0),(1,0,0),(-1,1,0),(1,0,0)]]*4

class zBlock(Block):
	def __init__(self):
		super().__init__()
		self.title = "z-Block"
		self.id = 5
		self.mask = np.array([
					[[-1, 1], [0, 1], [0, 0], [1,0]],
					[[-1, -1], [-1, 0], [0, 0], [0,1]]]*2)
		self.transMask=[
					[(-1,1,0),(1,0,0),(0,-1,0),(1,0,0)],
					[(-1,-1,0),(0,1,0),(1,0,0),(0,1,0)]]*2

class sBlock(Block):
	def __init__(self):
		super().__init__()
		self.title = "s-Block"
		self.id = 6
		self.mask = np.array([
					[[-1, 0], [0, 0], [0, 1], [1,1]],
					[[0,0], [0, 1], [-1, 1], [-1,2]]]*2)
		self.transMask=[
					[(-1,0,0),(1,0,0),(0,1,0),(1,0,0)],
					[(0,0,0),(0,1,0),(-1,0,0),(0,1,0)]]*2

def getNewBlock(n=None):
	if n is None:
		n = random.randint(0, 7)
	if n == 0:
		return iBlock()
	elif n == 1:
		return tBlock()
	elif n == 2:
		return lBlock()
	elif n == 3:
		return rBlock()
	elif n == 4:
		return zBlock()
	elif n == 5:
		return sBlock()
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

# Callback / UI management & global game
class CallBack:

	def __init__(self):
		self.rotation = 0
		self.height = Y_LIMIT-1
		self.X = int(X_LIMIT/2)
		self.Y = Y_LIMIT - 1
		self.delay = DELAY  #10
		self.speed = SPEED  #1
		self.timer = self.delay
		self.activeBlock = getNewBlock()
		self.gameboard = GameBoard()
		self.state = STATE.INIT
		self.pausedState = STATE.PAUSE
		self.testblock = getNewBlock()


	def resetActive(self):
		self.activeBlock = getNewBlock()
		self.height = Y_LIMIT-1
		self.X = int(X_LIMIT/2)
		self.Y = Y_LIMIT - 1

	def cycle(self):
		log.debug("Cycle")
		if self.state == STATE.PAUSE:
			return

		if self.state == STATE.INIT:
			self.resetActive()
			self.state = STATE.FALL

		if self.state == STATE.REMOVE:  #collapsing:
			self.timer -= 1
			if self.timer == 0:
				self.gameboard.remove()
				self.state = STATE.INIT
				# DOUBLE CHECK HERE

		if self.state == STATE.FALL:  #falling:
			self.timer -= self.speed
			if self.timer <= 0:
				self.height -= .1
				self.Y = int(np.floor(self.height))
				self.timer = self.delay
				mask = self.activeBlock.getMask(self.X, self.Y)
				# log.info("Falling: {}, {}, {}".format(self.X, self.Y, mask))
				if self.Y < 0:
					self.Y = 0
					self.state = STATE.LAND
				elif self.gameboard.collision(mask):
					self.Y += 1
					self.state = STATE.LAND

		elif self.state == STATE.LAND:
			self.gameboard.store(self.activeBlock, self.X, self.Y)
			if self.gameboard.collapse():
				self.state = STATE.REMOVE
				self.timer = 6
			else:
				self.state = STATE.INIT

			# log.info('X: {}, Y:{}, coll {}'. format(self.X, self.Y, self.gameboard.collision(self.activeBlock.getMask(self.X, self.Y))))
			# self.resetActive()
			# log.info('X: {}, Y:{}, coll {}'. format(self.X, self.Y, self.gameboard.collision(self.activeBlock.getMask(self.X, self.Y))))


	def keyPressed (self, *args):

		key = args[0].decode('utf-8')
		if key == ESCAPE or key == 'q':
			log.info('Program ending')
			sys.exit()

		elif key == 'n':
			nextid = (self.testblock.id + 1) % 7
			self.testblock = getNewBlock(nextid)
			# log.info(f"Showing {self.testblock.title}")

			nextid = (self.activeBlock.id + 1) % 7
			self.activeBlock = getNewBlock(nextid)
			log.info(f"CHANGE BLOCK TO:  {self.activeBlock.title}")
		elif key == 'N':
			self.testblock = getNewBlock()
		elif key == 'p':
			if self.state == STATE.PAUSE:
				self.state = self.pausedState
			else:
				self.pausedState = self.state
				self.state = STATE.PAUSE
			# self.paused = not self.paused

	def specialKey(self, key, x, y):
		if key == GLUT_KEY_UP:
			self.activeBlock.rotateLeft()
			if not self.activeBlock.inBound(self.X, self.Y):
				log.info("Illegal Rotatiom!")
				self.activeBlock.rotateRight()
			else:
				log.info(f'{self.activeBlock.title}  pos: {self.activeBlock.position}')
			# log.info(f'Block: pos0:  {pos0}  pos: {self.activeBlock.position},  x: {self.X},  y: {self.Y},  mask: {self.activeBlock.getMask(self.X, self.Y)}')
		elif key == GLUT_KEY_DOWN:
			self.height -= 1
		elif key == GLUT_KEY_LEFT:
			if self.X > 0:
				self.X -= 1
				if not self.activeBlock.inBound(self.X, self.Y):
					log.info("Illegal Move!")
					self.X += 1
				if self.gameboard.collision(self.activeBlock.getMask(self.X, self.Y)):
					self.X += 1
					log.info('COLLISION')
		elif key == GLUT_KEY_RIGHT:
			if self.X < X_LIMIT-1:
				self.X += 1
				if not self.activeBlock.inBound(self.X, self.Y):
					log.info("Illegal Move!")
					self.X -= 1
				if self.gameboard.collision(self.activeBlock.getMask(self.X, self.Y)):
					self.X -= 1
					log.info('COLLISION')
		else:
			pass

	def mouse(self, button, status, x, y):
		if status == GLUT_UP:
			log.info('{}: ({}, {})'.format(button, status, x, y))

game = CallBack()


def ReSizeGLScene(Width, Height):
	# global game

	# x, y = Width/(2.*PIXEL_PER_UNIT), Height/(2.*PIXEL_PER_UNIT)
	# z = 2*max(x, y) #approx z
	# game.x, game.y, game.z = x, y, z
	# # game.bounds.set(x, y, z)
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
	glColor3f(*colors['aqua'])

	# Set up lighting
	# lite0 = Light()
	# glEnable(lite0.id)
	# lite0.setPos(0, 0, 1)
	# lite0.set()
	# lite0.ambient(colors['grey'])
	# lite0.setColor('white')
	# glEnable(GL_LIGHTING)
	glEnable(GL_DEPTH_TEST)

	ReSizeGLScene(Width, Height)

	game.pos = 5

def DrawGLScene():
	global game, lite0

	# if game.activeBlock == None:
	# 	game.resetActive()

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	materials['pearl'].set()
	glutSolidSphere(.5, 120, 120)
	materials['brass'].set()

	glColor3f(*colors['blue'])
	game.gameboard.draw()

	#  Draw your o1ject here
	glPushMatrix()
	glTranslatef(.5, .5, 0)
	glTranslatef(game.X, game.Y, 0)
	# glRotatef(game.rotation, 0, 0, 1)
	materials['cyanplastic'].set()
	glColor3f(*colors['aqua'])
	game.activeBlock.draw(game.X, game.Y)
	glColor3f(*colors['blue'])
	materials['brass'].set()
	glPopMatrix()
	glutSwapBuffers()

	game.cycle()

def TestBlocks():
	global game, lite0, testblock

	# if game.activeBlock == None:
	# 	game.resetActive()

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	materials['pearl'].set()
	glutSolidSphere(.5, 120, 120)
	materials['brass'].set()

	glColor3f(*colors['blue'])
	# testblock = sBlock()
	glPushMatrix()
	glTranslatef(4, 3, 0)
	# log.info("MASK is  {}".format(testblock.mask))
	for p in range(4):
		c = .1
		color = (0, c, 0)
		for x,y in game.testblock.mask[p]:
			# log.info('POS: {}   ->  {}, {}'.format(p,x,y))
			glTranslatef(x, y, 0)
			glColor3f(*color)
			glutSolidCube(.95)
			c += .3
			color = (0, c, 0)
			glTranslatef(-x, -y, 0)
		glTranslatef(0, 5, 0)
	glPopMatrix()

	glPushMatrix()
	glTranslatef(8, 3, 0)
	# log.info("MASK is  {}".format(testblock.mask))
	for p in range(4):
		c = .1
		color = (0, c, 0)
		glPushMatrix()
		for t in game.testblock.transMask[p]:
			# log.info('POS: {}   ->  {}, {}'.format(p,x,y))
			glTranslatef(*t)
			glColor3f(*color)
			glutSolidCube(.95)
			c += .3
			color = (c, 0, 0)
			# glTranslatef(-x, -y, 0)
		glPopMatrix()
		glTranslatef(0, 5, 0)
	glPopMatrix()

	glutSwapBuffers()

def main():
	global window, game

	args = parseArgs()

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

	w, h = X_LIMIT*PIXEL_PER_UNIT, Y_LIMIT*PIXEL_PER_UNIT
	glutInitWindowSize(w, h)
	glutInitWindowPosition(0, 0)
	window = glutCreateWindow("Ben's Tetris")

	if args.test:
		glutDisplayFunc(TestBlocks)    # Register the drawing function with glut
		glutIdleFunc(TestBlocks)   # When we are doing nothing, redraw the scene.
	else:
		glutDisplayFunc(DrawGLScene)    # Register the drawing function with glut
		glutIdleFunc(DrawGLScene)   # When we are doing nothing, redraw the scene.

	glutReshapeFunc(ReSizeGLScene)
	glutKeyboardFunc(game.keyPressed)  # Registered keyboard callback function
	glutSpecialFunc(game.specialKey)
	glutMouseFunc(game.mouse)
	InitGL(w, h)      # Initialize our window.
	glutMainLoop()


main()