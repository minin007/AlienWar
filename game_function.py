import sys
import pygame
from alien import Alien
from ship import Ship


def check_events(ship):
    """响应按键和鼠标事件"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 按住按键
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        # 松开按键
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
        


def update_screen(ai_settings,screen,ship,aliens,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""

    screen.fill(ai_settings.bg_color)
    aliens.draw(screen)
    ship.blitme()
    pygame.display.flip()

def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""      
    available_space_x = ai_settings.screen_width - 2 * alien_width      
    number_aliens_x = int(available_space_x / (2 * alien_width))      
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height + (3 * alien_height) - ship_height)     
    number_rows = int(available_space_y / (2 * alien_height))      
    return number_rows 

def create_alien(ai_settings, screen, aliens, alien_number, row_number): 
    """创建外星人的位置"""
    alien = Alien(ai_settings, screen) 
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number      
    alien.rect.x = alien.x 
    alien.rect.y = alien.rect.height+2 * alien.rect.height * row_number
    aliens.add(alien) 

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings,screen)
    ship = Ship(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)     
    number_rows = get_number_rows(ai_settings,400,alien.rect.height)    
    # 创建外星人群
    for row_number in range(number_rows):         
        for alien_number in range(number_aliens_x):              
            create_alien(ai_settings, screen, aliens, alien_number, row_number)



def check_fleet_edges(ai_settings, aliens):
    """边缘检测并改变运动"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """将外星人下移并改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += alien.fleet_drop_speed
        alien.fleet_direction *= -1

def update_aliens(ai_settings, aliens):
    """更新外星人移动"""
    check_fleet_edges(ai_settings, aliens)
    for alien in aliens.sprites():
        alien.update()
    
