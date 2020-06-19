import math
import random

class PVector():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set(self, v):
        self.x = v.x
        self.y = v.y
    
    def get(self):
        v = PVector(self.x, self.y)
        return(v)
    
    def add(self, v):
        self.x += v.x
        self.y += v.y
        
    def sub(self, v):
        self.x -= v.x
        self.y -= v.y
    
    # Multiplikation mit einem Skalar
    def mult(self, n):
        self.x *= n
        self.y *= n
    
    # Division durch einen Skalar
    def div(self, n):
        self.x /= n
        self.y /= n

    # Elementweise Multiplikation eines Vektor mit einem anderen Vektor
    def mult2(self, v):
        self.x *= v.x
        self.y *= v.y

    # Elementweise Division eines Vektor mit einem anderen Vektor
    def div2(self, v):
        self.x /= v.x
        self.y /= v.y

    # Magnitude
    def mag(self):
        return (math.sqrt(self.x*self.x + self.y*self.y))
    
    # Normalisierung
    def normalize(self):
        m = self.mag()
        if (m != 0):
            self.div(m)

    # Berechnung der euklidischen Distanz zwischen zwei Vektoren
    def dist(self, v):
        dx = self.x - v.x
        dy = self.y - v.y
        return (math.sqrt(dx*dx + dy+dy))
    
    # Berechnung des Skalarprodukts (inneren Produkts) eines Vektors
    def dot(self, v):
        return self.x*v.x + self.y*v.y
    
    # Begrenzt die Magnitude eines Vektors auf max
    def limit(self, max):
        if self.mag() > max:
            self.normalize()
            self.mult(max)
    
    # Berechnet den Winkel der Rotation eines Vektors
    def heading(self):
        angle = math.atan2(-self.y, self.x)
        return -1*angle

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        result = PVector(x, y)
        return(result)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        result = PVector(x, y)
        return(result)
    
    def __str__(self):
        return("[" + str(self.x) + ", " + str(self.y) + "]")
        
    @classmethod
    def random2D(cls):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        v = cls(x, y)
        v.normalize()
        return(v)
