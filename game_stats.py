class GameStats():
    """Отслеживание статистики для игры"""

    def __init__(self, ai_game):
        #Инициализирует статистику
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        #Изменения в ходе игры
        self.ship_left = self.settings.ship_limit
        self.game_active = True








