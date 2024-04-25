import pygame
import sys
import pyRogue.Timer
import pyRogue.Player



class App:
    SIZE_X, SIZE_Y = 16, 9
    FPS            = 60
    SCALE          = 80 # 1280, 720
    WIDTH          = SCALE * SIZE_X
    HEIGHT         = SCALE * SIZE_Y

    def __init__(self, ):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(App.WIDTH, App.HEIGHT))
        self.timer  = pyRogue.Timer.Timer(FPS = App.FPS)
        self.player = pyRogue.Player.Player(width=1, height=1)
        
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

    def handle_keys_pressed(self):    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move_by((0,-10))
        if keys[pygame.K_s]:
            self.player.move_by((0,10))
        if keys[pygame.K_a]:
            self.player.move_by((-10,0))
        if keys[pygame.K_d]:
            self.player.move_by((10,0))

    def update_screen(self):
        self.screen.fill("black")
        self.draw_player()
        pygame.display.flip()


