import pygame

class Button:
    def __init__(self, text, x, y, width, height, image):
        self.text = text
        self.font = pygame.font.Font("assets/fonts/upheavtt.ttf", 40)
        self.button_rect = pygame.Rect(x, y, width, height)
        
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=self.button_rect.center)
        
    def draw(self, surface):
        surface.blit(self.image, self.button_rect)
        surface.blit(self.text_surface, self.text_rect)