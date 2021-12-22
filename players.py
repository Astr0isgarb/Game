import pygame
import config

class FemaleAdventurer:
    def __init__(self, x, y,screen):
        self.pos = [x,y]
        self.screen = screen
        self.poses = {
            "attack0": pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAattack0.png"),(config.SCALE,config.SCALE)), 
            "attack1":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAattack1.png"),(config.SCALE,config.SCALE)),
            "attack2":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAattack2.png"),(config.SCALE,config.SCALE)),
            "attackKick":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAattackKick.png"),(config.SCALE,config.SCALE)),
            "duck":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAduck.png"),(config.SCALE,config.SCALE)),
            "fall":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAfall.png"),(config.SCALE,config.SCALE)),
            "hit":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAhit.png"),(config.SCALE,config.SCALE)),
            "idle":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAidle.png"),(config.SCALE,config.SCALE)),
            "jump":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAjump.png"),(config.SCALE,config.SCALE)),
            "run0":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fArun0.png"),(config.SCALE,config.SCALE)),
            "run1":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fArun1.png"),(config.SCALE,config.SCALE)),
            "run2":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fArun2.png"),(config.SCALE,config.SCALE)),
            "walk0":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAwalk0.png"),(config.SCALE,config.SCALE)),
            "walk1":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAwalk1.png"),(config.SCALE,config.SCALE)),
            "walk2":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAwalk2.png"),(config.SCALE,config.SCALE)),
            "walk3":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAwalk3.png"),(config.SCALE,config.SCALE)),
            "walk4":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAwalk4.png"),(config.SCALE,config.SCALE)),
            "walk5":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAwalk5.png"),(config.SCALE,config.SCALE)),
            "walk6":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAwalk6.png"),(config.SCALE,config.SCALE)),
            "walk7":pygame.transform.scale(pygame.image.load("playerSprites/Female adventurer/PNG/Poses HD/fAwalk7.png"),(config.SCALE,config.SCALE)),
        }
        self.r_walk = [self.poses["walk0"],self.poses["walk1"],self.poses["walk2"],self.poses["walk3"],self.poses["walk4"],self.poses["walk5"],self.poses["walk6"],self.poses["walk7"]]
        self.l_walk = [pygame.transform.flip(self.poses["walk0"],True,False),pygame.transform.flip(self.poses["walk1"],True,False),pygame.transform.flip(self.poses["walk2"],True,False),pygame.transform.flip(self.poses["walk3"],True,False),pygame.transform.flip(self.poses["walk4"],True,False),pygame.transform.flip(self.poses["walk5"],True,False),pygame.transform.flip(self.poses["walk6"],True,False),pygame.transform.flip(self.poses["walk7"],True,False)]
        self.r_attack = [self.poses['attack0'],self.poses['attack1'],self.poses['attack2']]
        self.l_attack = [pygame.transform.flip(self.poses['attack0'],True,False),pygame.transform.flip(self.poses['attack1'],True,False),pygame.transform.flip(self.poses['attack2'],True,False)]
        self.r_jump = [self.poses['jump'],self.poses['fall']]
        self.l_jump = [pygame.transform.flip(self.poses['jump'],True,False),pygame.transform.flip(self.poses['fall'],True,False)]
        self.r_run = [self.poses["run0"],self.poses['run1'],self.poses['run2']]
        self.l_run = [pygame.transform.flip(self.poses['run0'],True,False),pygame.transform.flip(self.poses['run1'],True,False),pygame.transform.flip(self.poses['run2'],True,False)]
        self.r_kick = self.poses['attackKick']
        self.l_kick = pygame.transform.flip(self.poses['attackKick'],True,False)
        self.hit = self.poses['hit']
        self.rect = pygame.Rect(self.pos[0] * config.SCALE,self.pos[1]*config.SCALE,config.SCALE,config.SCALE)
        self.main_img = self.poses["idle"]


    def update(self):
        pass
    
    def render(self,screen,image):
        screen.blit(image,self.rect)
        self.rect = pygame.Rect(self.pos[0] * config.SCALE,self.pos[1]*config.SCALE,config.SCALE,config.SCALE)
    
    def update_position(self,new_pos):
        self.pos[0] += new_pos[0]
        self.pos[1] += new_pos[1]


