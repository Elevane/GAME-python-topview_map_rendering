import pygame as pg
import random
from properties import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # new game
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # game lopp update
        self.all_sprites.update()
        pass

    def events(self):
        # game loop events
        # event loop
        for event in pg.event.get():
            # closing window if
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        # game start screen
        pass

    def show_go_screen(self):
        # game over
        pass


g = Game()
g.show_start_screen()
while g.run:
    g.new()
    g.show_go_screen()

pg.quit()











