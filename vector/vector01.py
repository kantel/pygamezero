import pygame.math as math

test = math.Vector2(200, 200)
print(test.x)
print(test.y)

PositionA = math.Vector2(200,200)
PositionB = math.Vector2(500,300)
Distance = PositionB - PositionA
print(Distance)
print(type(Distance))

Position= math.Vector2(200,200)
Movement = math.Vector2(1,1)
Position += Movement
print(Position)

Position= math.Vector2(200,200)
Movement *= 2
print(Movement)
