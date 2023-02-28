import pygame

class Ball:
    def __init__(self, x_loc, y_loc, radius, surface):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.radius = radius
        self.color = (0, 0, 0)
        # x, y
        self.movement_vector = [0, 0]
        # screen that is being drawn to
        self.surface = surface

    def set_x_loc(self, loc):
        self.x_loc = loc

    def set_y_loc(self, loc):
        self.y_loc = loc

    def set_velocity(self, vector):
        self.movement_vector = vector

    def change_velocity(self, x, y):
        self.movement_vector[0] += x
        self.movement_vector[1] += y

    def move_frame(self):
        self.x_loc = self.x_loc + self.movement_vector[0]
        self.y_loc = self.y_loc + self.movement_vector[1]