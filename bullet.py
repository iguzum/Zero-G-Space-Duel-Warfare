import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, type):
        super().__init__()
        self.image = pygame.Surface((20, 5))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.type = type
        self.direction = direction
        
        if type == "P1":
            self.image.fill((255, 0 ,0 ))
        else:
            self.image.fill((0, 0, 255)) 

    def update(self, screen_width):
        self.rect.x += self.speed * self.direction

        # Remove if off screen
        if self.rect.right < 0 or self.rect.left > screen_width:
            self.kill()