import pygame
import random
import GameSettings

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("game_assetts/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,GameSettings.SCREEN_WIDTH),0) 
 
      # def move(self):
      #   self.rect.move_ip(0,10)
      #   if (self.rect.bottom > 600):
      #       self.rect.top = 0
      #       self.rect.center = (random.randint(100, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
