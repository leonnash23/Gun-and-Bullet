import random

import pygame

from model import bullet, goal, gun
from util import colors
from util.constants import Constants

score = 0
bullets_losted = 0
bullets = []


def draw_stick_figure(screen, x, y):
    pygame.draw.rect(screen, colors.Color.BLACK.value, [x, y - 10, x + 10, y])


def draw_score(screen, x, y):
    font = pygame.font.Font(None, Constants.FONT_SIZE.value)
    text = font.render("Killed: " + str(score), True, colors.Color.BLACK.value)
    screen.blit(text, [x, y])
    text = font.render("Bullets used: " + str(bullets_losted), True, colors.Color.BLACK.value)
    screen.blit(text, [x, y + Constants.FONT_SIZE.value])


def create_goal(screen):
    return goal.Goal(random.Random().randint(50, screen.get_width()), screen.get_height() // 2,
                     Constants.GOAL_SIZE.value, screen)


def create_bullet(screen, gun):
    global bullets_losted
    if len(bullets) >= Constants.MAX_BULLET_COUNT.value:
        bullets.pop(0)
    bullets.append(bullet.Bullet(0, screen.get_height() // 2, gun.end, screen))
    bullets_losted += 1


pygame.init()
screen = pygame.display.set_mode([Constants.SCREEN_WIDTH.value, Constants.SCREEN_HEIGHT.value])
pygame.display.set_caption(Constants.WINDOW_CAPTION.value)
clock = pygame.time.Clock()
goal_one = None
gun = gun.Gun(0, 0, screen)
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEMOTION:
            end = gun.calc_gun_end_position(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN:
            create_bullet(screen, gun)

    for bullet_one in bullets:
        bullet_one.move()
        if bullet_one.round_y() > screen.get_height() // 2:
            bullet_one.y = screen.get_height() // 2
            bullet_one.stop()
        if bullet_one.is_touch(goal_one):
            score += 1
            goal_one = create_goal(screen)
    if goal_one is None:
        goal_one = create_goal(screen)

    screen.fill(colors.Color.WHITE.value)
    gun.draw()
    pygame.draw.line(screen, colors.Color.BLACK.value, [0, screen.get_height() // 2],
                     [screen.get_width(), screen.get_height() // 2], 1)
    draw_score(screen, 10, 10)
    for bullet_one in bullets:
        bullet_one.draw()
    if goal_one is not None:
        goal_one.draw()

    pygame.display.flip()
    clock.tick(Constants.GAME_SPEED.value)
pygame.quit()
