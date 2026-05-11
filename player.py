import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, surface, type, border):
        super().__init__()
        self.SCREEN_WIDTH = surface.get_width()
        self.SCREEN_HEIGHT = surface.get_height()
        self.type = type
        self.border = border
        self.damage = 1
        self.MOVE_SPEED = 7
        self.health = 10
        self.last_health = self.health
        self.HIT_INDEX = 3
        self.hit = False
        self.hit_time = 0
        self.hit_duration = 1000 # 1 second
        self.inverted_controls = False
        
        # BULLETS
        self.bullet_speed = 10
        self.bullets = pygame.sprite.Group()
        self.max_bullets = 10

        def load_and_scale(path, size):
            img = pygame.image.load(path).convert_alpha()
            return pygame.transform.scale(img, size)

        # IMAGES
        self.p1_images = [
            load_and_scale('assets/pics/player1/Red Base.png', (70, 50)),
            load_and_scale('assets/pics/player1/Red Up.png', (70, 50)),
            load_and_scale('assets/pics/player1/Red Down.png', (70, 50)),
            load_and_scale('assets/pics/player1/Red Hit.png', (70, 50))
        ]

        self.p2_images = [
            load_and_scale('assets/pics/player2/Blue Base.png', (70, 50)),
            load_and_scale('assets/pics/player2/Blue Up.png', (70, 50)),
            load_and_scale('assets/pics/player2/Blue Down.png', (70, 50)),
            load_and_scale('assets/pics/player2/Blue Hit.png', (70, 50))
        ]

        # DEFAULT IMAGE
        self.image = self.p1_images[0] if type == "P1" else self.p2_images[0]
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

    # SHOOT
    def shoot(self):
        if len(self.bullets) < self.max_bullets:
            if self.type == "P1":
                bullet = Bullet(self.rect.centerx + 30, self.rect.centery, 1, self.bullet_speed, "P1")
            else:
                bullet = Bullet(self.rect.centerx - 30, self.rect.centery, -1, self.bullet_speed, "P2")
            self.bullets.add(bullet)

    # UPDATE
    def update(self):
        self.handle_movement()
        self.mask = pygame.mask.from_surface(self.image)

        # Update bullets
        self.bullets.update(self.SCREEN_WIDTH)

        # Detect health drop
        if self.health < self.last_health:
            self.hit = True
            self.hit_time = pygame.time.get_ticks()
            self.last_health = self.health
            

        # End hit state after 1 second
        if self.hit:
            if pygame.time.get_ticks() - self.hit_time > self.hit_duration:
                self.hit = False

    # DRAW
    def draw(self, screen):
        if self.hit:
            screen.blit(self.p1_images[self.HIT_INDEX] if self.type == "P1" else self.p2_images[self.HIT_INDEX], self.rect)
        else:
            screen.blit(self.image, self.rect)
        self.bullets.draw(screen)
        
    # MOVEMENT
    def handle_movement(self):
        key = pygame.key.get_pressed()
        speed = self.MOVE_SPEED

        # PLAYER 1 KEYS
        if self.type == "P1":

            up = pygame.K_w
            down = pygame.K_s
            left = pygame.K_a
            right = pygame.K_d

            # INVERT CONTROLS
            if self.inverted_controls:
                up, down = down, up
                left, right = right, left

        # PLAYER 2 KEYS
        else:
            up = pygame.K_i
            down = pygame.K_k
            left = pygame.K_j
            right = pygame.K_l

            # INVERT CONTROLS
            if self.inverted_controls:
                up, down = down, up
                left, right = right, left

        # Prevent opposite keys
        if (key[up] and key[down]) or (key[left] and key[right]):
            speed = 0

        # Diagonal slower
        if (key[up] and key[left]) or (key[up] and key[right]) or \
        (key[down] and key[left]) or (key[down] and key[right]):
            speed = 5

        # UP
        if key[up] and self.rect.top > 5:
            self.rect.y -= speed
            self.image = self.p1_images[1] if self.type == "P1" else self.p2_images[1]

        # DOWN
        if key[down] and self.rect.bottom < self.SCREEN_HEIGHT - 5:
            self.rect.y += speed
            self.image = self.p1_images[2] if self.type == "P1" else self.p2_images[2]

        # LEFT
        if key[left]:
            if self.type == "P1":
                if self.rect.left > 5:
                    self.rect.x -= speed
            else:
                if self.rect.left > self.border.right + 5:
                    self.rect.x -= speed

            self.image = self.p1_images[0] if self.type == "P1" else self.p2_images[0]

        # RIGHT
        if key[right]:
            if self.type == "P1":
                if self.rect.right < self.border.left - 5:
                    self.rect.x += speed
            else:
                if self.rect.right < self.SCREEN_WIDTH - 5:
                    self.rect.x += speed

            self.image = self.p1_images[0] if self.type == "P1" else self.p2_images[0]