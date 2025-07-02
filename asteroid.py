# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


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
        
    # Allows Asteroids to split into smaller pieces
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Calculate the properties of the smaller asteroids
        random_angle = random.uniform(20, 50)
        velocity_1 = self.velocity.rotate(random_angle) * 1.2
        velocity_2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
    
        # Spawn TWO smaller asteroids
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
    
        asteroid_1.velocity = velocity_1
        asteroid_2.velocity = velocity_2