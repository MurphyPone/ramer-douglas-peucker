import math

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y  

    # returns the magnitude of the vector
    def mag(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    # normalizes the vector
    def norm(self):
        m = self.mag()
        if(m != 0):
            self.x = self.x/m
            self.y = self.y/m

    # scales self by n
    def mult(self, n):
        self.x *= n
        self.y *= n

    # returns the dot product of n with self
    def dot(self, n):
        return (self.x * n.x) + (self.y * n.y)

    # string representation
    def __str__(self):
        return f"({self.x}, {self.y})"


# vector subtraction
def sub(a, b):
    return Vector(a.x - b.x, a.y - b.y)


# vector addition
def add(a, b):
    return Vector(a.x + b.x, a.y + b.y)


# distance between two vectors a, b
def dist(a, b):
    return math.sqrt((b.x-a.x)**2 + (b.y-a.y)**2)


# finds the scalar projection of p onto the line formed by a,b
def scalar_proj(p, a, b):
    ap = sub(p, a)
    ab = sub(b, a)
    ab.norm()
    ab.mult(ap.dot(ab))
    return add(a, ab)


# calculates the distance from point c to the line formed by a,b
def dist_from_line(c, a, b):
    normal_pt = scalar_proj(c, a, b)
    return dist(c, normal_pt)


