import pygame, controls
from dragon import Dragon
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from button import Button


def run():
    pygame.init()
    # создание игрового поля
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption('Rich dragon')
    color = (0, 0, 0)
    background = pygame.image.load('images/cave-in-the-stone.png')
    # создание объектов игры
    dragon = Dragon(screen)
    flames = Group()
    stones = Group()
    diamounds = Group()
    stats = Stats()
    controls.all_stones(screen, stats, stones)
    controls.all_diamounds(screen, stats, diamounds)
    score = Scores(screen, stats)
    play_button = Button(screen, "Play")

    # запуск цикла игры
    while True:
        controls.events(screen, stats, play_button, dragon, flames)
        controls.update(color, background, screen, stats, score, dragon, stones, diamounds, flames, play_button)
        if stats.run_game:
            # обновление позиций объектов игры
            dragon.update_dragon()
            controls.update_flames(screen, stats, score, diamounds, stones, flames)
            controls.update_stones(stats, screen, score, dragon, stones, diamounds, flames)
            controls.update_diamounds(diamounds, dragon, stats, score, flames)

run()