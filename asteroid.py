# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from circleshape import CircleShape

# Asteroid Class - Represents an Asteroid Moving Across the Screen
class Asteroid(CircleShape):
    
    # Initializes Asteroid's Position and Size
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    # Draws the Asteroid as a White Circle Outline on the Screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    # Updates Asteroid's Position Based on Its Current Velocity
    def update(self, dt):
        self.position += self.velocity * dt
