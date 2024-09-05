import sys

import pygame
from pygame.locals import QUIT

import Enemy
import GameSettings
import Player

pygame.init()

P1 = Player.Player()
pawns = []

starting_center = 0
for x in range(5):
    pawns.append(Player.Player())

for pawn in pawns:
    pawn.rect.x = starting_center
    starting_center += 35

E1 = Enemy.Enemy()


def run():
    """
    select the player
    deselect the player
    check to see if player is selected
    if player is selected and mouse was clicked move player to cursor
        location to where the cursor position was and deselect the player
    """

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            for p in range(pawns.__len__()):
                if event.type == pygame.MOUSEBUTTONDOWN and pawns[p].rect.collidepoint(
                    pygame.mouse.get_pos()
                ):
                    pawns[p].selected = True
                    print("i was clicked on")

                if (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and not pawns[p].rect.collidepoint(pygame.mouse.get_pos())
                    and pawns[p].selected
                ):
                    print("i moved!")
                    pawns[p].move()
                    pawns[p].selected = False

            # if (
            #     event.type == pygame.MOUSEBUTTONDOWN
            #     and not P1.rect.collidepoint(pygame.mouse.get_pos())
            #     and P1.selected
            # ):
            #     P1.selected = False

        # E1.move()

        GameSettings.DISPLAYSURF.fill(GameSettings.BLUE)
        for pawn in pawns:
            pawn.draw(GameSettings.DISPLAYSURF)
        E1.draw(GameSettings.DISPLAYSURF)

        pygame.display.update()
        GameSettings.FramePerSec.tick(GameSettings.FPS)


run()
