import pygame
import config
from game import Game
from game_state import GameState



pygame.init()


tiles = {
    "1": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Stone/stoneCenter.png"),(config.THING_SCALE,config.THING_SCALE)),
    "a": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_A.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "b": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_B.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "c": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_C.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "d": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_D.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "e": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_E.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "f": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_F.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "g": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_G.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "h": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_H.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "i": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_I.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "j": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_J.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "k": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_K.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "l": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_L.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "m": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_M.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "n": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_N.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "o": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_O.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "p": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_P.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "q": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_Q.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "r": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_R.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "s": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_S.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "t": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_T.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "u": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_U.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "v": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_V.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "w": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_W.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "x": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_X.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "y": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_Y.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "z": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_Z.png"),(config.LETTER_SCALE,config.LETTER_SCALE)),
    "A": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_A.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "B": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_B.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "C": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_C.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "D": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_D.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "E": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_E.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "F": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_F.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "G": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_G.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "H": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_H.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "I": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_I.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "J": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_J.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "K": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_K.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "L": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_L.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "M": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_M.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "N": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_N.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "O": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_O.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "P": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_P.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "Q": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_Q.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "R": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_R.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "S": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_S.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "T": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_T.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "U": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_U.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "V": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_V.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "W": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_W.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "X": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_X.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "Y": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_Y.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE)),
    "Z": pygame.transform.scale(pygame.image.load("letters/Yellow/letter_Z.png"),(config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE))
}


screen = pygame.display.set_mode((config.WIDTH,config.HEIGHT))
pygame.display.set_caption("2 Player Fighter")

clock = pygame.time.Clock()
game = Game(screen)
game.setup()

with open("maps/main_scr.txt") as f:
        map = []
        for i in f:
            map_line = []
            count =0
            for x in range((len(i)-1)):
                x = str(x)
                map_line.append(i[count])
                count += 1 
            map.append(map_line)

with open("maps/main_scr_txt.txt") as f:
    text = []
    for i in f:
        text_line = []
        count = 0
        for x in range(len(i)-1):
            x =str(x)
            text_line.append(i[count])
            count +=1
        text.append(text_line)
            
def load_text():
    y_pos = 3
    for i in text:
        x_pos = 1.5
        for x in i:
            if x.isupper() or x.isdigit():
                image = tiles[x]
                rect = pygame.Rect(x_pos*config.LARGE_LETTER_SCALE , y_pos*config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE,config.LARGE_LETTER_SCALE )
                screen.blit(image,rect)
            else:
                image = tiles[x]
                rect = pygame.Rect(x_pos*config.LETTER_SCALE+100, y_pos*config.LETTER_SCALE,config.LETTER_SCALE,config.LETTER_SCALE )
                screen.blit(image,rect)
            
            x_pos += 1
        y_pos += 1

def load_m():
    y_pos = 0
    for i in map:
        x_pos = 0
        for x in i:
            image = tiles[x]
            rect =pygame.Rect(x_pos*config.THING_SCALE,y_pos*config.THING_SCALE,config.THING_SCALE,config.THING_SCALE)
            screen.blit(image,rect)
            x_pos +=1 
        y_pos += 1

on_map_select_screen = False
on_player_select_screen = False
while game.game_state == GameState.RUNNING:
    if not on_map_select_screen:
        load_m()
        load_text()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    on_map_select_screen = True
    if on_map_select_screen:
        game.update()
    clock.tick(27)
    

    pygame.display.update()
    