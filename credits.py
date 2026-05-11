import pygame

class Credits:
    def __init__(self, screen_surface):
        self.display = screen_surface
        self.width, self.height = screen_surface.get_size()
        
        self.main_font = pygame.font.Font('assets/fonts/upheavtt.ttf', 35)
        self.small_font = pygame.font.Font('assets/fonts/upheavtt.ttf', 25)
        self.escape_instruction = self.small_font.render("Press ESC to return to Menu", True, (255, 255, 255))
        self.background = pygame.image.load('assets/pics/others/background-menu.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        
        self.bright_red = (255, 0, 0)
        self.pure_white = (255, 255, 255)
        self.soft_gray = (180, 180, 180)
        self.footer_color = (20, 20, 20)

        self.script = [
            "----- ZERO-G SPACE DUEL WARFARE -----",
            "",
            "About the Game",
            "The game is a fast-paced 2D zero-gravity space battle",
            "Two spaceships face each other in an intense duel arena",
            "Players must move, dodge, and attack while drifting through space",
            "Quick reflexes and accurate shooting are the keys to survival",
            "Only the last spaceship standing wins the battle",
            "",
            "Cosmic Chaos Protocol",
            "Every 20 seconds, random power-ups appear across the arena",
            "These power-ups can change the flow of the fight instantly",
            "Players may gain rapid fire, double damage, health recovery, etc.",
            "One player can gain the advantage while the other struggles to survive",
            "The battlefield becomes more chaotic as both players adapt",
            "",
            "LEGAL NOTICE",
            "The spaceships assets in this game were created by our group",
            "However the backgrounds and audio were sourced from the interet",
            "All external assets are credited to their original creators",
            "We do not claim ownership of any third-party audio and images",
            "This game is for educational and non-commercial purposes only"
            "", "",
            "< DEVELOPERS />",
            "",
            "Capinding, Mark Jay",
            "Lead Programmer",
            "",
            "Apellido, Rich Ashley",
            "Lead Designer",
            "",
            "Diola, Jorrenz",
            "Mondreal, Prince Jade",
            "Langit, Christian",
            "Estacio, Romeo Claro",
            "Assistant / Members",
        ]
        
        self.y_pos = self.height
        self.scroll_speed = 1.5
        self.line_height = 50
        
    def draw(self):
        self.display.blit(self.background, (0, 0))
        dark_overlay = pygame.Surface((self.width, self.height))
        dark_overlay.set_alpha(80) # Opacity yan
        dark_overlay.fill((0, 0, 0))
        self.display.blit(dark_overlay, (0, 0))
        
        current_y = self.y_pos
        
        for line in self.script:
            upper_line = line.upper()
            
            is_name = any(name in upper_line for name in ["CAPINDING", "APELLIDO", "DIOLA", "MONDREAL", "LANGIT", "ESTACIO"])
            is_label = any(label in upper_line for label in ["LEGAL NOTICE", "COSMIC CHAOS PROTOCOL", "ABOUT THE GAME", "-----"])
            is_role = any(label in upper_line for label in ["LEAD PROGRAMMER", "LEAD DESIGNER", "ASSISTANT / MEMBERS"])
            if is_name or is_label:
                active_font = self.main_font
            else:
                active_font = self.small_font
            
            if ":" in line or "-----" in line or is_label:
                text_color = self.bright_red
            elif is_name:
                text_color = self.pure_white
            elif is_role:
                text_color = self.soft_gray
            else:
                text_color = self.pure_white
            
            text_surface = active_font.render(line, True, text_color)
            
            center_x = (self.width // 2) - (text_surface.get_width() // 2)
            self.display.blit(text_surface, (center_x, current_y))
            
            current_y += self.line_height

        self.y_pos -= self.scroll_speed
        
        total_content_height = len(self.script) * self.line_height
        if self.y_pos < -total_content_height:
            self.y_pos = self.height

        pygame.draw.rect(self.display, self.footer_color, (0, self.height - 40, self.width, 40))
        
        footer_text = "PROGRAMMING 2 FINAL PROJECT"
        footer_surface = self.small_font.render(footer_text, True, self.pure_white)
        footer_x = (self.width // 2) - (footer_surface.get_width() // 2)
        
        self.display.blit(footer_surface, (footer_x, self.height - 30))
        self.display.blit(self.escape_instruction, (10, 10))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.y_pos = self.height
                return "MENU"
        return None