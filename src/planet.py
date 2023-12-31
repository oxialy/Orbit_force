from src import game_functions as gf
from src import msc


from src.settings import WIDTH, HEIGHT
from src.drawing_variables import colors, colB


import pygame
import math
import random

from pygame import Vector2
from math import sqrt, cos, sin
from random import randrange, choice


class Planet:
    def __init__(self, pos, rad, angle=0, type='planet', orbit_dist=0):
        self.pos = pos
        self.rad = rad
        self.angle = angle

        self.col = colors['blue2']

        self.angular_vel = 0.1
        self.vel = Vector2(0,0)
        self.vel_norm = 0

        self.max_vel = 7

        self.orbit = []
        self.orbit_dist = orbit_dist

        self.path = []
        self.TRACK_CD = 0

        self.DRAW_PATH = True

        self.type = type

    def init_orbit(self):
        self.type = 'planet'
        dist_1 = randrange(8,50)
        dist_2 = randrange(15,65)

        angle_1 = randrange(0, 620) / 100
        angle_2 = randrange(0, 620) / 100

        A = msc.get_point_from_angle(self.pos, angle_1, dist_1)
        B = msc.get_point_from_angle(self.pos, angle_2, dist_2)
        C = msc.get_point_from_angle(self.pos, angle_2, 30)

        planet_a = Planet(A, 10, angle_1, 'orbit', dist_1)
        planet_b = Planet(B, 10, angle_2, 'orbit', dist_2)
        planet_c = Planet(C, 10, angle_2, 'orbit', 30)

        planet_a.col = colors['orange1']
        planet_a.angular_vel = randrange(5, 20) / 100 * choice([-1, 1])

        planet_b.col = colors['orange1']
        planet_b.angular_vel = randrange(1,13) / 100 * choice([-1, 1])

        planet_c.angular_vel = randrange(1,13) / 100 * choice([-1, 1])


        self.orbit = [planet_a, planet_b]

        return self.orbit

    def draw(self, win):
        pygame.draw.circle(win, self.col, self.pos, self.rad)

        self.draw_orbit(win)

        if self.DRAW_PATH:
            self.draw_path(win)

    def draw_orbit(self, win):
        for orbit in self.orbit:
            orbit.draw(win)

    def draw_path(self, win):
        for pos in self.path:
            pygame.draw.circle(win, colors['grey1'], pos, 1)

    def move(self):
        self.pos += self.vel

    def apply_force(self):
        for orbit in self.orbit:
            B = orbit.pos
            force_factor = 3

            force = msc.get_gravity(self.pos, B, 0, force_factor)

            self.vel += force

    def update_vel_norm(self):
        x, y = self.vel

        self.vel_norm = sqrt(x**2 + y**2)

        return self.vel_norm

    def cap_velocity(self):
        self.update_vel_norm()

        if self.vel != (0,0):
            k = self.max_vel / self.vel_norm

            if self.vel_norm > self.max_vel:
                self.vel *= k

    def add_pos(self):
        x, y = self.pos
        self.path.append((x,y))
        if len(self.path) > 170:
            self.path.pop(0)

    def update_orbit(self):
        for orbit in self.orbit:
            orbit.angle += orbit.angular_vel
            orbit.pos = msc.get_point_from_angle(self.pos, orbit.angle, orbit.orbit_dist)


def update_all_planets(planets):
    for planet in planets:
        if planet.type == 'planet':
            planet.apply_force()
            planet.cap_velocity()
            planet.update_orbit()

            planet.move()

        if planet.TRACK_CD >= 2:
            planet.add_pos()
            planet.TRACK_CD = 0

        planet.TRACK_CD += 1

    return planets


def toggle_path(planets):
    for planet in planets:
        planet.DRAW_PATH = not planet.DRAW_PATH








