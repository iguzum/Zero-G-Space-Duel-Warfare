import pygame
import sys
from sound_effects import SoundEffects
from menu import Menu
from game import Game
from pause import Pause
from game_over import GameOver
from options import Options
from credits import Credits

class Main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # INIT ONCE ONLY

        self.WIDTH, self.HEIGHT = 1200, 700
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Zero-G Space Duel Warfare")
        
        self.ICON = pygame.image.load("assets/pics/others/icon.png").convert_alpha()
        pygame.display.set_icon(self.ICON)

        self.CLOCK = pygame.time.Clock()
        self.running = True
        self.winner = None

        # Create ONCE
        self.menu = Menu(self.SCREEN)
        self.game = Game(self.SCREEN)
        self.game_over = GameOver(self.SCREEN)
        self.pause = Pause(self.SCREEN)
        self.options = Options(self.SCREEN)
        self.credits = Credits(self.SCREEN)
        self.background_music = SoundEffects("assets/music/background.mp3", volume=1.0)
        self.background_music.play(loop=True)

        self.current_state = "MENU"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.current_state == "MENU":
                choice = self.menu.handle_event(event)
                if choice == "START":
                    self.game.reset()
                    self.game.timer.start()
                    self.current_state = "GAME"
                elif choice == "OPTIONS":
                    self.current_state = "OPTIONS"
                elif choice == "CREDITS":
                    self.current_state = "CREDITS"                    
                elif choice == "EXIT":
                    self.running = False
                    
            elif self.current_state == "OPTIONS":
                option = self.options.handle_event(event)
                if option == "BACK":
                    self.current_state = "MENU"
                    self.options.toggle = True  # Reset toggle for next timedm
                elif option in ["MUSIC_TOGGLE", "SOUND_TOGGLE"]:
                    self.apply_audio_settings()
            
            elif self.current_state == "CREDITS":
                state = self.credits.handle_event(event)
                if state == "MENU":
                    self.current_state = "MENU"
                    
            elif self.current_state == "GAME":
                state = self.game.handle_event(event)
                
                if state == "PAUSED":
                    self.current_state = "PAUSE"
                    self.game.timer.pause()

            elif self.current_state == "PAUSE":
                state = self.game.handle_event(event)

                if state == "RESUMED":
                    self.current_state = "GAME"
                    self.game.timer.start()
                        
            elif self.current_state == "GAME_OVER":
                user = self.game_over.handle_event(event)
                if user == "RESTART":
                    self.game.reset()
                    self.game.timer.start()
                    self.current_state = "GAME"
                elif user == "MENU":
                    self.game.reset()
                    self.current_state = "MENU"

    def apply_audio_settings(self):
        self.background_music.set_volume(1.0 if self.options.music_enabled else 0)
        volume = 0.7 if self.options.sound_enabled else 0
        self.game.hit_sound_effects.set_volume(volume)
        self.game.shoot_sound_effects.set_volume(volume)

    def update(self):
        if self.current_state == "GAME":
            result = self.game.update()
            self.game.timer.update()
            if result:
                self.winner = result
                self.current_state = "GAME_OVER"

    def draw(self):
        self.SCREEN.fill((0, 0, 0))

        if self.current_state == "MENU":
            self.menu.draw()
        elif self.current_state == "GAME":
            self.game.draw()
            self.game.timer.draw()
        elif self.current_state == "OPTIONS":
            self.options.draw()
        elif self.current_state == "CREDITS":
            self.credits.draw()
        elif self.current_state == "PAUSE":
            self.pause.draw()
        elif self.current_state == "GAME_OVER":
            self.game_over.draw(self.winner)

        pygame.display.update()

    def run(self):
        while self.running:
            self.CLOCK.tick(60)
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Main().run()