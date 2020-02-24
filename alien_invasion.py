import pygame
import sys
from settings import Settings
import game_function as gf
from alien import Alien
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien War")

    # 创建外星人
    aliens = Group()
    gf.create_fleet(ai_settings,screen,0,aliens)
    while(True):
        # 更新外星人移动
        gf.update_aliens(ai_settings, aliens)

        gf.check_events()
        # 更新整个屏幕 Todo:添加飞船和子弹的更新
        gf.update_screen(ai_settings,screen,0,aliens,0)


run_game()