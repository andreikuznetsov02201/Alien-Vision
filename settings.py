class Settings():
    """Класс для хранения всех настроек"""
    
    def __init__(self):
        """Инициализирует статические настройки игры"""
        #Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #Корабль
        self.ship_limit = 3
        self.ship_speed = 3
        #Стрельба
        self.bullet_speed = 3
        self.bullet_height = 15
        self.bullet_weight = 3#3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        #Скорость пришельца
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10#10

        #Темп ускорения игры
        self.speedup_scale = 1.1#1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки изменяющиеся в ходе игры"""
        self.ship_speed_factor = 0.5#1.5
        self.bullet_speed_factor = 0.5#3.0
        self.alien_speed_factor = 0.5#1.0

        self.fleet_direction = 1
        #fleet_direction 1 это право, а -1 это лев
        #Подсчет очков
        self.aliens_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.aliens_points = int(self.aliens_points * self.score_scale)#возможно не рабочий метод
        #print(self.aliens_points)