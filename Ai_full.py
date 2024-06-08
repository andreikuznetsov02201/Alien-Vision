import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint

class AlienInvasion:#класс для управления кода

    def __init__(self):# создаем игровые ресурсы

        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height#высота
        self.settings.screen_width = self.screen.get_rect().width#ширина
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  
        pygame.display.set_caption("Alien Inavasion")

        #Создание экземпляра для хранения игровой статистики
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()#добавлено

        self._create_fleet()
        self._create_star_fleet()

        #Создание кнопки play
        self.play_button = Button(self, "Play")

    def run_game(self):#основной цикл игы
        #Основные процессы
        while True:
            self._check_events()
            
            if self.stats.game_active:            
                self.ship.update()
                self.bullets.update()
                self._update_aliens()
                self._update_bullets()

            self._update_screen()
                        
    def _check_events(self):
        #обрабатывается нажатие клавиш
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
            elif event.type == pygame.KEYDOWN:#активирование клавиатуры
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True
    
    def _check_keydown_events(self, event):
        #НАЖАТИЕ КЛАВИШ
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        #ОТПУСКАНИЕ КЛАВИШ
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        #Создаем новый снаряд
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
 
    def _update_screen(self):
        #Обновляет изображение на экране и отображает новый
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.stars.draw(self.screen)#добавлено      
        self.aliens.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw_button()
        
        
        pygame.display.flip()#прорисовывает последний экран только под конец игры

    def _update_bullets(self):
        #Обновляет позиции снарярядов и уничтожает старые снраряды
        #Обновление позиций снарядов
        self.bullets.update()
        #Удаление снапрядов вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets))#показывает сколько снарядов сейчас в игре (не обязательная)

        self._check_bullet_alien_collisions()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _check_bullet_alien_collisions(self):
        #проверка попаданий в пришельцев
        #при обнаружении попадания удалить снаярд и пришельца
        collisions = pygame.sprite.groupcollide(
        self.bullets, self.aliens, True, True)

    def _update_aliens(self):
        #Обновляет позиции всех пришельцев во флоте
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #Проверить добрались ли пришельцы до нижнего края экрана
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Обрабатывает стокновение корабля с пришельцем"""
        if self.stats.ship_left > 0:#self не нужен
            self.stats.ship_left -= 1

            #Очистка списков пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()

            #Создание нового флота и размещение корабля в центре
            self._create_fleet()
            self.ship.center_ship()

            #Пауза
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """Проверяет добрались ли пришельцы до нижнего края экрана"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
        
    def _create_fleet(self):
        #Создает флот с пришельцами#
        #создание пришельца и вычисление количества пришельцев в ряду
        #интервал между соседними пришельцами равен ширине пришельца
        alien = Alien(self)
        #alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        #определяет колтчество рядов котооые поместятся на экране
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #создание флота
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

        #создание первого ряда пришельцев
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        #созданеи пришельца и размещение его в ряду
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        #alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        #Реагирует на достижение пришельца края
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        #Опускает весь флот и меняет направление флота
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
     
    """Создание звездного неба"""
    #Создание звездной сетки по первому примеру
    def _create_star_fleet(self):
        star = Star(self)
        star_width, star_height = star.rect.size

        
        available_space_x1 = self.settings.screen_width - (2 * star_width)
        number_stars_x1 = available_space_x1 // (5 * star_width)

        available_space_y1 = (self.settings.screen_height - (3 * star_height))
        number_rows1 = available_space_y1 // (5 * star_height)

        for row_number in range(number_rows1):
            for star_number in range(number_stars_x1):
                self._create_star(row_number, star_number)

    def _create_star(self, row_number, star_number):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 5 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 5 * star.rect.height * row_number
        delta = 30
        star.rect.x += randint(-delta, delta)
        star.rect.y += randint(-delta, delta)
        self.stars.add(star)
        
        #return random_star#новая


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

