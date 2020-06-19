from pvector import PVector

WIDTH = 400
HEIGHT = 400

class Ball():
    
    def __init__(self, x, y, v_x, v_y, radius, color):
        self.position = PVector(x, y)
        self.radius = radius
        self.color = color
        self. velocity = PVector(v_x, v_y)
    
    def show(self, screen):
        screen.draw.filled_circle((self.position.x, self.position.y), self.radius, self.color)
    
    def move(self):
        self.position.add(self.velocity)
    
        if (self.position.x > WIDTH - self.radius) or (self.position.x < self.radius):
            self.velocity.x *= -1
        if (self.position.y > HEIGHT - self.radius) or (self.position.y < self.radius):
            self.velocity.y *= -1