from src import drawing_variables as DV
from src import game_functions as GF
from src import settings as sett
from src import msc

from .drawing_variables import colors
from .settings import WIDTH, HEIGHT
from .planet import Planet


import pygame


p1 = Planet((300,300), 8)

orbit_1 = p1.init_orbit()

planets = [p1]
orbits = orbit_1
objects = [p1] + orbit_1


TOGGLE_PATH = True


questions = [
    {'title': 1, 'answers': [1,2,3]},
    {'title': 2, 'answers': [1,2,3]},
    {'title': 3, 'answers': [1,2,3]}
]


def gradient_colors(col_1, col_2):
    r1, g1, b1 = col_1
    r2, g2, b2 = col_2












