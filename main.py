import pygame as pg
import random
from properties import *



class Game:
    def __init(self):
        #initialize game window
        pg.init()
        pg.mixer.init()
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        clock = pg.time.clock()
        self.run = True

    def new(self):
        #new game
        pass

    def run(self):
        #game loop
        pass

    def update(self):
        #game lopp update
        pass

    def events(self):
        #game loop events
        pass

    def draw(self):
        #game loop draw
        pass
    def show_start_screen(self):
        #game start screen
        pass
    def show_go_screen(self):
        #game over
        pass


g = Game()
g.show_start_screen()
while g.run:
    g.new()
    g.show_go_screen()

pg.QUIT()




all_sprites = pg.sprite.Group()


run = True
# GAme loop
while run:
    # speed of the loop
    clock.tick(FPS)
    #event lopp
    for event in pygmae.event.get():
        #closing window if
        if event.type == pg.QUIT:
            run = False

