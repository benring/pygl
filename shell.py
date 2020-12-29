import logging
logging.basicConfig(format='%(message)s', level=logging.INFO)

import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from util import *
from shapes import *
from lights import Light
from callback import CallBack

PIXEL_PER_UNIT = 32

state = Singleton()
callback = CallBack()

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

def DrawGLScene():
	global state, lite0

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()

	#  Draw your object here
	glScalef(3,3,3)
	square()

	glutSwapBuffers()

def main():

	# pass arguments to init
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

	# get a 640 x 480 window
	glutInitWindowSize(640, 480)
	glutInitWindowPosition(0, 0)
	window = glutCreateWindow("My OpenGL Canvas")

	glutDisplayFunc(DrawGLScene)    # Register the drawing function with glut
	glutIdleFunc(DrawGLScene)   # When we are doing nothing, redraw the scene.
	glutReshapeFunc(ReSizeGLScene)
	glutKeyboardFunc(callback.keyPressed)  # Registered keyboard callback function
	glutSpecialFunc(callback.specialKey)
	glutMouseFunc(callback.mouse)

	InitGL(640, 480)      # Initialize our window.
	glutMainLoop()        # Start Event Processing Engine


main()