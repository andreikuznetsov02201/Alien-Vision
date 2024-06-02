class Settings():
    """Класс для хранения всех настроек"""
    
    def __init__(self):
        """Инициализирует настройки игры"""
        #Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #Корабль
        self.ship_limit = 3
        self.ship_speed = 3
        #Стрельба
        self.bullet_speed = 2
        self.bullet_height = 15
        self.bullet_weight = 3#3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        #Скорость пришельца
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10#10
        self.fleet_direction = 1
        #fleet_direction 1 это право, а -1 это лево
