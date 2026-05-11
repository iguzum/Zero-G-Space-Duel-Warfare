import pygame
from GIF import GIF
from player import Player
from sound_effects import SoundEffects
from timer import Timer
from Cosmic_Chaos_Protocol import CCP

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background_image = GIF("assets/pics/others/green_planet.gif")
        self.font = pygame.font.Font("assets/fonts/upheavtt.ttf", 35)
        self.hit_sound_effects = SoundEffects("assets/music/hit_sound_effects.wav", 0.7)
        self.shoot_sound_effects = SoundEffects("assets/music/shoot_sound_effects.wav", 0.7)

        # Initial objects
        self.border = pygame.Rect(self.surface.get_width() //2, 0, 3, self.surface.get_height())
        
        self.player1 = Player(50, self.surface.get_height() // 2, self.surface, "P1", self.border)
        self.player2 = Player(self.surface.get_width() - 50, self.surface.get_height() // 2, self.surface, "P2", self.border)
        

        self.ccp = CCP(self.player1, self.player2, self.surface, self.border)
        self.timer = Timer(self.surface, self.ccp)
        self.update_health()
        

    def reset(self):
        self.player1 = Player(50, self.surface.get_height() // 2, self.surface, "P1", self.border)
        self.player2 = Player(self.surface.get_width() - 50, self.surface.get_height() // 2, self.surface, "P2", self.border)
        self.ccp = CCP(self.player1, self.player2, self.surface, self.border)

        # Reuse timer
        self.timer.ccp = self.ccp
        self.timer.restart()
        self.update_health()

    def update(self):
        self.player1.update()
        self.player2.update()

        for bullet in self.player1.bullets:
            if pygame.sprite.collide_rect(bullet, self.player2):
                self.player2.health -= self.player1.damage
                bullet.kill()
                self.hit_sound_effects.play(loop=False)

        for bullet in self.player2.bullets:
            if pygame.sprite.collide_rect(bullet, self.player1):
                self.player1.health -= self.player2.damage
                bullet.kill()
                self.hit_sound_effects.play(loop=False)

        self.update_health()
        self.ccp.update()

        if self.player1.health <= 0:
            return 'PLAYER 2 WINS'
        elif self.player2.health <= 0:
            return 'PLAYER 1 WINS'

    def draw(self):
        self.background_image.draw(self.surface)

        pygame.draw.rect(self.surface, (255, 255, 255), self.border)

        self.player1.draw(self.surface)
        self.player2.draw(self.surface)

        self.surface.blit(self.p1_health_text, (20, 650))
        self.surface.blit(self.p2_health_text, (1080, 650))

    def update_health(self):
        self.p1_health_text = self.font.render(f"HP : {self.player1.health}", True, (255, 255, 255))
        self.p2_health_text = self.font.render(f"HP : {self.player2.health}", True, (255, 255, 255))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                self.player1.shoot()
                self.shoot_sound_effects.play(loop=False)

            if event.key == pygame.K_RCTRL:
                self.player2.shoot()
                self.shoot_sound_effects.play(loop=False)

            if event.key == pygame.K_ESCAPE:
                return "PAUSED"
            
            if event.key == pygame.K_BACKSPACE:
                return "RESUMED"