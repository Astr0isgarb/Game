import pygame
from game_state import GameState
from players import FemaleAdventurer, FemalePerson, MaleAdventurer, MalePerson, Robot, Zombie
import config

class Game:
    def __init__(self,screen):
        self.screen = screen
        self.game_state = GameState.NONE
        self.on_player_select_screen = True
        self.playing = False
        self.playing2 = False
        self.done = False
        
        # Player 1
        self.p1walkCount = 0
        self.p1attackCount = 0
        self.p1attack = False
        self.p1right = False
        self.p1left = False
        self.p1isJump = False
        self.p1jumpCount = 10
        self.p1jumpCount2 = 0
        self.p1run = False
        self.p1runCount = 0
        self.p1kick = False
        self.p1kickCount = 0

        # Player 2
        self.p2walkCount = 0
        self.p2attackCount = 0
        self.p2attack = False
        self.p2right = False
        self.p2left = False
        self.p2isJump = False
        self.p2jumpCount = 10
        self.p2jumpCount2 = 0
        self.p2run = False
        self.p2runCount = 0
        self.p2kick = False
        self.p2kickCount = 0

    def setup(self):
        self.game_state = GameState.RUNNING
        self.objects= []


    def update(self):
        if self.on_player_select_screen:
            mouse = pygame.mouse.get_pos()
            rect = pygame.Rect(0,0,config.WIDTH,config.HEIGHT)
            image = (pygame.transform.scale(pygame.image.load("maps/map_select_screen.png"),(config.WIDTH, config.HEIGHT)))
            self.screen.blit(image,rect)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 30 <= mouse[0] <=240 and 180 <= mouse[1] <= 480:
                        self.map_pick = "map1"
                        self.on_player_select_screen = False
                    
                    if 400 <= mouse[0] <=610 and 180 <= mouse[1] <= 480:
                        self.map_pick = "map2"
                        self.on_player_select_screen = False

                    if 740 <= mouse[0] <=950 and 180 <= mouse[1] <= 480:
                        self.map_pick = "map3"
                        self.on_player_select_screen = False

        if not self.on_player_select_screen and not self.done:
            rect = pygame.Rect(0,0,config.WIDTH,config.HEIGHT)
            image = (pygame.transform.scale(pygame.image.load("maps/player_select_screen.png"),(config.WIDTH, config.HEIGHT)))
            self.screen.blit(image,rect)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    try:
                        if event.key == pygame.K_q:
                            
                            self.player1 = FemaleAdventurer(1,(config.HEIGHT-config.SCALE-config.THING_SCALE)/config.SCALE,self.screen)
                            self.objects.append(self.player1)
                            self.playing = True
                    except:pass
                    try:
                        if event.key == pygame.K_w:
                            
                            self.player1 = FemalePerson(1,(config.HEIGHT-config.SCALE-config.THING_SCALE)/config.SCALE,self.screen)
                            self.objects.append(self.player1)
                            self.playing = True
                    except:pass
                    try:
                        if event.key == pygame.K_a:
                            
                            self.player1 = MaleAdventurer(1,(config.HEIGHT-config.SCALE-config.THING_SCALE)/config.SCALE,self.screen)
                            self.objects.append(self.player1)
                            self.playing = True
                    except:pass
                    try:
                        if event.key == pygame.K_s:
                            
                            self.player1 = MalePerson(1,(config.HEIGHT-config.SCALE-config.THING_SCALE)/config.SCALE,self.screen)
                            self.objects.append(self.player1)
                            self.playing = True
                    except:pass
                    try:
                        if event.key == pygame.K_z:
                            
                            self.player1 = Robot(1,(config.HEIGHT-config.SCALE-config.THING_SCALE)/config.SCALE,self.screen)
                            self.objects.append(self.player1)
                            self.playing = True
                    except:pass
                    try:
                        if event.key == pygame.K_x:
                            
                            self.player1 = Zombie(1,(config.HEIGHT-config.SCALE-config.THING_SCALE)/config.SCALE,self.screen)
                            self.objects.append(self.player1)
                            self.playing = True
                    except:pass
                    # Player 2
                    try:
                        if event.key == pygame.K_y:
                            
                            self.player2 = FemaleAdventurer(11,(config.HEIGHT-config.SCALE-config.THING_SCALE)/config.SCALE,self.screen)
                            self.objects.append(self.player2)
                            self.playing2 = True
                    except:pass    
                    try:
                        if event.key == pygame.K_u:
                            
                            self.player2 = FemalePerson(11,(config.HEIGHT-config.SCALE-config.THING_SCALE)/config.SCALE,self.screen)
                            self.objects.append(self.player2)
                            self.playing2 = True
                    except:pass
                    try:
                        if event.key == pygame.K_h:
                            
                            self.player2 = MaleAdventurer(11,(config.HEIGHT-config.SCALE-config.THING_SCALE)/config.SCALE,self.screen)
                            self.objects.append(self.player2)
                            self.playing2 = True
                    except:pass
                    try:
                        if event.key == pygame.K_j:
                            
                            self.player2 = MalePerson(11,(config.HEIGHT-config.SCALE-config.THING_SCALE)/config.SCALE,self.screen)
                            self.objects.append(self.player2)
                            self.playing2 = True
                    except:pass
                    try:
                        if event.key == pygame.K_n:
                            
                            self.player2 = Robot(11,(config.HEIGHT-config.SCALE-config.THING_SCALE)/config.SCALE,self.screen)
                            self.objects.append(self.player2)
                            self.playing2 = True
                    except:pass
                    try:
                        if event.key == pygame.K_m:
                            
                            self.player2 = Zombie(11,(config.HEIGHT-config.SCALE-config.THING_SCALE)/config.SCALE,self.screen)
                            self.objects.append(self.player2)
                            self.playing2 = True
                    except:pass
        if self.playing and self.playing2:
            self.done = True
            self.load_map(self.map_pick)
            self.handle_events()
            self.player_movements()
    
    def handle_events(self):
        keys = pygame.key.get_pressed()
        

        # Player 1
        if keys[pygame.K_d] and (self.player1.pos[0]*config.SCALE)+config.THING_SCALE + 10 <= config.WIDTH:
            self.player1.update_position([.05,0])
            self.p1right = True
            self.p1left = False

        if keys[pygame.K_a] and self.player1.pos[0]*config.THING_SCALE >0:
            self.player1.update_position([-.05,0])
            self.p1left = True
            self.p1right = False

        if keys[pygame.K_LSHIFT] and self.p1left and self.player1.pos[0]*config.THING_SCALE >0:
            self.player1.update_position([-.15,0])
            self.p1run = True
        
        if keys[pygame.K_LSHIFT] and self.p1right and (self.player1.pos[0]*config.SCALE)+config.THING_SCALE + 10 <= config.WIDTH:
            self.player1.update_position([.15,0])
            self.p1run = True


        if not keys[pygame.K_LSHIFT] or not self.p1right or not self.p1left:
            if not keys[pygame.K_a]: 
                if not keys[pygame.K_d]:
                    if not self.p1isJump:
                        self.player1.render(self.screen,self.player1.main_img)
                        self.p1right= False
                        self.p1left = False
                        self.p1walkCount = 0
                        self.p1run = False

        # Player 2

        if keys[pygame.K_RIGHT] and (self.player2.pos[0]*config.SCALE)+config.THING_SCALE + 10 <= config.WIDTH:
            self.player2.update_position([.05,0])
            self.p2right = True
            self.p2left = False

        if keys[pygame.K_LEFT] and self.player2.pos[0]*config.THING_SCALE >0:
            self.player2.update_position([-.05,0])
            self.p2left = True
            self.p2right = False

        if keys[pygame.K_RCTRL] and self.p2left and self.player2.pos[0]*config.THING_SCALE >0:
            self.player2.update_position([-.15,0])
            self.p2run = True
        
        if keys[pygame.K_RCTRL] and self.p2right and (self.player2.pos[0]*config.SCALE)+config.THING_SCALE + 10 <= config.WIDTH:
            self.player2.update_position([.15,0])
            self.p2run = True


        if not keys[pygame.K_RIGHT]:
            if not keys[pygame.K_LEFT]:
                if not keys[pygame.K_RCTRL] or not self.p2right or not self.p2left:
                    if not self.p2isJump:
                        self.player2.render(self.screen,self.player2.main_img)
                        self.p2right= False
                        self.p2left = False
                        self.p2walkCount = 0
                        self.p2run = False
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED

            if event.type == pygame.KEYDOWN:
                
                # Player 1
                if event.key == pygame.K_TAB:
                    self.p1attack = True
                    self.p1attackCount = 0
            
                if self.p1isJump == False:
                    if event.key == pygame.K_w:
                        self.p1isJump = True
                        self.p1right = False 
                        self.p1left = False
                
                if event.key == pygame.K_q:
                    self.p1kick = True
                        
                # Player 2
                if event.key == pygame.K_RSHIFT:
                    self.p2attack = True
                    self.p2attackCount = 0
            
                if self.p2isJump == False:
                    if event.key == pygame.K_UP:
                        self.p2isJump = True
                        self.p2right = False 
                        self.p2left = False
                
                if event.key == pygame.K_RETURN:
                    self.p2kick = True


    def player_movements(self):
        # Player 1
        if self.p1walkCount +1 >= 27:
            self.p1walkCount = 0
        if self.p1attackCount +1 >= 14:
            self.p1attackCount = 0
            self.p1attack = False
        if self.p1runCount + 1 >= 14:
            self.p1runCount = 0
        if self.p1kickCount + 1>= 14:
            self.p1kickCount = 0
            self.p1kick = False

        if self.p1run and self.p1right and not self.p1isJump:
            self.player1.render(self.screen,self.player1.r_run[(self.p1runCount//5)-1])
            self.p1runCount +=1 
        
        elif self.p1right and self.p1kick and not self.p1isJump:
            self.player1.render(self.screen,self.player1.r_kick)
            self.p1kickCount += 1
        
        elif self.p1right and self.p1attack:
            self.player1.render(self.screen,self.player1.r_attack[(self.p1attackCount//5)-1])
            self.p1attackCount += 1
        
        elif self.p1right and not self.p1isJump:
            self.player1.render(self.screen,self.player1.r_walk[(self.p1walkCount//3)-1])
            self.p1walkCount += 1

        if self.p1run and self.p1left and not self.p1isJump:
            self.player1.render(self.screen,self.player1.l_run[(self.p1runCount//5)-1])
            self.p1runCount +=1 

        elif self.p1left and self.p1kick and not self.p1isJump:
            self.player1.render(self.screen,self.player1.l_kick)
            self.p1kickCount += 1

        elif self.p1left and self.p1attack:
            self.player1.render(self.screen,self.player1.l_attack[(self.p1attackCount//5)-1])
            self.p1attackCount += 1

        elif self.p1left and not self.p1isJump:
            self.player1.render(self.screen,self.player1.l_walk[(self.p1walkCount//3)-1])
            self.p1walkCount +=1 
        
        if self.p1isJump:
            if self.p1jumpCount >= -10:
                neg = 1
                if self.p1jumpCount <0 :
                    neg = -1
                
                self.player1.pos[1] -= (self.p1jumpCount**2*.01*neg)
                if self.p1right:
                    self.player1.render(self.screen,self.player1.r_jump[(self.p1jumpCount2//10)-1])
                elif self.p1left:
                    self.player1.render(self.screen,self.player1.l_jump[(self.p1jumpCount2//10)-1])
                else:
                    self.player1.render(self.screen,self.player1.r_jump[(self.p1jumpCount2//10)-1])

                self.p1jumpCount -= 1
                self.p1jumpCount2 += 1
            else:
                self.p1jumpCount = 10
                self.p1isJump = False
                self.p1jumpCount2 = 0

        # Player 2

        if self.p2walkCount +1 >= 27:
            self.p2walkCount = 0
        if self.p2attackCount +1 >= 14:
            self.p2attackCount = 0
            self.p2attack = False
        if self.p2runCount + 1 >= 14:
            self.p2runCount = 0
        if self.p2kickCount + 1>= 14:
            self.p2kickCount = 0
            self.p2kick = False

        if self.p2run and self.p2right and not self.p2isJump:
            self.player2.render(self.screen,self.player2.r_run[(self.p2runCount//5)-1])
            self.p2runCount +=1 
        
        elif self.p2right and self.p2kick and not self.p2isJump:
            self.player2.render(self.screen,self.player2.r_kick)
            self.p2kickCount += 1
        
        elif self.p2right and self.p2attack:
            self.player2.render(self.screen,self.player2.r_attack[(self.p2attackCount//5)-1])
            self.p2attackCount += 1
        
        elif self.p2right and not self.p2isJump:
            self.player2.render(self.screen,self.player2.r_walk[(self.p2walkCount//3)-1])
            self.p2walkCount += 1

        if self.p2run and self.p2left and not self.p2isJump:
            self.player2.render(self.screen,self.player2.l_run[(self.p2runCount//5)-1])
            self.p2runCount +=1 

        elif self.p2left and self.p2kick and not self.p2isJump:
            self.player2.render(self.screen,self.player2.l_kick)
            self.p2kickCount += 1

        elif self.p2left and self.p2attack:
            self.player2.render(self.screen,self.player2.l_attack[(self.p2attackCount//5)-1])
            self.p2attackCount += 1

        elif self.p2left and not self.p2isJump:
            self.player2.render(self.screen,self.player2.l_walk[(self.p2walkCount//3)-1])
            self.p2walkCount +=1 
        
        if self.p2isJump:
            if self.p2jumpCount >= -10:
                neg = 1
                if self.p2jumpCount <0 :
                    neg = -1
                
                self.player2.pos[1] -= (self.p2jumpCount**2*.01*neg)
                if self.p2right:
                    self.player2.render(self.screen,self.player2.r_jump[(self.p2jumpCount2//10)-1])
                elif self.p2left:
                    self.player2.render(self.screen,self.player2.l_jump[(self.p2jumpCount2//10)-1])
                else:
                    self.player2.render(self.screen,self.player2.r_jump[(self.p2jumpCount2//10)-1])

                self.p2jumpCount -= 1
                self.p2jumpCount2 += 1
            else:
                self.p2jumpCount = 10
                self.p2isJump = False
                self.p2jumpCount2 = 0
    
    
    
    def load_map(self,map):
        self.map = []
        self.bg = []
        with open("maps/"+map+"_bg.txt") as f:
            string = f.read()
            self.bg.append(string)
            f.close()
        
        with open("maps/"+map+".txt") as f:
            for i in f:
                self.map_line = []
                count = 0
                for x in range(len(i)-1):
                    self.map_line.append(i[count])
                    count += 1
                self.map.append(self.map_line)
            f.close()

        rect = pygame.Rect(0,0,config.WIDTH,config.HEIGHT)
        image = backgrounds[self.bg[0]]
        self.screen.blit(image,rect)
        
        self.y_pos = 0
        for i in self.map:
            self.x_pos = 0
            for x in i:
                try: 
                    image = map_tiles[x]
                    rect =pygame.Rect(self.x_pos*config.THING_SCALE,self.y_pos*config.THING_SCALE,config.THING_SCALE,config.THING_SCALE)
                    self.screen.blit(image,rect)
                    self.x_pos += 1
                    self.objects.append(rect)
                
                except:
                    self.x_pos += 1
            self.y_pos += 1
        
        


        

        

backgrounds = {
    "Desert1" : pygame.transform.scale(pygame.image.load("backGrounds/Desert1.png"),(config.WIDTH,config.HEIGHT)),
    "Desert2": pygame.transform.scale(pygame.image.load("backGrounds/Desert2.png"),(config.WIDTH,config.HEIGHT)),
    "Fall" : pygame.transform.scale(pygame.image.load("backGrounds/Fall.png"),(config.WIDTH,config.HEIGHT)),
    "Forest" : pygame.transform.scale(pygame.image.load("backGrounds/Forest.png"),(config.WIDTH,config.HEIGHT)),
    "Grass1" : pygame.transform.scale(pygame.image.load("backGrounds/Grass1.png"),(config.WIDTH,config.HEIGHT)),
    "Grass2" : pygame.transform.scale(pygame.image.load("backGrounds/Grass2.png"),(config.WIDTH,config.HEIGHT)),
    "Land" : pygame.transform.scale(pygame.image.load("backGrounds/Land.png"),(config.WIDTH,config.HEIGHT)),
    "Shroom" : pygame.transform.scale(pygame.image.load("backGrounds/Shroom.png"),(config.WIDTH,config.HEIGHT))
}

map_tiles = {
    "1": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Planet/planetLeft.png"),(config.THING_SCALE,config.THING_SCALE)),
    "2": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Planet/planetMid.png"),(config.THING_SCALE,config.THING_SCALE)),
    "3": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Planet/planetRight.png"),(config.THING_SCALE,config.THING_SCALE)),
    "4": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Planet/planetHalf_left.png"),(config.THING_SCALE,config.THING_SCALE)),
    "5": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Planet/planetHalf_mid.png"),(config.THING_SCALE,config.THING_SCALE)),
    "6": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Planet/planetHalf_right.png"),(config.THING_SCALE,config.THING_SCALE)),
    "q": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Sand/sandLeft.png"),(config.THING_SCALE,config.THING_SCALE)),
    "w": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Sand/sandMid.png"),(config.THING_SCALE,config.THING_SCALE)),
    "e": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Sand/sandRight.png"),(config.THING_SCALE,config.THING_SCALE)),
    "r": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Sand/sandHalf_left.png"),(config.THING_SCALE,config.THING_SCALE)),
    "t": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Sand/sandHalf_mid.png"),(config.THING_SCALE,config.THING_SCALE)),
    "y": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Sand/sandHalf_right.png"),(config.THING_SCALE,config.THING_SCALE)),
    "a": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Dirt/dirtLeft.png"),(config.THING_SCALE,config.THING_SCALE)),
    "s": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Dirt/dirtMid.png"),(config.THING_SCALE,config.THING_SCALE)),
    "d": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Dirt/dirtRight.png"),(config.THING_SCALE,config.THING_SCALE)),
    "f": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Dirt/dirtHalf_left.png"),(config.THING_SCALE,config.THING_SCALE)),
    "g": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Dirt/dirtHalf_mid.png"),(config.THING_SCALE,config.THING_SCALE)),
    "h": pygame.transform.scale(pygame.image.load("tileSprites/PNG/Ground/Dirt/dirtHalf_right.png"),(config.THING_SCALE,config.THING_SCALE)),
}