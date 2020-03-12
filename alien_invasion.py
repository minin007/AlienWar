import pygame
import sys
from settings import Settings
import game_function as gf
from alien import Alien
from pygame.sprite import Group
from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from threading import Timer

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien War")
    # 创建一个用于存储统计信息的实例
    stats = GameStats(ai_settings)
    # 创建飞船
    ship = Ship(ai_settings,screen)     
    # 创建一个用于子弹的编组
    bullet = Bullet(ai_settings,screen,ship)
    bullets = Group()
    # 创建外星人
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    while True:

        gf.check_events(ai_settings, screen, ship, bullet)
        if stats.game_active == True:
            # 更新外星人移动
            gf.update_aliens(ai_settings,stats,screen,ship, aliens,bullets)
            # 更新飞船移动
            ship.update()
            # 更新子弹位置
            gf.update_bullets(ai_settings, screen, ship, bullets, bullet)
        # 更新整个屏幕 Todo:添加飞船和子弹的更新
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        

run_game()