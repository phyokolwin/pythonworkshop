class Polygon():
    """A class to capture common utilities for dealing with shapes"""
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths
        
    def __str__(self):
        return 'Polygon with %s sides' % self.num_sides 
        
    @property
    def num_sides(self):
        return len(self.side_lengths)
        
    @property
    def perimeter(self):
        return sum(self.side_lengths)

class Rectangle(Polygon):
    def __init__(self, height, width):
        super().__init__([height, width, height, width])

    @property
    def area(self):
        return self.side_lengths[0] * self.side_lengths[1]

r = Rectangle(1, 5)
r.area, r.perimeter

class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)

s = Square(5)
s.area, s.perimeter
