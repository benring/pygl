from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

from keycallback import *
from shapes import *


# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0

r1, rx, ry, rz = 0,0,0,0



# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):				# We call this right after our OpenGL window is created.
	glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
	glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
	glDepthFunc(GL_LESS)				# The Type Of Depth Test To Do
	glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
	glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()					# Reset The Projection Matrix
										# Calculate The Aspect Ratio Of The Window
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



def doPolyTest():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()					# Reset The View
	glTranslatef(-1.5, 0.0, -6.0)
	polytest()
	glutSwapBuffers()


# The main drawing function.
def DrawGLScene():
	global r1, rx, ry, rz
	# Clear The Screen And The Depth Buffer
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()					# Reset The View

	# Move Left 1.5 units and into the screen 6.0 units.
	glTranslatef(-1.5, 0.0, -6.0)


	string = "TEST"
	for ch in string:
		glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(ch))

	glRotatef(r1, 1, 0, 0)
	glRotatef(r1, 0, 1, 0)
	glRotatef(r1, 0, 0, 1)
	cube()
	# square(-0.5, -.5, 0., 2.)
	# triangle()
	# prism()

	glutSwapBuffers()

	r1 += .75


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

	glutKeyboardFunc(keyboard.keyPressed)  # Registered keyboard callback function

	# Initialize our window.
	InitGL(640, 480)

	# Start Event Processing Engine
	glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.\n")
main()