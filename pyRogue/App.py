import pygame
import sys
import math

from pyRogue.Config import *
import pyRogue.Timer
import pyRogue.Player


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(ROGUE_WIDTH, ROGUE_HEIGHT))
        self.timer  = pyRogue.Timer.Timer(FPS = ROGUE_FPS)
        self.player = pyRogue.Player.Player(size_x=ROGUE_PLAYER_SIZE_X, size_y=ROGUE_PLAYER_SIZE_Y)
    def run(self):
        while True:
            self.timer.update()
            self.mainloop()
            self.timer.wait_remaining_time()
    def mainloop(self):
        self.handle_events()
        self.handle_keys_pressed()
        self.update_screen()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    def handle_keys_movement(self, keys):
        # handle movement
        dvx, dvy = 0, 0
        if keys[pygame.K_w]:
            dvy += -1
        if keys[pygame.K_s]:
            dvy += 1
        if keys[pygame.K_a]:
            dvx += -1
        if keys[pygame.K_d]:
            dvx += 1
        metric = dvx**2 + dvy**2
        if metric < 0.5:
            self.player.decelerate()
        else:
            norm = math.sqrt(metric)
            self.player.accelerate(dvx/norm*ROGUE_ACC_PLAYER_MAX, dvy/norm*ROGUE_ACC_PLAYER_MAX)
        self.player.propagate()
    def handle_keys_pressed(self):    
        keys = pygame.key.get_pressed()
        self.handle_keys_movement(keys)
    def draw_player(self):
        pygame.draw.rect(self.screen, "blue", self.player.get_rect())
    def update_screen(self):
        self.screen.fill("black")
        self.draw_player()
        pygame.display.flip()


