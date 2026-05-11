import pygame

class Options:
    def __init__(self, surface):
        self.surface = surface
        self.size = (200, 75)
        self.toggle = True
        
        # States
        self.music_enabled = True
        self.sound_enabled = True
        
        self.music_on = self.load_and_scale('assets/pics/utils/music on.png', self.size)
        self.music_off = self.load_and_scale('assets/pics/utils/music off.png', self.size)
        self.sound_on = self.load_and_scale('assets/pics/utils/sound effects on.png', self.size)
        self.sound_off = self.load_and_scale('assets/pics/utils/sound effects off.png', self.size)
        
        self.music_rect = self.music_on.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() // 2))
        self.sound_rect = self.sound_on.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() // 2 + 100))
        
    def load_and_scale(self, file, size):
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img, (size))
        return img
    
    def draw(self):
        if not self.toggle:
            return
        
        self.text = pygame.font.Font('assets/fonts/upheavtt.ttf', 80).render("OPTIONS", True, (255, 255, 255))
        self.option = pygame.font.Font('assets/fonts/upheavtt.ttf', 60).render("[ ESC ] = BACK", True, (255, 0, 0))
        
        music_img = self.music_on if self.music_enabled else self.music_off
        sound_img = self.sound_on if self.sound_enabled else self.sound_off
        
        self.surface.blit(music_img, self.music_rect)
        self.surface.blit(sound_img, self.sound_rect)  
        self.surface.blit(self.text, ((self.surface.get_width() - self.text.get_width()) // 2, 100))
        self.surface.blit(self.option, ((self.surface.get_width() - self.option.get_width()) // 2, 180))
        
    def handle_event(self, event):
        if not self.toggle:
            return
        
        # ESC closes options
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.toggle = False
                return "BACK"

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = event.pos

                # Toggle music
                if self.music_rect.collidepoint(mouse_pos):
                    self.music_enabled = not self.music_enabled
                    return "MUSIC_TOGGLE"

                # Toggle sound effects
                if self.sound_rect.collidepoint(mouse_pos):
                    self.sound_enabled = not self.sound_enabled
                    return "SOUND_TOGGLE"