from OpenGL.GL import *
from OpenGL.GLUT import *

from collections import OrderedDict

glutObject = OrderedDict({
	"sphere"	: lambda : glutSolidSphere(3., 120, 120),
	"cube"		: lambda : glutSolidCube(3.),
	"cone"		: lambda : glutSolidCone(3., 3., 120, 120),
	"torus"		: lambda : glutSolidTorus(1.5, 3., 60, 60),
	"dode"		: lambda : glutSolidDodecahedron(),
	"octa"		: lambda : glutSolidOctahedron(),
	"tetra"		: lambda : glutSolidTetrahedron(),
	"icoha"		: lambda : glutSolidIcosahedron(),
	"teapot"	: lambda : glutSolidTeapotglutWireTeapot(3.)
})


objectNames = list(glutObject.keys())
print(glutObject.keys())


