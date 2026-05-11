import pygame

class Timer:
    def __init__(self, surface, ccp):
        self.surface = surface
        self.ccp = ccp
        self.font = pygame.font.Font('assets/fonts/upheavtt.ttf', 30)

        self.restart()

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = pygame.time.get_ticks() - self.elapsed_time

    def pause(self):
        if self.running:
            self.running = False
            self.elapsed_time = pygame.time.get_ticks() - self.start_time

    def restart(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.round_num = 1
        self.times = []
        self.next_trigger = 20000

    def update(self):
        if self.running:
            current_time = pygame.time.get_ticks()
            self.elapsed_time = current_time - self.start_time

            if self.elapsed_time >= self.next_trigger:
                self.ccp.generate_event()
                self.times.append(f"Round {self.round_num} {self.ccp.effect_name}")
                self.round_num += 1
                self.next_trigger += 20000

    def draw(self):
        seconds = self.elapsed_time / 1000

        timer_text = self.font.render(f"Timer : {seconds:.2f} s", True, (255, 255, 255))
        self.surface.blit(timer_text, (self.surface.get_width() // 2 - 250, 20))

        if self.times:
            small_text = self.font.render(self.times[-1], True, (255, 255, 255))
            self.surface.blit(small_text, (self.surface.get_width() // 2 + 30, 20))