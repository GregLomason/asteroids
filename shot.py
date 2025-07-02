# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

# Shot Class - Represents the Bullet
class Shot(CircleShape):
    
    #Initialization - starts the shot's position and size
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    # Drawing Logic - draws the "shot" as a white circle outline on the screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    # Movement Updating - updates the shot's position based on it current velocity
    def update(self, dt):
        self.position += self.velocity * dt