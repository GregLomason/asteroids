# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED

# Player Class - Represents the Player's Spaceship
class Player(CircleShape):
    
    # Initializes Player's Position, Size, and Rotation
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # Calculates the Three Points of the Triangle Representing the Ship
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Draws the Player as a White Triangle on the Screen
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    # Rotates the Player Left or Right Based on Input
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    # Moves the Player Forward or Backward Based on Input
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    # Spawns a Shot Moving in the Direction the Player is Facing
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.velocity = velocity

    # Handles Player Input for Movement, Rotation, and Shooting
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
