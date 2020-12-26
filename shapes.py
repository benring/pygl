from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


polyargs = [GL_POINTS, GL_LINES, GL_LINE_STRIP, GL_LINE_LOOP, GL_TRIANGLES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_QUADS, GL_QUAD_STRIP, GL_POLYGON]

class state:
	def __init__(self):
		self.rotate = 0

def square(x=0, y=0, z=0, d=1):
    # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
    glBegin(GL_QUADS) # Begin the sketch
    glVertex3f(x, y, z) # Coordinates for the bottom left point
    glVertex3f(x+d, y, z) # Coordinates for the bottom right point
    glVertex3f(x+d, y+d, z) # Coordinates for the top right point
    glVertex3f(x, y+d, z) # Coordinates for the top left point
    glEnd() # Mark the end of drawing


def polytest():
	x, y, z = 0, 0, 0
	d = .25
	# glTranslatef(-2., 0, 0)
	for p in polyargs:
	    glBegin(p) 
	    glVertex3f(x, y, z)
	    glVertex3f(x+d, y, z)
	    glVertex3f(x+d, y+d, z)
	    glVertex3f(x, y+d, z)
	    glEnd() # Mark the end of drawing
	    x += .3



def triangle():
	glBegin(GL_POLYGON)                 # Start drawing a polygon
	glColor3f(1.0, 0.0, 0.0)            # Red
	glVertex3f(0.0, 1.0, 0.0)           # Top
	glColor3f(0.0, 1.0, 0.0)            # Green
	glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
	glColor3f(0.0, 0.0, 1.0)            # Blue
	glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
	glEnd() 



def prism():
	glBegin(GL_LINE_STRIP)                 # Start drawing a polygon
	glColor3f(1.0, 0.0, 0.0)            # Red
	glVertex3f(0.0, 1.0, .0)           # Top

	glColor3f(0.0, 1.0, 0.0)            # Green
	glVertex3f(1.0, -1.0, -1.0)          # Bottom Right

	glColor3f(0.0, 0.0, 1.0)            # Blue
	glVertex3f(-1.0, -1.0, -1.0)         # Bottom Left

	glColor3f(0.0, 0.0, 1.0)            # Blue
	glVertex3f(0., -1., 0)         # Bottom Left
	glEnd() 


def cube(clist=[]):

	polyargs = [GL_POINTS, GL_LINES, GL_LINE_STRIP, GL_LINE_LOOP, GL_TRIANGLES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_QUADS, GL_QUAD_STRIP, GL_POLYGON]


	if len(clist) == 0:
		clist = [(1,0,0), (1,1,0), (0,1,0), (0,1,1), (0,0,1), (1,0,1)]

	glBegin(GL_QUADS)
	
	glColor3f(*clist[0])
	glVertex3f( 1.0, 1.0,-1.0)
	glVertex3f(-1.0, 1.0,-1.0)
	glVertex3f(-1.0, 1.0, 1.0)
	glVertex3f( 1.0, 1.0, 1.0) 
	
	glColor3f(*clist[1])
	glVertex3f( 1.0,-1.0, 1.0)
	glVertex3f(-1.0,-1.0, 1.0)
	glVertex3f(-1.0,-1.0,-1.0)
	glVertex3f( 1.0,-1.0,-1.0) 
	
	glColor3f(*clist[2])
	glVertex3f( 1.0, 1.0, 1.0)
	glVertex3f(-1.0, 1.0, 1.0)
	glVertex3f(-1.0,-1.0, 1.0)
	glVertex3f( 1.0,-1.0, 1.0)
	
	glColor3f(*clist[3])
	glVertex3f( 1.0,-1.0,-1.0)
	glVertex3f(-1.0,-1.0,-1.0)
	glVertex3f(-1.0, 1.0,-1.0)
	glVertex3f( 1.0, 1.0,-1.0)
	
	glColor3f(*clist[4])
	glVertex3f(-1.0, 1.0, 1.0) 
	glVertex3f(-1.0, 1.0,-1.0)
	glVertex3f(-1.0,-1.0,-1.0) 
	glVertex3f(-1.0,-1.0, 1.0) 
	
	glColor3f(*clist[5])
	glVertex3f( 1.0, 1.0,-1.0) 
	glVertex3f( 1.0, 1.0, 1.0)
	glVertex3f( 1.0,-1.0, 1.0)
	glVertex3f( 1.0,-1.0,-1.0)
	
	glEnd()	

