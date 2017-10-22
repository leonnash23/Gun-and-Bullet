import pygame

from util.colors import Color


class Goal:
    def __init__(self, x, y, h, screen):
        self.x = x
        self.y = y
        self.h = h
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, Color.RED.value, [self.x, self.y - self.h, self.h, self.h])
