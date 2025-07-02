# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    
    #Initialization
    def __init__(self, x, y, radius):
        
        # Handle container assignment if applicable
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        # Position and Movement
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
   
    # Collision Detection
    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
    
    # Placeholder for Drawing Logic
    def draw(self, screen):
        # sub-classes must override
        pass
    # Placeholder for Update Logic
    def update(self, dt):
        # sub-classes must override
        pass