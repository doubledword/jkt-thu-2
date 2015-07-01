from random import random, seed
from circle import Circle

seed(8675309)
print 'Using Citrus(tm) version', Circle.version
n = 10
circles = [Circle(random()) for i in xrange(n)]
print 'The average are of',n,'random circles'
avg = sum([c.area() for c in circles]) / n
print 'is %.1f ' % avg
print