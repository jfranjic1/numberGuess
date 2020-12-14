import pygame

class Grid:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.size = 5
        self.surface = None
        self.clock = None
        self.screen = None
        pass

    def draw(self):
        self.clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height), 0, 32)
        surface = pygame.Surface(screen.get_size())
        self.surface = surface.convert()
        self.screen = screen

        temp = pygame.Rect((0, 0), (self.width, self.height))
        pygame.draw.rect(self.surface, (255, 255, 255), temp)


        while(1):
            self.clock.tick(30)

            self.screen.blit(self.surface, (0, 0))
            pygame.display.update()
