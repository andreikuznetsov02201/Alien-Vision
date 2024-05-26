class Settings():
    """Класс для хранения всех настроек"""
    
    def __init__(self):
        """Инициализирует настройки игры"""
        #Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 3
        #Стрельба
        self.bullet_speed = 2
        self.bullet_height = 15
        self.bullet_weight = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
#dddлоуау