class FemalePerson:
    def __init__(self, x, y,screen):
        self.pos = [x,y]
        self.screen = screen
        self.poses = {
            "attack0": pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fattack0.png"),(config.SCALE,config.SCALE)), 
            "attack1":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fattack1.png"),(config.SCALE,config.SCALE)),
            "attack2":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fattack2.png"),(config.SCALE,config.SCALE)),
            "attackKick":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/FattackKick.png"),(config.SCALE,config.SCALE)),
            "duck":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fduck.png"),(config.SCALE,config.SCALE)),
            "fall":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Ffall.png"),(config.SCALE,config.SCALE)),
            "hit":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fhit.png"),(config.SCALE,config.SCALE)),
            "idle":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fidle.png"),(config.SCALE,config.SCALE)),
            "jump":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fjump.png"),(config.SCALE,config.SCALE)),
            "run0":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Frun0.png"),(config.SCALE,config.SCALE)),
            "run1":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Frun1.png"),(config.SCALE,config.SCALE)),
            "run2":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Frun2.png"),(config.SCALE,config.SCALE)),
            "walk0":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fwalk0.png"),(config.SCALE,config.SCALE)),
            "walk1":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fwalk1.png"),(config.SCALE,config.SCALE)),
            "walk2":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fwalk2.png"),(config.SCALE,config.SCALE)),
            "walk3":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fwalk3.png"),(config.SCALE,config.SCALE)),
            "walk4":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fwalk4.png"),(config.SCALE,config.SCALE)),
            "walk5":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fwalk5.png"),(config.SCALE,config.SCALE)),
            "walk6":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fwalk6.png"),(config.SCALE,config.SCALE)),
            "walk7":pygame.transform.scale(pygame.image.load("playerSprites/Female person/PNG/Poses HD/Fwalk7.png"),(config.SCALE,config.SCALE)),
        }
        self.r_walk = [self.poses["walk0"],self.poses["walk1"],self.poses["walk2"],self.poses["walk3"],self.poses["walk4"],self.poses["walk5"],self.poses["walk6"],self.poses["walk7"]]
        self.l_walk = [pygame.transform.flip(self.poses["walk0"],True,False),pygame.transform.flip(self.poses["walk1"],True,False),pygame.transform.flip(self.poses["walk2"],True,False),pygame.transform.flip(self.poses["walk3"],True,False),pygame.transform.flip(self.poses["walk4"],True,False),pygame.transform.flip(self.poses["walk5"],True,False),pygame.transform.flip(self.poses["walk6"],True,False),pygame.transform.flip(self.poses["walk7"],True,False)]
        self.r_attack = [self.poses['attack0'],self.poses['attack1'],self.poses['attack2']]
        self.l_attack = [pygame.transform.flip(self.poses['attack0'],True,False),pygame.transform.flip(self.poses['attack1'],True,False),pygame.transform.flip(self.poses['attack2'],True,False)]
        self.r_jump = [self.poses['jump'],self.poses['fall']]
        self.l_jump = [pygame.transform.flip(self.poses['jump'],True,False),pygame.transform.flip(self.poses['fall'],True,False)]
        self.r_run = [self.poses["run0"],self.poses['run1'],self.poses['run2']]
        self.l_run = [pygame.transform.flip(self.poses['run0'],True,False),pygame.transform.flip(self.poses['run1'],True,False),pygame.transform.flip(self.poses['run2'],True,False)]
        self.r_kick = self.poses['attackKick']
        self.l_kick = pygame.transform.flip(self.poses['attackKick'],True,False)
        self.hit = self.poses['hit']
        self.rect = pygame.Rect(self.pos[0] * config.SCALE,self.pos[1]*config.SCALE,config.SCALE,config.SCALE)
        self.main_img = self.poses["idle"]


    def update(self):
        pass
    
    def render(self,screen,image):
        screen.blit(image,self.rect)
        self.rect = pygame.Rect(self.pos[0] * config.SCALE,self.pos[1]*config.SCALE,config.SCALE,config.SCALE)
    
    def update_position(self,new_pos):
        self.pos[0] += new_pos[0]
        self.pos[1] += new_pos[1]


