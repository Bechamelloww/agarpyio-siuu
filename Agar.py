import pygame


class Agar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.size = 40
        animated_image = pygame.image.load("ball.gif")
        animated_image = pygame.transform.scale(animated_image, (self.size * 2, self.size * 2))
        self.image = animated_image.convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.width = self.size * 2
        self.rect.height = self.size * 2
        self.score = 0
        self.speed = 100
        self.rect.x -= self.size - self.size/2
        self.rect.y -= self.size - self.size/2

    def increase_speed(self):
        if self.speed < 500:
            self.speed += 5

    def increase_size(self):
        if self.size < 200:
            self.size += 2
            animated_image = pygame.image.load("ball.gif")
            animated_image = pygame.transform.scale(animated_image, (self.size * 2, self.size * 2))
            self.image = animated_image.convert_alpha()
            self.rect = self.image.get_rect(center=self.rect.center)

    def collidetrap(self, trap_size_multiplier):
        self.size /= trap_size_multiplier
        self.speed /= trap_size_multiplier
        animated_image = pygame.image.load("ball.gif")
        animated_image = pygame.transform.scale(animated_image, (self.size * 2, self.size * 2))
        self.image = animated_image.convert_alpha()
        self.rect = self.image.get_rect(center=self.rect.center)