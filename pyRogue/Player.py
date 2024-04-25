import pygame
import App


class Player:
    def __init__(self, width, height, color = "blue", x = 0, y = 0):
        self.width = width  # need to make that a float value in 0 -- 16
        self.width_2 = width/2
        self.height = height
        self.height_2 = height/2
        self.color = color
        self.x, self.y = x, y # actually represent the middle part of the player
        self.vx, self.vy = 0, 0

    def move_by(self, d_x, d_y): # delta = (right, down)
        if   (self.x - self.width_2  + dx < 0) or (self.x + self.width_2  + dx > App.App.SIZE_X):
            return
        elif (self.y - self.height_2 + dy < 0) or (self.y + self.height_2 + dy > App.App.SIZE_Y):
            return
        else:
            self.x += + d_x
            self.y += + d_y

    def draw(self):
        pygame.draw.rect(self.surface, "blue", self.rect)
