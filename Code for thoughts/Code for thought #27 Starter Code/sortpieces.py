## Fill in the missing code to generate the following printout.

##C: 4 50.26548245743669
##C: 1 3.141592653589793
##C: 9 254.46900494077323
##C: 1 3.141592653589793
##C: 3 28.274333882308138
##R: 4 1 4
##R: 1 3 3
##R: 6 4 24
##R: 2 6 12
##R: 8 6 48
##---------------------------
##C: 9 254.46900494077323
##C: 4 50.26548245743669
##C: 3 28.274333882308138
##C: 1 3.141592653589793
##C: 1 3.141592653589793
##R: 1 3 3
##R: 4 1 4
##R: 2 6 12
##R: 6 4 24
##R: 8 6 48

from random import randrange, seed
import math
class Piece:
    def area(self):
        raise NotImplementedError

    def __lt__(self, other):
        if isinstance(self, Circle) and isinstance(other, Rectangle):
            ## add your code here
            return True
            
        elif isinstance(self, Circle) and isinstance(other, Circle):
            ## add your code here
            return self.area() > other.area()

        elif isinstance(self, Rectangle) and isinstance(other, Rectangle):
            ## add your code here
            return self.area() < other.area()

        else:
            ## add your code here
            return False
            
    def __str__(self):
        raise NotImplementedError
    
class Circle(Piece):
    def __init__(self, radius):
        ## add your code here
        self.radius = radius

    def area(self):
        return math.pi*self.radius*self.radius
    
    def __str__(self):
        ## add your code here
        return 'C' + ': ' + str(self.radius) + ' ' + str(self.area())

class Rectangle(Piece):
    def __init__(self, length, width):
        ## add your code here
        self.length = length
        self.width = width

    def area(self):
        ## add your code here
        return self.length * self.width

    def __str__(self):
        ## add your code here
        return 'R' + ': ' + str(self.length) + ' ' + str(self.width) + ' ' + str(self.area())

seed(15)

circles = [Circle(1 + randrange(10))  for i in range(5)] 

rectangles = [Rectangle(1 + randrange(10), 1 + randrange(10)) for i in range(5)]

pieces = circles + rectangles

for b in pieces:
    print(b)

print("---------------------------")
pieces.sort()
for b in pieces:
    print(b)
