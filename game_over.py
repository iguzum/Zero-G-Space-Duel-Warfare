import pygame

class GameOver:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.Font('assets/fonts/upheavtt.ttf', 80)

    def draw(self, winner):
        if winner == "PLAYER 1 WINS":
            text = self.font.render("PLAYER 1 WINS", True, (255, 0, 0))
        else:
            text = self.font.render("PLAYER 2 WINS", True, (0, 0, 255))
        restart = pygame.font.Font('assets/fonts/upheavtt.ttf', 40).render("[ R ] = Restart : [ M ] = Menu", True, (255, 255, 255))
        self.surface.blit(text, ((self.surface.get_width() - text.get_width()) // 2, 250))
        self.surface.blit(restart, ((self.surface.get_width() - text.get_width()) // 2, 350))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                return "RESTART"
            if event.key == pygame.K_m:
                return "MENU"