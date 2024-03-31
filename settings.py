class Settings():
    """Класс для хранения всех настроек"""
    
    def __init__(self):
        """Инициализирует настройки игры"""
        #Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 255)
        self.ship_speed = 1.5#fgvb