class MaleAdventurer:
    def __init__(self, x, y,screen):
        self.pos = [x,y]
        self.screen = screen
        self.poses = {
            "attack0": pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAattack0.png"),(config.SCALE,config.SCALE)), 
            "attack1":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAattack1.png"),(config.SCALE,config.SCALE)),
            "attack2":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAattack2.png"),(config.SCALE,config.SCALE)),
            "attackKick":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAattackKick.png"),(config.SCALE,config.SCALE)),
            "duck":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAduck.png"),(config.SCALE,config.SCALE)),
            "fall":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAfall.png"),(config.SCALE,config.SCALE)),
            "hit":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAhit.png"),(config.SCALE,config.SCALE)),
            "idle":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAidle.png"),(config.SCALE,config.SCALE)),
            "jump":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAjump.png"),(config.SCALE,config.SCALE)),
            "run0":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mArun0.png"),(config.SCALE,config.SCALE)),
            "run1":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mArun1.png"),(config.SCALE,config.SCALE)),
            "run2":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mArun2.png"),(config.SCALE,config.SCALE)),
            "walk0":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAwalk0.png"),(config.SCALE,config.SCALE)),
            "walk1":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAwalk1.png"),(config.SCALE,config.SCALE)),
            "walk2":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAwalk2.png"),(config.SCALE,config.SCALE)),
            "walk3":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAwalk3.png"),(config.SCALE,config.SCALE)),
            "walk4":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAwalk4.png"),(config.SCALE,config.SCALE)),
            "walk5":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAwalk5.png"),(config.SCALE,config.SCALE)),
            "walk6":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAwalk6.png"),(config.SCALE,config.SCALE)),
            "walk7":pygame.transform.scale(pygame.image.load("playerSprites/Male adventurer/PNG/Poses HD/mAwalk7.png"),(config.SCALE,config.SCALE)),
        }
        self.r_walk = [self.poses["walk0"],self.poses["walk1"],self.poses["walk2"],self.poses["walk3"],self.poses["walk4"],self.poses["walk5"],self.poses["walk6"],self.poses["walk7"]]
        self.l_walk = [pygame.transform.flip(self.poses["walk0"],True,False),pygame.transform.flip(self.poses["walk1"],True,False),pygame.transform.flip(self.poses["walk2"],True,False),pygame.transform.flip(self.poses["walk3"],True,False),pygame.transform.flip(self.poses["walk4"],True,False),pygame.transform.flip(self.poses["walk5"],True,False),pygame.transform.flip(self.poses["walk6"],True,False),pygame.transform.flip(self.poses["walk7"],True,False)]
        self.r_attack = [self.poses['attack0'],self.poses['attack1'],self.poses['attack2']]
        self.l_attack = [pygame.transform.flip(self.poses['attack0'],True,False),pygame.transform.flip(self.poses['attack1'],True,False),pygame.transform.flip(self.poses['attack2'],True,False)]
        self.r_jump = [self.poses['jump'],self.poses['fall']]
        self.l_jump = [pygame.transform.flip(self.poses['jump'],True,False),pygame.transform.flip(self.poses['fall'],True,False)]
        self.r_run = [self.poses["run0"],self.poses['run1'],self.poses['run2']]
        self.l_run = [pygame.transform.flip(self.poses['run0'],True,False),pygame.transform.flip(self.poses['run1'],True,False),pygame.transform.flip(self.poses['run2'],True,False)]
        self.r_kick = self.poses['attackKick']
        self.l_kick = pygame.transform.flip(self.poses['attackKick'],True,False)
        self.hit = self.poses['hit']
        self.rect = pygame.Rect(self.pos[0] * config.SCALE,self.pos[1]*config.SCALE,config.SCALE,config.SCALE)
        self.main_img = self.poses["idle"]


    def update(self):
        pass
    
    def render(self,screen,image):
        screen.blit(image,self.rect)
        self.rect = pygame.Rect(self.pos[0] * config.SCALE,self.pos[1]*config.SCALE,config.SCALE,config.SCALE)
    
    def update_position(self,new_pos):
        self.pos[0] += new_pos[0]
        self.pos[1] += new_pos[1]


