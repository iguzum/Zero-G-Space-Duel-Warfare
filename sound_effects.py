import pygame

class SoundEffects:
    def __init__(self, file, volume=1.0):
        self.file = file
        self.sound = pygame.mixer.Sound(self.file)
        self.sound.set_volume(volume)

    def play(self, loop=True):
        if loop:
            self.sound.play(-1)
        else:
            self.sound.play()

    def stop(self):
        self.sound.stop()

    def pause(self):
        self.sound.pause()

    def unpause(self):
        self.sound.unpause()

    def set_volume(self, volume):
        self.sound.set_volume(volume)