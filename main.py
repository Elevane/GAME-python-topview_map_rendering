import pygame as pg
import random
import sys
from properties import *
from sprites import *
from os import path

class Game:
    def __init__(self):
        # initialize game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.loadData()
        self.running = True

    def new(self):
        # new game
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self)
        self.platforms = pg.sprite.Group()
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
           p = Platform(*plat)
           self.all_sprites.add(p)
           self.platforms.add(p)
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def loadData(self):
        self.dir = path.dirname(__file__)
        imgDir = path.join(self.dir, 'img/Player')
        self.spritesheet = Spritesheet(path.join(imgDir, SPRITESHEET))

    def update(self):
        # game loop update
        self.all_sprites.update()
        # check if player hots platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        if self.player.pos.x > WIDTH - (4 * PLAYER_WIDTH) and self.player.walking:
            for plat in self.platforms:
                plat.rect.x -= abs(self.player.vel.x)
        if self.player.pos.x < (4 * PLAYER_WIDTH) and self.player.walking:
            for plat in self.platforms:
                plat.rect.x += abs(self.player.vel.x)


    def events(self):
        # game loop events
        # event loop
        for event in pg.event.get():
            # closing window if
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                sys.exit()
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
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
exit()











