from typing import Any
import pygame
from pygame.sprite import Sprite
#класс представляющий одного пришельца
class Alien(Sprite):
    #инициализация пришельца и задает начвальную позицию
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #загрузка изображения
        self.image = pygame.image.load("images/alien_ship_new.png")
        self.rect = self.image.get_rect()

        #каждый новый пришелец появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #сохранениеточной горизонтальной позиции пришельца
        self.x = float(self.rect.x)    
    
    def check_edges(self):
        """Возвращает True если пришелец у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)        
        self.rect.x = self.x

        