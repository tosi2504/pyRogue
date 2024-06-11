import pygame
import math

from pyRogue.Config import *

class Player:
    def __init__(self, size_x, size_y, color = "blue", x = ROGUE_SIZE_X/2, y = ROGUE_SIZE_Y/2):
        self.size_x = size_x  # need to make that a float value in 0 -- 16
        self.size_x_2 = size_x/2
        self.size_y = size_y
        self.size_y_2 = size_y/2
        self.color = color
        self.x, self.y = x, y # actually represent the middle part of the player
        self.vx, self.vy = 0, 0 # speed should be in units of [x,y]/[1s]

    def move_by(self, dx, dy): # delta = (right, down)
        if   (self.x - self.size_x_2  + dx < 0) or (self.x + self.size_x_2  + dx > ROGUE_SIZE_X):
            return
        elif (self.y - self.size_y_2 + dy < 0) or (self.y + self.size_y_2 + dy > ROGUE_SIZE_Y):
            return
        else:
            self.x += + dx
            self.y += + dy

    def propagate(self):
        self.move_by(self.vx, self.vy)

    def accelerate(self, dvx, dvy):
        self.vx += dvx 
        self.vy += dvy 
        metric = self.vx ** 2 + self.vy ** 2
        if (metric > ROGUE_V_PLAYER_MAX**2):
            norm = math.sqrt(metric)
            self.vx = ROGUE_V_PLAYER_MAX * self.vx / norm
            self.vy = ROGUE_V_PLAYER_MAX * self.vy / norm

    def decelerate(self):
        norm = math.sqrt(self.vx ** 2 + self.vy ** 2)
        if (norm < ROGUE_ACC_PLAYER_MAX):
            self.vx, self.vy = 0, 0
        else :
            self.vx -= ROGUE_ACC_PLAYER_MAX * self.vx/norm
            self.vy -= ROGUE_ACC_PLAYER_MAX * self.vy/norm

    def get_rect(self):
        return pygame.Rect((self.x-self.size_x_2)*ROGUE_SCALE,
                           (self.y-self.size_y_2)*ROGUE_SCALE,
                           self.size_x*ROGUE_SCALE,
                           self.size_y*ROGUE_SCALE)
