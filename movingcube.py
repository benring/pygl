from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

from keycallback import *
from shapes import *

r1, rx, ry, rz = 0,0,0,0

ESCAPE = '\x1b'

class callBack:

	def __init__(self):
		self.keyCache = ''
		self.rot = 1.0
		self.speed = 0.5
		self.xpos = 0.0
		self.ypos = 0.0
		self.zpos = 0.0

	def rotate(self):
		glRotatef(self.rot, 1, 0, 0)
		glRotatef(self.rot, 0, 1, 0)
		glRotatef(self.rot, 0, 0, 1)

	def translate(self):
		glTranslatef(self.xpos, self.ypos, self.zpos)

	def keyPressed (self, *args):
		key = args[0].decode('utf-8')
		if key == '\x08':
			self.keyCache = self.keyCache[:-1]
		elif key == ESCAPE:
			sys.exit()
		elif key == 'm':
			print ("You pressed m\n")
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
			self.ypos += .1
		elif key == GLUT_KEY_DOWN:
			self.ypos -= .1
		elif key == GLUT_KEY_LEFT:
			self.xpos -= .1
		elif key == GLUT_KEY_RIGHT:
			self.xpos += .1
		else:
			print("Some other special key")

state = callBack()


# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
	glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
	glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
	glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
	glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
	glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()					# Reset The Projection Matrix
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
	if Height == 0:						# Prevent A Divide By Zero If The Window Is Too Small
		Height = 1
	glViewport(0, 0, Width, Height)		# Reset The Current Viewport And Perspective Transformation
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)


# The main drawing function.
def DrawGLScene():
	global state

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()					

	glTranslatef(0., 0.0, -10.0)

	state.translate()
	state.rotate()
	cube()
	glutSwapBuffers()

	state.rot += state.speed


def main():
	global window
	keyboard = keyCallBack()


	# pass arguments to init
	glutInit(sys.argv)

	# Select type of Display mode:
	#  Double buffer
	#  RGBA color
	# Alpha components supported
	# Depth buffer
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

	# get a 640 x 480 window
	glutInitWindowSize(640, 480)

	# the window starts at the upper left corner of the screen
	glutInitWindowPosition(0, 0)

	# Okay, like the C version we retain the window id to use when closing, but for those of you new
	# to Python (like myself), remember this assignment would make the variable local and not global
	# if it weren't for the global declaration at the start of main.
	window = glutCreateWindow("Jeff Molofee's GL Code Tutorial ... NeHe '99")

   	# Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
	# set the function pointer and invoke a function to actually register the callback, otherwise it
	# would be very much like the C version of the code.
	glutDisplayFunc(DrawGLScene)

	# Uncomment this line to get full screen.
	#glutFullScreen()

	# When we are doing nothing, redraw the scene.
	glutIdleFunc(DrawGLScene)

	# Register the function called when our window is resized.
	glutReshapeFunc(ReSizeGLScene)

	glutKeyboardFunc(state.keyPressed)  # Registered keyboard callback function
	glutSpecialFunc(state.specialKey)

	# Initialize our window.
	InitGL(640, 480)

	# Start Event Processing Engine
	glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.\n")
main()