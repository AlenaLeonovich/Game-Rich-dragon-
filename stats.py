
class Stats():
    # статистика игры

    def __init__(self):

        self.game_stats()
        self.initialize_speed()
        self.initialize_row()
        self.speed_scale = 1.3
        self.row_scale = 1
        self.run_game = False


    def game_stats(self):
        # изменяемая статистика игры
        self.dragon_lifes = 1
        self.score = 0
        self.level = 1


    def initialize_speed(self):
        # инициализация скорости камней и алмазов
        self.speed_stones = 1.5
        self.speed_diamounds = 1.5


    def increase_speed(self):
        # увеличение скорости камней и алмазов
        self.speed_stones *= self.speed_scale
        self.speed_diamounds *= self.speed_scale


    def initialize_row(self):
        # инициализация рядов камней и алмазов
        self.col_stone_y = 2
        self.col_diamound_y = 2


    def increase_row(self):
        # увеличение рядов камней и алмазов
        self.col_stone_y += self.row_scale
        self.col_diamound_y += self.row_scale

