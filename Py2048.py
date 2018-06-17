import sys
import random
import time
import pygame
import pygame.locals
import os
import tkinter.messagebox as messagebox
from tkinter import Tk

mainbox = Tk()
mainbox.withdraw()

pygame.init()
gamefont = pygame.font.SysFont('Consolas', 30)
pygame.display.set_caption('2048')

BOXWIDTH = 1037
BOXHEIGHT = 537

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BACKGROUND = (142, 126, 108)

screen = pygame.display.set_mode((BOXWIDTH, BOXHEIGHT), pygame.RESIZABLE)
tiles = {}
random_tiles = ('tile_2', 'tile_4')
for i in range(16):
    tiles[i] = []

tile_2 = pygame.image.load(os.getcwd() + '\\py2048_assets\\tiles\\2048_2.jpg')
tile_4 = pygame.image.load(os.getcwd() + '\\py2048_assets\\tiles\\2048_4.jpg')
tile_8 = pygame.image.load(os.getcwd() + '\\py2048_assets\\tiles\\2048_8.jpg')
tile_16 = pygame.image.load(os.getcwd() + '\\py2048_assets\\tiles\\2048_16.jpg')
tile_32 = pygame.image.load(os.getcwd() + '\\py2048_assets\\tiles\\2048_32.jpg')
tile_64 = pygame.image.load(os.getcwd() + '\\py2048_assets\\tiles\\2048_64.jpg')
tile_128 = pygame.image.load(os.getcwd() + '\\py2048_assets\\tiles\\2048_128.jpg')
tile_256 = pygame.image.load(os.getcwd() + '\\py2048_assets\\tiles\\2048_256.jpg')
tile_blank = pygame.image.load(os.getcwd() + '\\py2048_assets\\tiles\\2048_blank.jpg')

playermoved = False
game_end = False
score = 0


def main():
    global playermoved, game_end, score
    random_tile()
    try:
        while True:
            screen.fill(BACKGROUND)
            if playermoved:
                random_tile()
                playermoved = False
            draw_blocks()
            screen.blit(gamefont.render(f'Score: {score}', True, WHITE), (BOXWIDTH - 250, 0))
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen.blit(gamefont.render('Exiting...', True, WHITE), (0, 0))
                    pygame.display.update()
                    sys.exit()
                if keys[pygame.K_RIGHT]:
                    move_tile('right')
                elif keys[pygame.K_UP]:
                    move_tile('up')
                elif keys[pygame.K_LEFT]:
                    move_tile('left')
                elif keys[pygame.K_DOWN]:
                    move_tile('down')
            pygame.display.update()
    except Exception as e:
        messagebox.showerror('Error', f'Py2048 has encountered a fatal error and cannot continue:\n {e}')


def random_tile():
    global random_tiles, game_end
    templist1 = []
    for atile in tiles:
        if not tiles[atile]:
            templist1.append(atile)
    if not templist1:
        gameover()
        game_end = True
    tiles[random.choice(templist1)] = [random.choice(random_tiles)]
    # print(tiles)


def draw_blocks():
    for item in tiles:
        if tiles[item] and item % 2 != 0 or item % 4 == 0 and tiles[item]:
            screen.blit(eval(tiles[item][0]), (255 + (item % 4) * 133, 5 + int(item / 4) * 133))
        elif tiles[item]:
            screen.blit(eval(tiles[item][0]), (255 + 266, 5 + int(item / 4) * 133))
        else:
            screen.blit(tile_blank, (255 + (item % 4) * 133, 5 + int(item / 4) * 133))


