import pygame
from pygame.sprite import Sprite
#класс представляющий одного пришельца
class Alien(Sprite):
    #инициализация пришельца и задает начвальную позицию
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #загрузка изображения
        self.image = pygame.image.load("images/ailen_photo.png")
        self.rect = self.image.get_rect()

        #каждый новый пришелец появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #сохранениеточной горизонтальной позиции пришельца
        self.x = float(self.rect.x)
        #gggg