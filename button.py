import pygame.font

class Button():

    def __init__(self, screen, button):
        # инициализация кнопки запуска и размещение на экране
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # создание размера, цвета, шрифта кнопки
        self.width = 100
        self.height = 30
        self.button_color = (216, 30, 6)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.image_button(button)


    def image_button(self, button):
        # преобразование кнопки в изображение
        self.button_draw = self.font.render(button, True, self.text_color, self.button_color)
        self.button_rect = self.button_draw.get_rect()
        self.button_rect.center = self.rect.center


    def draw_button(self):
        # отрисовка кнопки на экране
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.button_draw, self.button_rect)


