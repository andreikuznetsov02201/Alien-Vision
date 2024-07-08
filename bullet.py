import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.color = self.settings.bullet_color

        #Создание снаряда и назначение позиции
        self.rect = pygame.Rect(0, 0, self.settings.bullet_weight, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #Позиция снаряда
        self.y = float(self.rect.y)
    
    def update(self):
        #Перемещает снаряд вверх и обновление позиции!
        self.y -= self.settings.bullet_speed
        #Обновление позиции
        self.rect.y = self.y

    def draw_bullet(self):
        #Вывод снаряда на экран
        pygame.draw.rect(self.screen, self.color, self.rect)
#Thats all
