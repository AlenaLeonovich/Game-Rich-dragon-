import pygame
from pygame.sprite import Sprite

class Dragon(Sprite):

    def __init__(self, screen):
        # инициализация дракона, размещение на экране и поворот в стороны
        super(Dragon, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/kisspng-nickelodeon-nick.png')
        self.image_left = pygame.transform.flip(self.image, 1, 0)
        self.image_right = self.image
        self.rect = self.image.get_rect()
        self.rect_left = self.image_left.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.right = False
        self.left = False


    def draw(self):
        # отрисовка дракона на экране
        self.screen.blit(self.image, self.rect)


    def update_dragon(self):
        # движение дракона по горизонтали
        if self.right and self.rect.right < self.screen_rect.right:
            self.image = self.image_right
            self.center += 6.5
        if self.left and self.rect.left > 0:
            self.image = self.image_left
            self.center -= 6.5
        self.rect.centerx = self.center


    def new_dragon(self):
        # создание нового дракона по центру
        self.center = self.screen_rect.centerx