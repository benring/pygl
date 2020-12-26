import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from keycallback import *


w, h = 500,500

# ---Section 1---
def square(x=0, y=0, d=1):
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS) # Begin the sketch
    glColor3f(0.5, 0.0, 1.0)
    glVertex2f(x, y) # Coordinates for the bottom left point
    glVertex2f(x+d, y) # Coordinates for the bottom right point
    glColor3f(1.0, 0.5, 1.0)
    glVertex2f(x+d, y+d) # Coordinates for the top right point
    glVertex2f(x, y+d) # Coordinates for the top left point
    glEnd() # Mark the end of drawing

# This alone isn't enough to draw our square


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
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 1.0)

	glMatrixMode(GL_MODELVIEW)

# for reshaping the window
def reshape(w, h):
	print('w,h = {}, {}\n'.format(w,h))
	glViewport(0, 0, w, h)
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity()
	gluPerspective(45.0, w/h, -100, 100.0)
	glMatrixMode(GL_MODELVIEW)

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    square(0, 0, d=10) # Draw a square using our function
    glutSwapBuffers()

#---Section 3---
keyboard = keyCallBack()
glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(640, 480)   # Set the w and h of your window
glutInitWindowPosition(50, 50)   # Set the position at which this windows should appear
wind = glutCreateWindow("My OpenGL Window") # Set a window title
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen) # Keeps the window open
# glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard.keyPressed)  # Registered keyboard callback function
InitGL(640, 480)
glutMainLoop()  # Keeps the above created window displaying/running in a loop