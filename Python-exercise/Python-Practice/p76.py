class Shape:
	def __init__(self):
		self.color='Green'
		self.lineWeight=10.0

	def draw(self):
		print("Draw-to be implemented")
	def setColor(self, c):
		self.color=c
	def getColor(self):
		return self.color
	def setLineWeight(self,lwt):
		self.lineWeight=lwt
	def getLineWeight(self):
		return self.lineWeight

class Circle(Shape):
	def setCenter(self,c):
		self.center=c
	def getCenter(self):
		return self.center
	def setRadius(self,r):
		self.radius=r
	def getRadius(self):
		return self.radius
	def draw(self):
		print("Draw Circle (overriden function)")

class Point:
	def __init__(self,x,y):
		self.xCoordinate=x
		self.yCoordinate=y
	def setX(self,x):
		self.xCoordinate=x
	def setY(self,y):
		self.yCoordinate=y
	def getX(self):
		return self.xCoordinate
	def getY(self):
		return self.yCoordinate

p=Point(2,6)
cir=Circle(p,9)
cir.getColor()
cir.setColor('red')
cir.getColor()
cir.getLineWeight()
cir.draw()
cir.radius
		