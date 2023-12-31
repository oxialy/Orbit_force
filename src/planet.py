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
    def __init__(self, pos, rad, angle=0, type='planet'):
        self.pos = pos
        self.rad = rad
        self.angle = angle

        self.col = colors['blue2']

        self.angular_vel = 0.1
        self.vel = Vector2(0,0)
        self.vel_norm = 0

        self.max_vel = 7

        self.orbit = []
        self.orbit_dist = 60

        self.path = []
        self.TRACK_CD = 0

        self.DRAW_PATH = True

        self.type = type

    def init_orbit(self):
        self.type = 'planet'
        angle_1 = randrange(0, 620) / 100
        angle_2 = randrange(0, 620) / 100

        A = msc.get_point_from_angle(self.pos, angle_1, self.orbit_dist)
        B = msc.get_point_from_angle(self.pos, angle_2, self.orbit_dist)

        planet_a = Planet(A, 10, angle_1, 'orbit')
        planet_b = Planet(B, 10, angle_2, 'orbit')

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
            pygame.draw.circle(win, colors['grey1'], pos, 3)

    def move(self):
        self.pos += self.vel

    def apply_force(self):
        for orbit in self.orbit:
            B = orbit.pos
            force_factor = 60

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
        if len(self.path) < 100:
            self.path.append(self.pos)

    def update_orbit(self):
        for orbit in self.orbit:
            orbit.angle += orbit.angular_vel
            orbit.pos = msc.get_point_from_angle(self.pos, orbit.angle, self.orbit_dist)


def update_all_planets(planets):
    for planet in planets:
        if planet.type == 'planet':
            planet.apply_force()
            planet.cap_velocity()
            planet.update_orbit()

            planet.move()

        if planet.TRACK_CD >= 4:
            planet.add_pos()
            planet.TRACK_CD = 0

        planet.TRACK_CD += 1

    return planets


def toggle_path(planets):
    for planet in planets:
        planet.DRAW_PATH = not planet.DRAW_PATH








