from circle import Circle

bbd = 25.1
# NameError: name 'bbd_to_radius' is not defined
c = Circle(bbd_to_radius(bbd))

print 'A circle with a bbd of 25.1'
print 'has a radius of',c.radius
print 'and an area of',c.area()
print
