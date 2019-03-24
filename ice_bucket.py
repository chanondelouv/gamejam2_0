import pygame as py
from pygame.locals import *
import numpy as np 
import random
import time
import test
def main():
    py.init()
    continuer=1
    son = py.mixer.Sound("enclume.wav")
    
    fenetre = py.display.set_mode((1200, 700))
    fond = py.image.load("background1.jpg").convert()
    
    
    
    perso=py.image.load("rund.png").convert_alpha()
    persog=py.image.load("rung.png").convert_alpha()
    enfantok=py.image.load("ice_bucket1.png").convert_alpha()
    enfantmouille=py.image.load("ice_bucket4.png").convert_alpha()
    
    py.font.init() #initialisation du texte de fond 
    font=py.font.Font(None,36)
    text= font.render("Ice Bucket Challenge 2014",1,(0,0,0))
    fond.blit(text,(10,10))
    
    position_enfants=[(random.randint(0,1110),random.randint(0,570)),(random.randint(0,1110),random.randint(0,570)),(random.randint(0,1110),random.randint(0,570)),(random.randint(0,1110),random.randint(0,570)),(random.randint(0,1110),random.randint(0,570)),(random.randint(0,1110),random.randint(0,570)),(random.randint(0,1110),random.randint(0,570))]
    renverse=np.ones(7)
    perso_x=0
    perso_y=0
    droite=True
    
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, (perso_x,perso_y))
    py.display.flip()
    count=0
    py.key.set_repeat(20, 1)
    lastfalse=random.randint(0,6)
    renverse[lastfalse]=0
    pasttime=py.time.get_ticks()
    
    while continuer and count < 10:
        if (py.time.get_ticks() - pasttime) >= 700:
            pasttime=py.time.get_ticks()
            renverse[lastfalse]=1
            lastfalse=random.randint(0,6)
            renverse[lastfalse]=0
            
        for event in py.event.get():  #On parcours la liste de tous les événements reçus
            if(event.type == QUIT):     #Si un de ces événements est de type QUI 
                continuer = 0 
            if event.type == MOUSEMOTION:
                perso_x = event.pos[0]-20
                perso_y = event.pos[1]-20
    
    #        if event.type == KEYDOWN:       #fait bouger le personnage à droite ou à gauche             
    #            if event.key == K_RIGHT:
    #                perso_x=perso_x+2
    #                droite=True
    #            if event.key == K_LEFT:
    #                perso_x=perso_x-2
    #                droite=False
    #            if event.key == K_UP:
    #                perso_y=perso_y-2
    #            if event.key == K_DOWN:
    #                perso_y=perso_y+2
            if event.type == MOUSEBUTTONDOWN:
                if event.button==1:
                  if( perso_x > position_enfants[lastfalse][0]-90 and perso_x < position_enfants[lastfalse][0]+83 and perso_y < position_enfants[lastfalse][1]+100 and perso_y > position_enfants[lastfalse][1]-127):
                        count+=1
                        son.play()
                        position_enfants[lastfalse]=(random.randint(0,1110),random.randint(0,570))
        fenetre.blit(fond, (0,0))
        
        for i in range(0,6):
            if(renverse[i]):
                fenetre.blit(enfantok,position_enfants[i])
            else:
                fenetre.blit(enfantmouille,position_enfants[i])
        if droite:
            fenetre.blit(perso, ((perso_x,perso_y)))
        else:
            fenetre.blit(persog, ((perso_x,perso_y)))
        py.display.flip()  
    fenetre = py.display.set_mode((693, 623))
    thefloor = py.image.load("floor_is.jpg").convert()
    fenetre.blit(thefloor, (0,0))
    py.mixer.init() #initialisation de la musique
    py.mixer.music.load("grrr.wav")
    py.mixer.music.play()                    
    py.display.flip()
    time.sleep(4)
    test.main()