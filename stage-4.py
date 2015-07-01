from circle import Circle

class Tire(Circle):

	def perimeter(self):
		return Circle.perimeter(self) * 1.25

t = Tire(22)
print 'A tire of radius',t.radius
print 'has an inner area of',t.area()
print 'and an odometer corrected perimeter of'
print t.perimeter()
print
