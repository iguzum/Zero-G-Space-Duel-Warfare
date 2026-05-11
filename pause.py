import pygame

class Pause:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.Font("assets/fonts/upheavtt.ttf", 60)
        self.background = pygame.image.load('assets/pics/others/background-menu.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.surface.get_width(), self.surface.get_height()))

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.show_options = True

    def draw(self):
        if self.show_options:
            self.surface.blit(self.background, (0,0))

            text_surface1 = self.font.render("GAME IS PAUSED!", True, self.WHITE)
            text_rect1 = text_surface1.get_rect(center=(self.surface.get_width() //2, self.surface.get_height() //2 - 100))
            self.surface.blit(text_surface1, text_rect1)
            
            text_surface2 = self.font.render("PRESS ESC OR BACKSPACE TO CONTINUE", True, self.WHITE)
            text_rect2 = text_surface1.get_rect(topleft=(self.surface.get_width() //2  - text_surface2.get_width() // 2, self.surface.get_height() // 2 - 80))
            self.surface.blit(text_surface2, text_rect2)
