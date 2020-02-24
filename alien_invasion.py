import pygame
import sys
from settings import Settings
import game_function as gf
from alien import Alien
from pygame.sprite import Group
from ship import Ship

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien War")

    # 创建外星人
    aliens = Group()
    gf.create_fleet(ai_settings,screen,0,aliens)
    # 创建飞船
    ship = Ship(ai_settings,screen)
    while True:
        # 更新外星人移动
        gf.update_aliens(ai_settings, aliens)
        # 更新飞船移动
        gf.check_events(ship)
        ship.update()
        # 更新整个屏幕 Todo:添加飞船和子弹的更新
        gf.update_screen(ai_settings,screen,ship,aliens,0)


run_game()