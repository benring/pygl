from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

from keycallback import *
from shapes import *

r1, rx, ry, rz = 0,0,0,0

ESCAPE = '\x1b'

class Point:
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	def __add__(self, p):
		# if type(p) == tuple:
		# 	x, y, z = p
		# else:
		# 	x, y, z = p.x, p.y, p.z
		self.x += p.x
		self.y += p.y
		self.z += p.z

	def __sub__(self, p):
		self.x -= p.x
		self.y -= p.y
		self.z -= p.z

	def add(self, p):
		self.x += p.x
		self.y += p.y
		self.z += p.z


	def get(self):
		return (self.x, self.y, self.z)

class callBack:

	def __init__(self):
		self.keyCache = ''
		self.rot = 1.0
		self.speed = 0.5
		self.pos = Point()
		self.roam = False
		self.dir = Point(.01, .007, .00)

	def rotate(self):
		glRotatef(self.rot, 1, 0, 0)
		glRotatef(self.rot, 0, 1, 0)
		glRotatef(self.rot, 0, 0, 1)


	def checkBound(self):
		if abs(self.pos.x) > 10:
			self.dir.x *= -1.
		if abs(self.pos.y) > 10:
			self.dir.y *= -1.


	def translate(self):
		if self.roam:
			self.pos.add(self.dir)
			self.checkBound()

		glTranslatef(*self.pos.get())

	def keyPressed (self, *args):
		key = args[0].decode('utf-8')
		if key == '\x08':
			self.keyCache = self.keyCache[:-1]
		elif key == ESCAPE:
			sys.exit()
		elif key == 'r':
			self.roam = not self.roam
		elif key == '<':
			if self.speed > 0:
				self.speed -= .1
				print('speed = {}'.format(self.speed))
		elif key == '>':
			self.speed += .1
			print('speed = {}'.format(self.speed))
		else:
			self.keyCache += key
		sys.stdout.write(self.keyCache +"\r")
		sys.stdout.flush()

	def specialKey(self, key, x, y):
		if key == GLUT_KEY_UP:
			self.pos.y += .1
		elif key == GLUT_KEY_DOWN:
			self.pos.y -= .1
		elif key == GLUT_KEY_LEFT:
			self.pos.x -= .1
		elif key == GLUT_KEY_RIGHT:
			self.pos.x += .1
		else:
			print("Some other special key")

	def mouse(self, button, state, x, y):
		if state == GLUT_UP:
			print('{}: ({}, {})'.format(button, state, x, y))


state = callBack()


class Light:

	LIGHT_LIST = [GL_LIGHT0, GL_LIGHT1, GL_LIGHT2, GL_LIGHT3, GL_LIGHT4, GL_LIGHT5, GL_LIGHT6, GL_LIGHT7]
	activeLights = 0

	def __init__(self, *args):
		if (len(args)) == 3:
			self.pos = Point(*args)
		else:
			self.pos = Point()
		self.id = Light.LIGHT_LIST[Light.activeLights]
		Light.activeLights += 1


	def setPos(self, p):
		self.pos = p

	def setPos(self, x, y, z):
		self.pos = Point(x, y, z)

	def call(self):
		glEnable(self.id);
		glLightfv(self.id, GL_POSITION, *self.pos.get(), 0.0)
		glLightfv(self.id, GL_AMBIENT, 0., 1., 0.)


# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.

	mat_spec  = (0.0, 1.0, 0.0, 1.0)
	mat_shiny = 100.0

	lite0 = Light(-.1, 10, -5.0)

	glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
	glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
	glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
	glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
	glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading

	# Set up lighting
	glMaterialfv(GL_FRONT, GL_SPECULAR, *mat_spec)
	glMaterialfv(GL_FRONT, GL_SHININESS, mat_shiny)


	glEnable(GL_LIGHT0);
	glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 0, 0])
	# glLightfv(self.id, GL_AMBIENT, 0., 1., 0.)

	glEnable(GL_LIGHTING);
	glEnable(GL_DEPTH_TEST);

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()					# Reset The Projection Matrix
	# gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	glOrtho (-10, 10, -10,10, -10.0, 10.0);
	glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
	if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small
		Height = 1
	glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	# gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	glOrtho (-10, 10, -10,10, -10.0, 10.0);
	glMatrixMode(GL_MODELVIEW)


# The main drawing function.
def DrawGLScene():
	global state

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	# glTranslatef(0., 0.0, -10.0)
	state.translate()
	# state.rotate()
	# cube()
	glutSolidSphere(3., 60, 60)
	glutSwapBuffers()
	state.rot += state.speed


def main():
	global window, state

	# pass arguments to init
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

	# get a 640 x 480 window
	glutInitWindowSize(640, 480)

	# the window starts at the upper left corner of the screen
	glutInitWindowPosition(0, 0)

	window = glutCreateWindow("My OpenGL Canvas")

	glutDisplayFunc(DrawGLScene)		# Register the drawing function with glut
	#glutFullScreen()
	glutIdleFunc(DrawGLScene)		# When we are doing nothing, redraw the scene.
	glutReshapeFunc(ReSizeGLScene)
	glutKeyboardFunc(state.keyPressed)  # Registered keyboard callback function
	glutSpecialFunc(state.specialKey)
	glutMouseFunc(state.mouse)

	InitGL(640, 480)			# Initialize our window.
	glutMainLoop()				# Start Event Processing Engine


# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.\n")
main()