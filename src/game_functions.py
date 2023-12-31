from src import drawing_variables as dv
from src import settings as sett
from src import msc

from .drawing_variables import colors
from .settings import FONT20, FONT22, FONT25, FONT30, FONT35, FONT40

import pygame
import math
import random
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




