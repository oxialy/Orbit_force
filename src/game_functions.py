from src import drawing_variables as dv
from src import game_variables as GV
from src import settings as sett
from src import msc

from .drawing_variables import colors
from .settings import WIDTH, HEIGHT, FONT20, FONT22, FONT25, FONT30

import pygame
import math
import random

from pygame import Vector2
from math import sqrt
from random import randrange, choice, shuffle



def center_rect(rect):
    x, y, w, h = rect

    x2 = x - w//2
    y2 = y - h//2
    new_rect = pygame.Rect(x2, y2, w, h)

    return new_rect


def get_dist(A, B):
    x1, y1 = A
    x2, y2 = B

    return sqrt((x2-x1)**2 + (y2-y1)**2)


def reset_pos(planets):
    center = WIDTH / 2, HEIGHT / 2
    offset = msc.get_dist(GV.p1.pos, center)
    angle = msc.get_angle(GV.p1.pos, center)

    pos = msc.get_point_from_angle((0,0), angle, offset)
    vec = Vector2(pos)


    for planet in planets:
        planet.pos += vec













