# Tutorial
from circle import Circle

print 'Citrus version', Circle.version

c = Circle(10)
print 'A circle of radius', c.radius
print 'has an area of', c.area()
print