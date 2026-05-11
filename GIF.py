import pygame
from PIL import Image

class GIF:
    def __init__(self, filename):
        self.frames = []
        self.index = 0
        self.load_gif(filename)

    def load_gif(self, filename):
        img = Image.open(filename)
        for i in range(img.n_frames):
            img.seek(i)
            frame = img.convert('RGB')
            frame = pygame.image.fromstring(frame.tobytes(), frame.size, 'RGB')
            self.frames.append(frame)
            
    def draw(self, surface):
        # Scale dynamically to screen size
        frame = self.frames[self.index % len(self.frames)]
        frame = pygame.transform.scale(frame, surface.get_size())
        surface.blit(frame, (0, 0))
        self.index += 1
