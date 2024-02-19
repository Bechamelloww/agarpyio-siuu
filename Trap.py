import pygame
import random


class Trap(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.size = random.randint(40, 150)
        self.image = pygame.image.load("messitrap.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size * 2, self.size * 2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.place_randomly(screen_width, screen_height)

    def place_randomly(self, screen_width, screen_height):
        self.rect.x = random.randint(0, screen_width - self.size * 2)
        self.rect.y = random.randint(0, screen_height - self.size * 2)
