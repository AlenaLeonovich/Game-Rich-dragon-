import pygame


class Diamound(pygame.sprite.Sprite):

    def __init__(self, screen, stats):
        # инициализация алмазов и размещение на экране
        super(Diamound,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/diamound-1.png')
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.y - 50
        self.y = float(self.rect.y)
        self.speed = stats.speed_diamounds


    def draw(self):
        # отрисовка алмазов на экране
        self.screen.blit(self.image, self.rect)


    def update(self):
        # движение алмазов по вертикали
         self.y += self.speed
         self.rect.y = self.y


