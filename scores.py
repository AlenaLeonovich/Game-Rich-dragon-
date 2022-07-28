import pygame.font
from pygame.sprite import Group
from heart import Heart


class Scores():

    def __init__(self, screen, stats):
        # инициализация счета игры
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 40)
        self.image_score()
        self.image_level()
        self.image_lifes_dragon()
        self.image_end()


    def image_score(self):
        # преобразование счета в изображение
        self.score_draw = self.font.render(str(self.stats.score), True, self.text_color, (None))
        self.score_rect = self.score_draw.get_rect()
        # расположение сета на экране
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10


    def image_level(self):
        # преобразование уровней игры в изображение
        self.level_draw = self.font.render(str(self.stats.level), True, self.text_color)
        self.level_rect = self.level_draw.get_rect()
        # расположение уровней на экране
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def image_lifes_dragon(self):
        # количество жизней дракона
        self.heart = Group()
        for number in range(self.stats.dragon_lifes):
            heart = Heart(self.screen)
            heart.rect.x = 10
            heart.rect.y = 10 + number * (1.5 * heart.rect.height)
            self.heart.add(heart)


    def show_score(self):
        # вывод сета, уровней и жизней на экран
        self.screen.blit(self.score_draw, self.score_rect)
        self.screen.blit(self.level_draw, self.level_rect)
        self.heart.draw(self.screen)


    def image_end(self):
        # преобразование конца игры в изображение и вывод на экран
        self.end_draw = self.font.render('Game Over', True, self.text_color, (None))
        self.end_rect = self.end_draw.get_rect()
        self.end_rect.center = self.screen_rect.center
        self.screen.blit(self.end_draw, self.end_rect)