class MalePerson:
    def __init__(self, x, y,screen):
        self.pos = [x,y]
        self.screen = screen
        self.poses = {
            "attack0": pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mattack0.png"),(config.SCALE,config.SCALE)), 
            "attack1":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mattack1.png"),(config.SCALE,config.SCALE)),
            "attack2":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mattack2.png"),(config.SCALE,config.SCALE)),
            "attackKick":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/MattackKick.png"),(config.SCALE,config.SCALE)),
            "duck":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mduck.png"),(config.SCALE,config.SCALE)),
            "fall":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mfall.png"),(config.SCALE,config.SCALE)),
            "hit":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mhit.png"),(config.SCALE,config.SCALE)),
            "idle":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Midle.png"),(config.SCALE,config.SCALE)),
            "jump":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mjump.png"),(config.SCALE,config.SCALE)),
            "run0":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mrun0.png"),(config.SCALE,config.SCALE)),
            "run1":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mrun1.png"),(config.SCALE,config.SCALE)),
            "run2":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mrun2.png"),(config.SCALE,config.SCALE)),
            "walk0":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mwalk0.png"),(config.SCALE,config.SCALE)),
            "walk1":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mwalk1.png"),(config.SCALE,config.SCALE)),
            "walk2":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mwalk2.png"),(config.SCALE,config.SCALE)),
            "walk3":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mwalk3.png"),(config.SCALE,config.SCALE)),
            "walk4":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mwalk4.png"),(config.SCALE,config.SCALE)),
            "walk5":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mwalk5.png"),(config.SCALE,config.SCALE)),
            "walk6":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mwalk6.png"),(config.SCALE,config.SCALE)),
            "walk7":pygame.transform.scale(pygame.image.load("playerSprites/Male person/PNG/Poses HD/Mwalk7.png"),(config.SCALE,config.SCALE)),
        }
        self.r_walk = [self.poses["walk0"],self.poses["walk1"],self.poses["walk2"],self.poses["walk3"],self.poses["walk4"],self.poses["walk5"],self.poses["walk6"],self.poses["walk7"]]
        self.l_walk = [pygame.transform.flip(self.poses["walk0"],True,False),pygame.transform.flip(self.poses["walk1"],True,False),pygame.transform.flip(self.poses["walk2"],True,False),pygame.transform.flip(self.poses["walk3"],True,False),pygame.transform.flip(self.poses["walk4"],True,False),pygame.transform.flip(self.poses["walk5"],True,False),pygame.transform.flip(self.poses["walk6"],True,False),pygame.transform.flip(self.poses["walk7"],True,False)]
        self.r_attack = [self.poses['attack0'],self.poses['attack1'],self.poses['attack2']]
        self.l_attack = [pygame.transform.flip(self.poses['attack0'],True,False),pygame.transform.flip(self.poses['attack1'],True,False),pygame.transform.flip(self.poses['attack2'],True,False)]
        self.r_jump = [self.poses['jump'],self.poses['fall']]
        self.l_jump = [pygame.transform.flip(self.poses['jump'],True,False),pygame.transform.flip(self.poses['fall'],True,False)]
        self.r_run = [self.poses["run0"],self.poses['run1'],self.poses['run2']]
        self.l_run = [pygame.transform.flip(self.poses['run0'],True,False),pygame.transform.flip(self.poses['run1'],True,False),pygame.transform.flip(self.poses['run2'],True,False)]
        self.r_kick = self.poses['attackKick']
        self.l_kick = pygame.transform.flip(self.poses['attackKick'],True,False)
        self.hit = self.poses['hit']
        self.rect = pygame.Rect(self.pos[0] * config.SCALE,self.pos[1]*config.SCALE,config.SCALE,config.SCALE)
        self.main_img = self.poses["idle"]


    def update(self):
        pass
    
    def render(self,screen,image):
        screen.blit(image,self.rect)
        self.rect = pygame.Rect(self.pos[0] * config.SCALE,self.pos[1]*config.SCALE,config.SCALE,config.SCALE)
    
    def update_position(self,new_pos):
        self.pos[0] += new_pos[0]
        self.pos[1] += new_pos[1]


