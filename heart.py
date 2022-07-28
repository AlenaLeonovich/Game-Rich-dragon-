import pygame

class Heart(pygame.sprite.Sprite):

    def __init__(self, screen):

        super(Heart, self).__init__()

        # инициализация изображения сердца
        self.screen = screen
        self.image = pygame.image.load('images/heart.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


    def draw_heart(self):
        # отрисовка сердца на экране
        self.screen.blit(self.image, self.rect)