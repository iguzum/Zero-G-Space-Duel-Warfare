import pygame
import sys
from GIF import GIF
from button import Button

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.gif = GIF("assets/pics/others/background.gif")
        self.buttons = []
        self.background_image = "assets/pics/others/button.png"
        self.spacing = 15
        self.spacing = int(self.spacing * 1.5)
        self.button_width = 250
        self.button_height = 100
        self.pos_x = (self.surface.get_width() // 2) + 250
        self.pos_y = (self.surface.get_height() // 2) - 200
        self.title_font = pygame.font.Font("assets/fonts/upheavtt.ttf", 75)
        self.rendered_title = self.title_font.render("ZERO-G Space Duel Warfare", True, (255, 255, 255))
        self.create_button()
        
    def create_button(self):
        labels = ["START", "OPTIONS", "CREDITS", "EXIT"]
        for i, text in enumerate(labels):
            y = self.pos_y + i * (self.button_height + self.spacing)
            self.buttons.append(Button(text,self.pos_x, y, self.button_width, self.button_height, self.background_image))
            
    def draw(self):
        self.gif.draw(self.surface)
        for button in self.buttons: 
            button.draw(self.surface)
        self.surface.blit(self.rendered_title, ((self.surface.get_width() - self.rendered_title.get_width()) // 2, 20))
            
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.button_rect.collidepoint(pos):
                    if button.text == "START":
                        return "START"
                    elif button.text == "OPTIONS":
                        return "OPTIONS"
                    elif button.text == "CREDITS":
                        return "CREDITS"
                    elif button.text == "EXIT":
                        pygame.quit()
                        sys.exit()