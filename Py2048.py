import sys
import random
import time
import pygame
import pygame.locals
import os
import tkinter.messagebox as messagebox

pygame.init()
gamefont = pygame.font.SysFont('Consolas', 30)

BOXWIDTH = 837
BOXHEIGHT = 537

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((BOXWIDTH, BOXHEIGHT), pygame.RESIZABLE)
tiles = {}
random_tiles = ('tile_2', 'tile_4')
for i in range(16):
    tiles[i] = []

tile_2 = pygame.image.load(os.getcwd() + '\\py2048_assets\\tiles\\2048_2.jpg')
tile_4 = pygame.image.load(os.getcwd() + '\\py2048_assets\\tiles\\2048_4.jpg')
tile_blank = pygame.image.load(os.getcwd() + '\\py2048_assets\\tiles\\2048_blank.jpg')
playermoved = False


def main():
    global playermoved
    random_tile()
    try:
        while True:
            if playermoved:
                random_tile()
                playermoved = False
            draw_blocks()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen.blit(gamefont.render('Exiting...', True, WHITE), (0, 0))
                    pygame.display.update()
                    sys.exit()
                if keys[pygame.K_RIGHT]:
                    move_tile('right')
            pygame.display.update()
    except Exception as e:
        messagebox.showerror('Error',f'Py2048 has encountered a fatal error and cannot continue:\n {e}')


def random_tile():
    global random_tiles
    templist1 = []
    for atile in tiles:
        if not tiles[atile]:
            templist1.append(atile)
    for lol in range(random.randint(1, 4)):
        tiles[random.choice(templist1)] = [random.choice(random_tiles)]
    #print(tiles)


def draw_blocks():
    for item in tiles:
        if tiles[item] and item % 2 != 0 or item % 4 == 0 and tiles[item]:
            screen.blit(eval(tiles[item][0]), (155 + (item % 4) * 133, 5 + int(item / 4) * 133))
        elif tiles[item]:
            screen.blit(eval(tiles[item][0]), (155 + 266, 5 + int(item / 4) * 133))
        else:
            screen.blit(tile_blank, (155 + (item % 4) * 133, 5 + int(item / 4) * 133))


def move_tile(direction):
    global playermoved
    if direction == 'right':
        for item in tiles:
            if (item + 1) % 3 == 0:
                if not tiles[item + 1]:
                    tiles[item + 1] = tiles[item]
                    tiles[item] = []
                    print(tiles)
    playermoved = True


if __name__ == '__main__':
    main()
