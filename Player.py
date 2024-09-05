import pygame

import GameSettings


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("game_assetts/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.selected = False

    def update(self):
        self.move()
        # if self._is_player_selected():
        #     print("you clicked on me")
        #
        # if (
        #     pygame.mouse.get_pressed()[0] is True
        #     and not self.rect.collidepoint(pygame.mouse.get_pos())
        #     and self.selected
        # ):
        #     self.move()
        #     print("you clicked off of me")

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self):
        self.rect.y -= 100
        # if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(
        #     pygame.mouse.get_pos()
        # ):
        #     self.selected = True
        #     return self.selected
        # else:
        #     return False
