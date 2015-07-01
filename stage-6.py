from random import random, seed
from circle import Circle

n = 10000000
seed(8675309)
print 'Using Citrus(tm) version', Circle.version
circles = [Circle(random()) for i in xrange(n)]
print 'The average are of',n,'random circles'
avg = sum([c.area() for c in circles]) / n
print 'is %.1f ' % avg
print