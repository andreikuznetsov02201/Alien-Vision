import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:#класс для управления кода

    def __init__(self):# создаем игровые ресурсы

        pygame.init()#почему не ставится нижние подчеркивание
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  
        pygame.display.set_caption("Alien Inavasion")

        self.ship = Ship(self.screen)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit

            pygame.display.flip()
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
        



