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

        self.ship = Ship(self)

    def run_game(self):#основной цикл игы
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    def _check_events(self):
        #обрабатывается нажатие клавиш
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
            elif event.type == pygame.KEYDOWN:#активирование клавиатуры
                if event.key == pygame.K_RIGHT:#проверка нажатия
                    self.ship.moving_right = True  
                elif event.key == pygame.K_LEFT:#!!!TRUE
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:#!!!FALSE
                    self.ship.moving_left = False

    def _update_screen(self):
        #Обновляет изображение на экране
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
#дорешать !       



