import pygame
import random


class Food(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.size = 40
        self.image = pygame.image.load("cristiano.png")
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.place_randomly(screen_width, screen_height)

    def place_randomly(self, screen_width, screen_height):
        self.rect.x = random.randint(0, screen_width - self.size)
        self.rect.y = random.randint(0, screen_height - self.size)
