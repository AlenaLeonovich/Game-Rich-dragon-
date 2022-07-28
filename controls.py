import pygame, sys
from flame import Flame
from stone import Stone
from diamound import Diamound
import time


def events(screen, stats, play_button, dragon, flames):
    # обработка нажатия клавиш
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            # обработка нажития мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(screen, stats, play_button, mouse_x, mouse_y)

        elif event.type == pygame.KEYDOWN:
            # обработка нажития пробела, создание огня
            if event.key == pygame.K_SPACE:
                new_flame = Flame(screen, dragon)
                flames.add(new_flame)
            # движение дракона вправо
            if event.key == pygame.K_RIGHT:
                dragon.right = True
            # движение дракона влево
            elif event.key == pygame.K_LEFT:
                dragon.left = True

        elif event.type == pygame.KEYUP:
            # движение дракона вправо
            if event.key == pygame.K_RIGHT:
                dragon.right = False
            # движение дракона влево
            elif event.key == pygame.K_LEFT:
                dragon.left = False


def check_play_button(screen, stats, play_button, mouse_x, mouse_y):
    # проверка нажатия кнопки мыши, начало игры
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.run_game = True
        pygame.mouse.set_visible(False)


def update(color, background, screen, stats, score, dragon, stones, diamounds, flames,  play_button):
    # обновление экрана
    # отрисовка объектов игры
    screen.fill(color)
    screen.blit(background, (0, 0))
    score.show_score()
    for flame in flames.sprites():
        flame.draw_flame()
    dragon.draw()
    diamounds.draw(screen)
    stones.draw(screen)
    if stats.run_game == False:
        play_button.draw_button()
    pygame.display.flip()


def update_flames(screen, stats, score, diamounds, stones, flames):
    # обновление пламени
    flames.update()
    for flame in flames.copy():
        # удаление пламени за пределами игрового поля
        if flame.rect.bottom <= 0:
            flames.remove(flame)
    # проверка пересечения пламени и камней
    collisions = pygame.sprite.groupcollide(flames, stones, True, True)
    if collisions:
        # начисление баллов за все сбитые камни
        for stones in collisions.values():
            stats.score += 1 * len(stones)
        # счет игры и жизней дракона
        score.image_score()
        score.image_lifes_dragon()
    # удаление алмазов за пределами игрового поля
    for diamound in diamounds.copy():
        if diamound.rect.top >= 700:
            diamounds.remove(diamound)
    # проверка сбитых камней и алмазов
    if len(stones) == 0 and len(diamounds) == 0:
        # переход на новый уровень игры
        stats.level += 1
        score.image_level()
        flames.empty()
        # увеличение скорости камней и алмазов, количество рядов
        stats.increase_speed()
        stats.increase_row()
        # создание новых камней и алмазов
        all_diamounds(screen, stats, diamounds)
        all_stones(screen, stats, stones)


def update_diamounds(diamounds, dragon, stats, score, flames):
    # обновление алмазов
    diamounds.update()
    # проверка пересечения дракона с алмазами
    collisions_dragon = pygame.sprite.spritecollide(dragon, diamounds, True)
    for dragon in collisions_dragon:
        # при пересечении добавление 2 очков
        stats.score += 2
        score.image_score()
    # проверка пересечения пламени с алмазами
    collisions_diamounds = pygame.sprite.groupcollide(diamounds, flames, False, False)
    for diamound in collisions_diamounds:
        # при пересечении увеличение скорости алмазов
        diamound.speed += 0.5
        diamound.update()


def update_stones(stats, screen, score, dragon, stones, diamounds, flames):
    # обновление камней
    stones.update()
    # проверка столкновения дракона с камнями
    if pygame.sprite.spritecollideany(dragon, stones):
        dragon_kill(stats, screen, score,  dragon, stones, diamounds, flames)
    stones_check(stats, screen, score, dragon, stones, diamounds, flames)


def dragon_kill(stats, screen, score, dragon, stones, diamounds, flames):
    # обработка смерти дракона
    if stats.dragon_lifes > 0:
        stats.dragon_lifes -= 1
        score.image_lifes_dragon()
        # удаление камней, алмазов и пламени
        stones.empty()
        diamounds.empty()
        flames.empty()
        # создание новых камней, алмазов и дракона
        all_stones(screen, stats, stones)
        all_diamounds(screen, stats, diamounds)
        dragon.new_dragon()
        time.sleep(1)
    else:
        # если жизни закончились вывод 'game over' и завершение игры
        score.image_end()
        pygame.display.flip()
        time.sleep(2)
        stats.run_game = False
        sys.exit()


def stones_check(stats, screen, score, dragon, stones, diamounds, flames):
    # проверка касания камней края игрового поля
    screen_rect = screen.get_rect()
    for stone in stones.sprites():
        if stone.rect.bottom >= screen_rect.bottom:
            dragon_kill(stats, screen, score, dragon, stones, diamounds, flames)
            break


def all_stones(screen, stats, stones):
    # создание группы камней
    stone = Stone(screen, stats)
    stone_width = stone.rect.width
    stone_height = stone.rect.height
    col_stone_x = 10
    col_stone_y = stats.col_stone_y
    margin = 11
    # создание рядов и коллон камней
    for row in range(col_stone_y):
        for column in range(col_stone_x):
            stone = Stone(screen, stats)
            stone.x = stone_width + (column * stone_width) + margin * column
            stone.y = 0 - (row * stone_height) - margin * row
            stone.rect.x = stone.x
            stone.add(stones)


def all_diamounds(screen, stats, diamounds):
    # создание группы алмазов
    diamound = Diamound(screen, stats)
    diamound_width = diamound.rect.width
    diamound_height = diamound.rect.height
    col_diamound_x = 10
    col_diamound_y = stats.col_diamound_y
    margin = 11
    # создание рядов и коллон алмазов
    for row in range(col_diamound_y):
        for column in range(col_diamound_x):
            diamound = Diamound(screen, stats)
            diamound.x = diamound_width + (column * diamound_width) + margin * column
            diamound.y = 0 - (row * diamound_height) - margin * row
            diamound.rect.x = diamound.x
            diamound.add(diamounds)

