import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.settings = screen.settings
        self.screeen_rect = screen.get_rect()

        self.moving_right = False
        self.moving_left = False


        image = pygame.image.load('images/ship_photo.png')
        self.image = pygame.transform.scale(image, (89, 72))
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screeen_rect.midbottom

        self.x = float(self.rect.x)

        #флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.x += self.settings.ship_speed            
        if self.moving_left:
            self.x -= self.settings.ship_speed

            self.rect.x = self.x
            
    def blitme(self):
        self.screen.blit(self.image, self.rect)