class Robot:
    def __init__(self, x, y,screen):
        self.pos = [x,y]
        self.screen = screen
        self.poses = {
            "attack0": pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rattack0.png"),(config.SCALE,config.SCALE)), 
            "attack1":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rattack1.png"),(config.SCALE,config.SCALE)),
            "attack2":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rattack2.png"),(config.SCALE,config.SCALE)),
            "attackKick":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/RattackKick.png"),(config.SCALE,config.SCALE)),
            "duck":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rduck.png"),(config.SCALE,config.SCALE)),
            "fall":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rfall.png"),(config.SCALE,config.SCALE)),
            "hit":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rhit.png"),(config.SCALE,config.SCALE)),
            "idle":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Ridle.png"),(config.SCALE,config.SCALE)),
            "jump":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rjump.png"),(config.SCALE,config.SCALE)),
            "run0":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rrun0.png"),(config.SCALE,config.SCALE)),
            "run1":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rrun1.png"),(config.SCALE,config.SCALE)),
            "run2":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rrun2.png"),(config.SCALE,config.SCALE)),
            "walk0":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rwalk0.png"),(config.SCALE,config.SCALE)),
            "walk1":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rwalk1.png"),(config.SCALE,config.SCALE)),
            "walk2":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rwalk2.png"),(config.SCALE,config.SCALE)),
            "walk3":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rwalk3.png"),(config.SCALE,config.SCALE)),
            "walk4":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rwalk4.png"),(config.SCALE,config.SCALE)),
            "walk5":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rwalk5.png"),(config.SCALE,config.SCALE)),
            "walk6":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rwalk6.png"),(config.SCALE,config.SCALE)),
            "walk7":pygame.transform.scale(pygame.image.load("playerSprites/Robot/PNG/Poses/Rwalk7.png"),(config.SCALE,config.SCALE)),
        }
        self.r_walk = [self.poses["walk0"],self.poses["walk1"],self.poses["walk2"],self.poses["walk3"],self.poses["walk4"],self.poses["walk5"],self.poses["walk6"],self.poses["walk7"]]
        self.l_walk = [pygame.transform.flip(self.poses["walk0"],True,False),pygame.transform.flip(self.poses["walk1"],True,False),pygame.transform.flip(self.poses["walk2"],True,False),pygame.transform.flip(self.poses["walk3"],True,False),pygame.transform.flip(self.poses["walk4"],True,False),pygame.transform.flip(self.poses["walk5"],True,False),pygame.transform.flip(self.poses["walk6"],True,False),pygame.transform.flip(self.poses["walk7"],True,False)]
        self.r_attack = [self.poses['attack0'],self.poses['attack1'],self.poses['attack2']]
        self.l_attack = [pygame.transform.flip(self.poses['attack0'],True,False),pygame.transform.flip(self.poses['attack1'],True,False),pygame.transform.flip(self.poses['attack2'],True,False)]
        self.r_jump = [self.poses['jump'],self.poses['fall']]
        self.l_jump = [pygame.transform.flip(self.poses['jump'],True,False),pygame.transform.flip(self.poses['fall'],True,False)]
        self.r_run = [self.poses["run0"],self.poses['run1'],self.poses['run2']]
        self.l_run = [pygame.transform.flip(self.poses['run0'],True,False),pygame.transform.flip(self.poses['run1'],True,False),pygame.transform.flip(self.poses['run2'],True,False)]
        self.r_kick = self.poses['attackKick']
        self.l_kick = pygame.transform.flip(self.poses['attackKick'],True,False)
        self.hit = self.poses['hit']
        self.rect = pygame.Rect(self.pos[0] * config.SCALE,self.pos[1]*config.SCALE,config.SCALE,config.SCALE)
        self.main_img = self.poses["idle"]


    def update(self):
        pass
    
    def render(self,screen,image):
        screen.blit(image,self.rect)
        self.rect = pygame.Rect(self.pos[0] * config.SCALE,self.pos[1]*config.SCALE,config.SCALE,config.SCALE)
    
    def update_position(self,new_pos):
        self.pos[0] += new_pos[0]
        self.pos[1] += new_pos[1]


