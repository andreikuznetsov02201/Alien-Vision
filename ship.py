import pygame

class Ship():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()#!!!

        #self.moving_right = False
        #self.moving_left = False


        image = pygame.image.load('images/ship_photo.png')
        self.image = pygame.transform.scale(image, (89, 72))
        self.rect = self.image.get_rect()
    
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        #флаг перемещения!
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:#берём право и ширину объекта если мень грани
            self.x += self.settings.ship_speed#не выделяется            
        if self.moving_left and self.rect.left > 0:#берем сторону лево и ширину объекта ноль  это начало
            self.x -= self.settings.ship_speed

        self.rect.x = self.x#запрещает отматывать назад
            
    def blitme(self):
        self.screen.blit(self.image, self.rect)
#dddd