import pygame

class Stone(pygame.sprite.Sprite):

    def __init__(self, screen, stats):
        # инициализация камней и размещение на экране
        super(Stone, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/stone-1.png')
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.y - 50
        self.y = float(self.rect.y)
        self.speed = stats.speed_stones


    def draw(self):
        # отрисовка камней на экране
        self.screen.blit(self.image, self.rect)

    def update(self):
        # движение камней по вертикали
        self.y += self.speed
        self.rect.y = self.y

