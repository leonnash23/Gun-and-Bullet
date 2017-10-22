import pygame

from model import goal
from util.colors import Color
from util.constants import Constants


class Bullet:
    def __init__(self, x, y, v, screen):
        self.x = x
        self.y = y
        self.v = [v[0] - x, v[1] - y]
        self.a = Constants.BULLET_BOOST.value
        self.screen = screen
        self.r = 2

    def move(self):
        self.x += self.v[0] / 10
        self.y += self.v[1] / 10
        self.__change_speed()

    def round_x(self):
        return round(self.x)

    def round_y(self):
        return round(self.y)

    def stop(self):
        self.v = [0, 0]
        self.a = [0, 0]

    def draw(self):
        pygame.draw.circle(self.screen, Color.GOLD.value, [self.round_x(), self.round_y()], self.r, self.r)

    def __change_speed(self):
        self.v = [self.v[0] - self.a[0], self.v[1] - self.a[1]]

    def is_touch(self, g: goal.Goal):
        if self.x + self.r > g.x and self.x - self.r < g.x + g.h and self.y + self.r > g.y - g.h and self.y - self.r < g.y:
            return True
