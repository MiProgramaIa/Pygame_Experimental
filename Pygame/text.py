import pygame as pg

class Text:
    def __init__(self, x, y, text, font_size, font_color):
        self.font = pg.font.Font(None, font_size)
        self.font_color = font_color
        self.text = text
        self.image = self.font.render(text, True, font_color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def set_text(self, text):
        self.text = text
        self.image = self.font.render(text, True, self.font_color)