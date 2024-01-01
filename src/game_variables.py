from src import drawing_variables as DV
from src import game_functions as GF
from src import settings as sett
from src import msc

from .drawing_variables import colors
from .settings import WIDTH, HEIGHT
from .planet import Planet


import pygame


def gradient_colors(col_1, col_2):
    n = 10

    r1, g1, b1 = col_1
    r2, g2, b2 = col_2

    k_r = (r2 - r1) / n
    k_g = (g2 - g1) / n
    k_b = (b2 - b1) / n

    path_1 = []

    for i in range(n):
        r = int(i * k_r + r1)
        g = int(i * k_g + g1)
        b = int(i * k_b + g1)

        path_1.append((int(r), int(g), int(b)))

    path_2 = path_1[::-1]

    path_3 = [col_1 for _ in range(25)]
    path_4 = [col_2 for _ in range(25)]
    
    col_path = path_3 + path_1 + path_4 + path_2

    return col_path


start_col = 60,60,60
end_col = 190,190,190
COL_PATH_1 = gradient_colors(start_col, end_col)


p1 = Planet((300,300), 8)
p1.col_path = COL_PATH_1

orbit_1 = p1.init_orbit()

orbit_1[0].col_path = COL_PATH_1
orbit_1[1].col_path = COL_PATH_1

planets = [p1]
orbits = orbit_1
objects = [p1] + orbit_1


TOGGLE_PATH = True


questions = [
    {'title': 1, 'answers': [1,2,3]},
    {'title': 2, 'answers': [1,2,3]},
    {'title': 3, 'answers': [1,2,3]}
]














