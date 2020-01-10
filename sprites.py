# sprites classes for platform game
import pygame as pg
from properties import *
from random import *

vec = pg.math.Vector2
#img = ['img/R12.png', 'img/R22.png', 'img/R32.png', 'img/R42.png', 'img/R52.png']
class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def getimage(self, x, y, width, height):
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0,0), (x,y, width,height))
        image = pg.transform.scale(image, (width//3, height//3))
        return image

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.game.spritesheet.getimage(192, 1024, 192, 256)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(WIDTH / 2, HEIGHT -40)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def load_images(self):
        self.standing_frames = self.game.spritesheet.getimage(0, 0, 192, 256)
        self.standing_frames.set_colorkey(BLACK)
        self.walk_frames_r = [
                              self.game.spritesheet.getimage(192, 1024, 192, 256),
                              self.game.spritesheet.getimage(384, 1024, 192, 256),
                              self.game.spritesheet.getimage(576, 1024, 192, 256),
                              self.game.spritesheet.getimage(768, 1024, 192, 256),
                              self.game.spritesheet.getimage(960, 1024, 192, 256),
                              self.game.spritesheet.getimage(1152, 1024, 192, 256),
                              self.game.spritesheet.getimage(1344, 1024, 192, 256)
                              ]
        self.walk_frames_l = []
        self.jump_frame = self.game.spritesheet.getimage(192, 0, 192, 256)
        self.jump_frame.set_colorkey(BLACK)
        for frame in self.walk_frames_r:
            frame.set_colorkey(BLACK)
            self.walk_frames_l.append(pg.transform.flip(frame, True, False))


    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self,self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20
    def update(self):
        self.animate()
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

    def animate(self):

        now = pg.time.get_ticks()
        if round(self.vel.x) != 0:
            self.walking = True
            print(round(self.vel.x))
        else:
            self.walking = False

        if self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
        if not self.jumping and not self.walking:
            self.last_update = now
            bottom = self.rect.bottom
            self.image = self.standing_frames
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # calculation of the motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
