import HoldCategory

class Hold(object):
	'''
	This python class represents the hold on the wall

	Attributes:
		Size: the area that represents the circled area of the hold
		Shape: shape descriptor
		Color: (R,G,B)
		Category: a string that represents the hold Type
		Positivity: a double from 0 to 1 that represents how easy 
					it is to maintain contact with a hold
		Position: (x, y)
	'''

	def __init__(self, size, position, color):
		self.size = size
		self.position = position
		self.color = color
		self.category = None
		self.shape = None
		self.positivity = None

	def setCategory(self, category):
		'''
		Sets the category of the hold
		'''
		self.category = category

	def setShape(self, shape):
		'''
		Sets the shape descriptor for the hold
		'''
		self.shape = shape

	def getCategory(self):
		'''
		Gets the category of the hold
		'''
		return self.category

	def getPositivity(self):
		'''
		Gets the positivity of the hold
		'''
		return self.positivity