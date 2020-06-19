from pvector import PVector
import pgzrun
# from pgzero import Actor

WIDTH = 400
HEIGHT = 400

class Ball(Actor):
    
    def __init__(self, x, y, v_x, v_y, radius, image):
        super().__init__(self, image)
        self.radius = radius
        self.position = PVector(x, y)
        self. velocity = PVector(v_x, v_y)
    
    def show(self):
        self.draw()
    
    def move(self):
        self.position.add(self.velocity)
    
        if (self.position.x > WIDTH - RADIUS) or (self.position.x < RADIUS):
            self.velocity.x *= -1
        if (self.position.y > HEIGHT - RADIUS) or (self.position.y < RADIUS):
            self.velocity.y *= -1