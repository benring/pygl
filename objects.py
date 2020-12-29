from OpenGL.GL import *
from OpenGL.GLUT import *

from collections import OrderedDict

glutObject = OrderedDict({
	"sphere"	: lambda : glutSolidSphere(1., 120, 120),
	"cube"		: lambda : glutSolidCube(1.),
	"cone"		: lambda : glutSolidCone(1., 1., 120, 120),
	"torus"		: lambda : glutSolidTorus(.5, 1., 60, 60),
	"dode"		: lambda : glutSolidDodecahedron(),
	"octa"		: lambda : glutSolidOctahedron(),
	"tetra"		: lambda : glutSolidTetrahedron(),
	"icoha"		: lambda : glutSolidIcosahedron(),
	"teapot"	: lambda : glutSolidTeapotglutWireTeapot(1.)
})


objectNames = list(glutObject.keys())
print(glutObject.keys())


