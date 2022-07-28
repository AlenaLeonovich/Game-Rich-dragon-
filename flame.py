import pygame

class Flame(pygame.sprite.Sprite):

    def __init__(self, screen, dragon):
        # инициализация пламени и размещение на экране
        super(Flame, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/kisspng-fire-flame.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = dragon.rect.centerx
        self.rect.top = dragon.rect.top
        self.y = float(self.rect.y)
        self.speed = 7.5


    def update(self):
        # движение пламени по вертикали вверх
        self.y -= self.speed
        self.rect.y = self.y

    def draw_flame(self):
        # отрисовка пламени на экране
        self.screen.blit(self.image, self.rect)