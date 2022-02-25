
import pygame , sys

MAP = [0 for i in range(20) ]

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 640))
        pygame.display.set_caption("test sprites")
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.dt = self.clock.tick(60) / 1000
            self.update()
            self.events()

    def update(self):
        pygame.display.update()
        self.screen.fill((0, 0, 0))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.quit()
                pygame.quit


if __name__ == "__main__":
    g = Game()
    g.run()