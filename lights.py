from OpenGL.GL import *
from math import sin, cos, tan, atan, degrees, radians


from util import *


class Light:

  LIGHT_LIST = [GL_LIGHT0, GL_LIGHT1, GL_LIGHT2, GL_LIGHT3, GL_LIGHT4, GL_LIGHT5, GL_LIGHT6, GL_LIGHT7]
  activeLights = 0

  def default():
    glEnable(GL_LIGHT0)
    lite = Light()
    lite.set()
    lite.ambient(colors['white'])

  def __init__(self, *args):
    self.theta = 90
    if (len(args)) == 3:
      self.pos = Point(*args)
    elif (len(args)) == 0:
      self.pos = Point(cos(radians(self.theta)), sin(radians(self.theta)), 0)
    else:
      self.pos = Point()
    self.id = Light.LIGHT_LIST[Light.activeLights]
    self.inf = True
    self.color = (*colors['white'], 1.)
    Light.activeLights += 1


  def setPos(self, *args):
    if len(args) == 0:
      self.pos = Point(cos(radians(self.theta)), sin(radians(self.theta)), 0)
    elif len(args) == 1:
      self.pos = p
    elif len(args) == 3:
        x, y, z = args[:3]
        self.pos = Point(x, y, z)
    else:
      print("ill defined set pos in Light!")

  def setColor(self, c):
    color = colors[c] if type(c) == str else c
    self.color = (*color, 1.)


  def set(self):
    glLightfv(self.id, GL_POSITION, [*self.pos.get(), 0.0])
    glLightfv(self.id, GL_DIFFUSE, self.color)
    glLightfv(self.id, GL_SPECULAR, self.color)
    # glLightfv(self.id, GL_SPECULAR, (1,1,1,1))


  def ambient(self, color):
    glLightfv(self.id, GL_AMBIENT, [*color, 1.])
