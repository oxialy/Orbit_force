
from src import settings as sett
from src import game_variables as GV
from src import drawing_variables as dv
from src import msc, logs

from .drawing_variables import bg_color, colors
from .settings import WIDTH, HEIGHT, FONT15, FONT20, FONT25, FONT12, FONT22, FONT10


import pygame
import random
from random import randrange, choice


def draw_test(win):
    def write_words(n):
        for i in range(n):
            word = 'non' * i
            write_text()
    p1 = GV.planets[0]

    write_text(win, len(p1.path), (WIDTH - 40, 40))


def draw_screen(win):
    win.fill(bg_color)

    draw_elem(win, GV.planets)

    draw_test(win)


def draw_elem(win, elements):
    for elem in elements:
        elem.draw(win)



def write_text(win, data, pos, col=colors['grey1'], font=FONT20, center=False, resize_limit=0):
    #font = pygame.font.SysFont('arial', 30)

    text_surf = font.render(str(data), 1, col)
    size = text_surf.get_size()

    if resize_limit != 0 and size[0] > resize_limit:
        text_surf = sett.FONT15.render(str(data), 1, col)
        size = text_surf.get_size()

    if center:
        x = pos[0] - size[0] // 2
        y = pos[1] - size[1] // 2
    else:
        x, y = pos

    win.blit(text_surf, (x,y))
















