import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)

class Button(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, text):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.text = text
        font = pg.font.Font(None, 36)
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surface, text_rect)

    def update(self):
        pass

class Squere(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def fill(self, color):
        self.image.fill(color)
        pass

    def isColliding(self, rectangle):
        if self.rect.colliderect(rectangle):
            return True
        pass



