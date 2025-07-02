# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

# Player Class - Represents the Player's Spaceship
class Player(CircleShape):
    
    # Initializes Player's Position, Size, Rotation, and Shoot Cooldown Timer
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0  # Time remaining until the player can shoot again

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
        
    # Spawns a Shot Moving in the Direction the Player is Facing, with Cooldown Check
    def shoot(self):
        if self.shoot_timer > 0:
            return  # Too soon to shoot again
    
        shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.velocity = velocity
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        
    # Handles Player Input for Movement, Rotation, Shooting, and Updates Cooldown Timer
    def update(self, dt):
        self.shoot_timer -= dt
        if self.shoot_timer < 0:
            self.shoot_timer = 0
            
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
