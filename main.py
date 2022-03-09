
import random
import pygame , sys

randomaray = [1, 0, 0 ,0, 1, 0]


MAP= []
for i in range(100):
    MAP.append([randomaray[random.randint(0, len(randomaray)- 1)] for y in range(100)])
with open("map.py", "w+") as o:
    o.write(str(MAP))

"""
MAP = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]"""



class Map:
    def __init__(self, game):
        self.map = MAP
        self.game = game
        self.walls = []
    def draw(self):
        
        if self.map:
            for x, row in enumerate(self.map):
                for y, col in enumerate(row):
                    posx, posy = x*32 , y*32
                    
                    window = pygame.Rect(self.game.camera.x, self.game.camera.y, 800, 640)
                    
                    if pygame.Rect(posx, posy, 32, 32).colliderect(window):
                        
                        if col == 1:
                                img = pygame.image.load("img\stone_block.png").convert_alpha()
                                self.walls.append([posx, posy])
                        if col == 0:
                            img = pygame.image.load("img\\back_stone_block.png").convert_alpha()
                        if col == 2: 
                            img = pygame.image.load("img\grass_block.png").convert_alpha()
                        self.game.surface.blit(img, (posx, posy))
                  

    
                    


class Player:
    def __init__(self, game):
        self.game = game
        self.x = 200
        self.y = 200
        self.speed =16
        self.direction = "down"
        self.collide = False
    def draw(self):
        char = pygame.image.load(f"img\\{self.direction}_char.png").convert_alpha()
        self.game.surface.blit(char, (self.x, self.y))

    def move(self, axis):
        self.old_direction = self.direction
        self.direction = axis
        if self.colliding(self.old_direction) == False:
            if axis == "left":
                self.x -= self.speed
            elif axis == "right":
                self.x += self.speed
            elif axis == "up":
                self.y -= self.speed
            elif axis == "down":
                self.y += self.speed
                
class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y
            
class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.camera = Camera(0, 0)
        self.screen = pygame.display.set_mode((800, 640))
        
        self.clock = pygame.time.Clock()
        self.map = Map(self)
        ##self.player = Player(self)
        self.surface = pygame.Surface((800, 640)).convert_alpha()

    def run(self):
        while True:
            self.clock.tick(60)
            self.dt = self.clock.tick(60) / 1000
            self.update()
            self.events()
            self.draw()
            

    def draw(self):
        # à toutes les frames dessine seulement la surface visible
        # visible = 
        self.map.draw()
        self.screen.blit(self.surface, (0, 0))
        pygame.display.set_caption(str(self.clock.get_fps()))
        ##self.player.draw()

    def update(self):
        
        pygame.display.update()
        ##self.surface.fill((0,0,0))
        self.screen.fill((0, 0, 0))


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.quit()
                pygame.quit
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.camera.x -= 10
        elif key[pygame.K_RIGHT]:
            self.camera.x += 10
        elif key[pygame.K_UP]:
            self.camera.y += 10
        elif key[pygame.K_DOWN]:
            self.camera.y -= 10


if __name__ == "__main__":
    g = Game()
    g.run()