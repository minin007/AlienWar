import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self,ai_settings,screen):
        """初始化外星人并设置其初始位置"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.alien_speed_factor = 1.0
        self.fleet_drop_speed = 10.0
        self.fleet_direction = 1

        # 加载外星人图像，并设置rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人初始位置为屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """单个外星人与屏幕边缘的碰撞检测"""
        screen_rect = self.screen.get_rect()
        if self.rect.right > screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    
    def update(self):
        """根据当前的速度更新位置"""
        self.x += (self.alien_speed_factor * self.fleet_direction)
        self.rect.x = self.x
        

            
        
