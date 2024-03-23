import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.screeen_rect = screen.get_rect()

        image = pygame.image.load('images/ship_photo.png')
        self.image = pygame.transform.scale(image, (89, 72))
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screeen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
