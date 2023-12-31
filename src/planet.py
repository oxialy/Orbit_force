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

        self.angular_vel = 1
        self.vel = Vector2(0,0)
        self.vel_norm = 0

        self.max_vel = 7

        self.orbit = []
        self.orbit_dist = 60

        self.type = type

    def init_orbit(self):
        angle_1 = randrange(0, 620) / 100
        angle_2 = randrange(0, 620) / 100

        A = msc.get_point_from_angle(self.pos, angle_1, self.orbit_dist)
        B = msc.get_point_from_angle(self.pos, angle_2, self.orbit_dist)

        planet_a = Planet(A, 10, angle_1, 'orbit')
        planet_b = Planet(B, 10, angle_2, 'orbit')

        self.orbit = [planet_a, planet_b]

    def draw(self, win):
        pygame.draw.circle(win, self.col, self.pos, self.rad)

    def draw_orbit(self, win):
        for orbit in self.orbit:
            orbit.draw(win)

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

        k = self.max_vel / self.vel_norm

        if self.vel_norm > self.max_vel:
            self.vel *= k


    def update_orbit(self):
        for orbit in self.orbit:
            orbit.angle += orbit.angular_vel
            orbit.pos = msc.get_point_from_angle(self.pos, orbit.angle, self.orbit_dist)


def update_all_planets(planets):
    for planet in planets:
        planet.apply_force()
        planet.cap_velocity()
        planet.update_orbit()

        planet.move()

    return planets