class Zombie:
    def __init__(self, x, y,screen):
        self.pos = [x,y]
        self.screen = screen
        self.poses = {
            "attack0": pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zattack0.png"),(config.SCALE,config.SCALE)), 
            "attack1":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zattack1.png"),(config.SCALE,config.SCALE)),
            "attack2":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zattack2.png"),(config.SCALE,config.SCALE)),
            "attackKick":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/ZattackKick.png"),(config.SCALE,config.SCALE)),
            "duck":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zduck.png"),(config.SCALE,config.SCALE)),
            "fall":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zfall.png"),(config.SCALE,config.SCALE)),
            "hit":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zhit.png"),(config.SCALE,config.SCALE)),
            "idle":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zidle.png"),(config.SCALE,config.SCALE)),
            "jump":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zjump.png"),(config.SCALE,config.SCALE)),
            "run0":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zrun0.png"),(config.SCALE,config.SCALE)),
            "run1":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zrun1.png"),(config.SCALE,config.SCALE)),
            "run2":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zrun2.png"),(config.SCALE,config.SCALE)),
            "walk0":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zwalk0.png"),(config.SCALE,config.SCALE)),
            "walk1":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zwalk1.png"),(config.SCALE,config.SCALE)),
            "walk2":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zwalk2.png"),(config.SCALE,config.SCALE)),
            "walk3":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zwalk3.png"),(config.SCALE,config.SCALE)),
            "walk4":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zwalk4.png"),(config.SCALE,config.SCALE)),
            "walk5":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zwalk5.png"),(config.SCALE,config.SCALE)),
            "walk6":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zwalk6.png"),(config.SCALE,config.SCALE)),
            "walk7":pygame.transform.scale(pygame.image.load("playerSprites/Zombie/PNG/Poses HD/Zwalk7.png"),(config.SCALE,config.SCALE)),
        }
        self.r_walk = [self.poses["walk0"],self.poses["walk1"],self.poses["walk2"],self.poses["walk3"],self.poses["walk4"],self.poses["walk5"],self.poses["walk6"],self.poses["walk7"]]
        self.l_walk = [pygame.transform.flip(self.poses["walk0"],True,False),pygame.transform.flip(self.poses["walk1"],True,False),pygame.transform.flip(self.poses["walk2"],True,False),pygame.transform.flip(self.poses["walk3"],True,False),pygame.transform.flip(self.poses["walk4"],True,False),pygame.transform.flip(self.poses["walk5"],True,False),pygame.transform.flip(self.poses["walk6"],True,False),pygame.transform.flip(self.poses["walk7"],True,False)]
        self.r_attack = [self.poses['attack0'],self.poses['attack1'],self.poses['attack2']]
        self.l_attack = [pygame.transform.flip(self.poses['attack0'],True,False),pygame.transform.flip(self.poses['attack1'],True,False),pygame.transform.flip(self.poses['attack2'],True,False)]
        self.r_jump = [self.poses['jump'],self.poses['fall']]
        self.l_jump = [pygame.transform.flip(self.poses['jump'],True,False),pygame.transform.flip(self.poses['fall'],True,False)]
        self.r_run = [self.poses["run0"],self.poses['run1'],self.poses['run2']]
        self.l_run = [pygame.transform.flip(self.poses['run0'],True,False),pygame.transform.flip(self.poses['run1'],True,False),pygame.transform.flip(self.poses['run2'],True,False)]
        self.r_kick = self.poses['attackKick']
        self.l_kick = pygame.transform.flip(self.poses['attackKick'],True,False)
        self.hit = self.poses['hit']
        self.rect = pygame.Rect(self.pos[0] * config.SCALE,self.pos[1]*config.SCALE,config.SCALE,config.SCALE)
        self.main_img = self.poses["idle"]


    def update(self):
        pass
    
    def render(self,screen,image):
        screen.blit(image,self.rect)
        self.rect = pygame.Rect(self.pos[0] * config.SCALE,self.pos[1]*config.SCALE,config.SCALE,config.SCALE)
    
    def update_position(self,new_pos):
        self.pos[0] += new_pos[0]
        self.pos[1] += new_pos[1]