def move_tile(direction):
    global playermoved, score
    if direction == 'right':
        item: int
        for iteration in range(3):
            for item in tiles:
                if iteration == 0 and tiles[item] and item == 2 or item == 6 or item == 10 or item == 14:
                    if not tiles[item + 1]:
                        tiles[item + 1] = tiles[item]
                        tiles[item] = []
                    elif tiles[item + 1] == tiles[item]:
                        tiles[item + 1] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                if iteration == 1 and tiles[item] and item == 1 or item == 5 or item == 9 or item == 13:
                    if not tiles[item + 2] and not tiles[item + 1]:
                        tiles[item + 2] = tiles[item]
                        tiles[item] = []
                    elif tiles[item + 2] == tiles[item] and not tiles[item + 1]:
                        tiles[item + 2] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                    elif not tiles[item + 1]:
                        tiles[item + 1] = tiles[item]
                        tiles[item] = []
                    elif tiles[item + 1] == tiles[item]:
                        tiles[item + 1] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                if iteration == 2 and tiles[item] and item == 0 or item == 4 or item == 8 or item == 12:
                    if not tiles[item + 3] and not tiles[item + 2] and not tiles[item + 1]:
                        tiles[item + 3] = tiles[item]
                        tiles[item] = []
                    elif tiles[item + 3] == tiles[item] and not tiles[item + 2] and not tiles[item + 1]:
                        tiles[item + 3] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                    elif not tiles[item + 2] and not tiles[item + 1]:
                        tiles[item + 2] = tiles[item]
                        tiles[item] = []
                    elif tiles[item + 2] == tiles[item] and not tiles[item + 1]:
                        tiles[item + 2] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                    elif not tiles[item + 1]:
                        tiles[item + 1] = tiles[item]
                        tiles[item] = []
                    elif tiles[item + 1] == tiles[item]:
                        tiles[item + 1] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
    elif direction == 'up':
        for iteration in range(3):
            for item in tiles:
                if iteration == 0 and item == 4 or item == 5 or item == 6 or item == 7:
                    if not tiles[item - 4]:
                        tiles[item - 4] = tiles[item]
                        tiles[item] = []
                    elif tiles[item - 4] == tiles[item]:
                        tiles[item - 4] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                if iteration == 1 and item == 8 or item == 9 or item == 10 or item == 11:
                    if not tiles[item - 8] and not tiles[item - 4]:
                        tiles[item - 8] = tiles[item]
                        tiles[item] = []
                    elif tiles[item - 8] == tiles[item] and not tiles[item - 4]:
                        tiles[item - 8] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                    elif not tiles[item - 4]:
                        tiles[item - 4] = tiles[item]
                        tiles[item] = []
                    elif tiles[item - 4] == tiles[item]:
                        tiles[item - 4] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                if iteration == 2 and item == 12 or item == 13 or item == 14 or item == 15:
                    if not tiles[item - 12] and not tiles[item - 8] and not tiles[item - 4]:
                        tiles[item - 12] = tiles[item]
                        tiles[item] = []
                    elif tiles[item - 12] == tiles[item] and not tiles[item - 8] and not tiles[item - 4]:
                        tiles[item - 12] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                    elif not tiles[item - 8] and not tiles[item - 4]:
                        tiles[item - 8] = tiles[item]
                        tiles[item] = []
                    elif tiles[item - 8] == tiles[item] and not tiles[item - 4]:
                        tiles[item - 8] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                    elif not tiles[item - 4]:
                        tiles[item - 4] = tiles[item]
                        tiles[item] = []
                    elif tiles[item - 4] == tiles[item]:
                        tiles[item - 4] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
    elif direction == 'left':
        for iteration in range(3):
            for item in tiles:
                if iteration == 0 and tiles[item] and item == 1 or item == 5 or item == 9 or item == 13:
                    if not tiles[item - 1]:
                        tiles[item - 1] = tiles[item]
                        tiles[item] = []
                    elif tiles[item - 1] == tiles[item]:
                        tiles[item - 1] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                if iteration == 1 and tiles[item] and item == 2 or item == 6 or item == 10 or item == 14:
                    if not tiles[item - 2] and not tiles[item - 1]:
                        tiles[item - 2] = tiles[item]
                        tiles[item] = []
                    elif tiles[item - 2] == tiles[item] and not tiles[item - 1]:
                        tiles[item - 2] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                    elif not tiles[item - 1]:
                        tiles[item - 1] = tiles[item]
                        tiles[item] = []
                    elif tiles[item - 1] == tiles[item]:
                        tiles[item - 1] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                if iteration == 2 and tiles[item] and item == 3 or item == 7 or item == 11 or item == 15:
                    if not tiles[item - 3] and not tiles[item - 2] and not tiles[item - 1]:
                        tiles[item - 3] = tiles[item]
                        tiles[item] = []
                    elif tiles[item - 3] == tiles[item] and not tiles[item - 2] and not tiles[item - 1]:
                        tiles[item - 3] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                    elif not tiles[item - 2] and not tiles[item - 1]:
                        tiles[item - 2] = tiles[item]
                        tiles[item] = []
                    elif tiles[item - 2] == tiles[item] and not tiles[item - 1]:
                        tiles[item - 2] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                    elif not tiles[item - 1]:
                        tiles[item - 1] = tiles[item]
                        tiles[item] = []
                    elif tiles[item - 1] == tiles[item]:
                        tiles[item - 1] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
    elif direction == 'down':
        for iteration in range(3):
            for item in tiles:
                if iteration == 0 and item == 8 or item == 9 or item == 10 or item == 11:
                    if not tiles[item + 4]:
                        tiles[item + 4] = tiles[item]
                        tiles[item] = []
                    elif tiles[item + 4] == tiles[item]:
                        tiles[item + 4] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                if iteration == 1 and item == 4 or item == 5 or item == 6 or item == 7:
                    if not tiles[item + 8] and not tiles[item + 4]:
                        tiles[item + 8] = tiles[item]
                        tiles[item] = []
                    elif tiles[item + 8] == tiles[item] and not tiles[item + 4]:
                        tiles[item + 8] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                    elif not tiles[item + 4]:
                        tiles[item + 4] = tiles[item]
                        tiles[item] = []
                    elif tiles[item + 4] == tiles[item]:
                        tiles[item + 4] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                if iteration == 2 and item == 0 or item == 1 or item == 2 or item == 3:
                    if not tiles[item + 12] and not tiles[item + 8] and not tiles[item + 4]:
                        tiles[item + 12] = tiles[item]
                        tiles[item] = []
                    elif tiles[item + 12] == tiles[item] and not tiles[item + 8] and not tiles[item + 4]:
                        tiles[item + 12] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                    elif not tiles[item + 8] and not tiles[item + 4]:
                        tiles[item + 8] = tiles[item]
                        tiles[item] = []
                    elif tiles[item + 8] == tiles[item] and not tiles[item + 4]:
                        tiles[item + 8] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
                    elif not tiles[item + 4]:
                        tiles[item + 4] = tiles[item]
                        tiles[item] = []
                    elif tiles[item + 4] == tiles[item]:
                        tiles[item + 4] = [str(tiles[item][0]).split('_')[0] + '_' + str(int(str(tiles[item][0]).split('_')[1]) * 2)]
                        score += int(str(tiles[item][0]).split('_')[1]) * 2
                        tiles[item] = []
    playermoved = True


def gameover():
    global score
    screen.fill(BLACK)
    screen.blit(gamefont.render(f' Game Over. Score: {score}', True, WHITE),(0, BOXHEIGHT / 2))
    pygame.display.update()
    time.sleep(2)
    sys.exit()


if __name__ == '__main__':
    main()
