class GameStats():
    """Отслеживание статистики для игры"""

    def __init__(self, ai_game):
        #Инициализирует статистику
        self.ship_left = 0
        self.settings = ai_game.settings
        self.reset_stats()
        #self.high_score = 0

        self.game_active = False#F
        self.high_score = 0
        self.level = 1
        self.score = 0


    def reset_stats(self):
        #Изменения в ходе игры
        if self.ship_left <= 0:
            self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.game_active = True#T
          