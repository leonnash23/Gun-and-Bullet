import math

import pygame

from util.constants import Constants
from util.colors import Color


class Gun:
    def __init__(self, x, y, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.end = [0, 0]

    def __normalize(self, arr):
        h = math.sqrt(arr[0] ** 2 + arr[1] ** 2)
        return [arr[0] / h, arr[1] / h]

    def calc_gun_end_position(self, mouse_pos):
        mouse_pos = [mouse_pos[0], mouse_pos[1] - self.screen.get_height() // 2]
        mouse_pos = self.__normalize(mouse_pos)
        mouse_pos = [round(mouse_pos[0] * Constants.GUN_LENGTH.value),
                     self.screen.get_height() // 2 + round(mouse_pos[1] * Constants.GUN_LENGTH.value)]
        if mouse_pos[1] > self.screen.get_height() // 2:
            mouse_pos = [Constants.GUN_LENGTH.value, self.screen.get_height() // 2]
        self.end = mouse_pos

    def draw(self):
        pygame.draw.line(self.screen, Color.BLACK.value, [0, self.screen.get_height() // 2], self.end, 5)
