import pygame as py
from pygame.locals import *
import random
import time
import ice_bucket

def main():
    py.init()
    
    fenetre = py.display.set_mode((640, 480)) #création de la fenêtre
    
    fond = py.image.load("background.jpg").convert() #création de l'image de fond
    
    fenetre.blit(fond, (0,0)) #initialisation de l'image de fond sur ka fenêtre
    
    perso = py.image.load("rund.png").convert_alpha() #création de l'image du personnage principal tourné vers la droite
    persog = py.image.load("rung.png").convert_alpha() #création de l'image du personnage principal tourné vers la gauche
    persodead = py.image.load("dead.png").convert_alpha()
    
    cheddar= py.image.load("cheddar.png").convert_alpha() #création des images pour les cheddars
    cheddar2=py.image.load("cheddar.png").convert_alpha()
    cheddar3=py.image.load("cheddar.png").convert_alpha()
    cheddar4=py.image.load("cheddar.png").convert_alpha()
    
    coeur=py.image.load("coeur.png").convert_alpha() #création des images de coeur représentant les vies
    
    perso_x=0  # initialisation des coordonnées de bases du personnage et cheddar
    perso_y=380
    position_cheddar=(0,0) 
    
    py.font.init() #initialisation du texte de fond 
    font=py.font.Font(None,36)
    text= font.render("Cheddar Challenge 2019",1,(0,0,0))
    fond.blit(text,(10,10))
    
    #Rafraîchissement de l'écran
    py.display.flip()
    
    py.mixer.init() #initialisation de la musique
    py.mixer.music.load("son1.wav")
    py.mixer.music.play() #démarage de la musique
    
    py.key.set_repeat(20, 1) #fait en sorte de pouvoir rester appuyé pour bouger
    
    
    for a in range(0,3):
        continuer=1
        i=0 #variabbles évlouants en fonction de la chute de chaque fromage (respectivement 1,2,3 et 4)
        j=0
        k=0
        l=0
        count=0
        abscisse2=0
        abscisse3=0
        abscisse4=0
        droite=True
        while continuer:# and py.time.get_ticks()<90000:
            abscisse=random.randint(0,640) #initialisation de l'abscisse aléatoire de chaque fromage
            for i in range(0,480):
                if i==120:
                    abscisse2=random.randint(0,640)
                if i==240:
                    abscisse3=random.randint(0,640)
                if i==360:
                    abscisse4=random.randint(0,640)
                    
                for event in py.event.get(): 
                    if(event.type == QUIT):     #arrêt du programme si le bouton d'arrêt est pressé
                       continuer = 0  
                       py.quit()
                    if event.type == KEYDOWN:       #fait bouger le personnage à droite ou à gauche             
                       if event.key == K_RIGHT:
                            perso_x=perso_x+2
                            droite=True
                       if event.key == K_LEFT:
                            perso_x=perso_x-2
                            droite=False
    
                if i<120:
                    j=i+360
                else:
                    j=i-120
                if i<240:
                    k=i+240
                else:
                    k=i-240
                if i<360:
                    l=i+120
                else:
                    l=i-360
                        
                count=count+1 
                py.display.flip()
                position_cheddar=(abscisse,i)  #fait descendre les fromages
                position_cheddar2=(abscisse2,j)
                position_cheddar3=(abscisse3,k)
                position_cheddar4=(abscisse4,l)
                fenetre.blit(fond, (0,0))
                
                
                fenetre.blit(coeur, (600,0)) #fait en sorte d'avoir le nombre de vie correspondant
                if a<2 :
                    fenetre.blit(coeur, (560,0))
                if a<1:
                    fenetre.blit(coeur, (520,0))
                    
                    
                fenetre.blit(cheddar, position_cheddar)
                if droite:
                  fenetre.blit(perso, ((perso_x,perso_y)))
                else:
                    fenetre.blit(persog, ((perso_x,perso_y)))
                if count>120:
                    fenetre.blit(cheddar2,position_cheddar2)
                    if count>240:
                        fenetre.blit(cheddar3,position_cheddar3)
                        if count>360:
                            fenetre.blit(cheddar4,position_cheddar4)
                            
                            
                if (perso_x > (position_cheddar[0]-80) and perso_x < (position_cheddar[0]+25) and position_cheddar[1] >350 and position_cheddar[1]< 475) or (perso_x > (position_cheddar2[0]-80) and perso_x < (position_cheddar2[0]+25) and position_cheddar2[1] > 350 and count>120 and position_cheddar[1]< 475) or (perso_x > (position_cheddar3[0]-80) and perso_x < (position_cheddar3[0]+25) and position_cheddar3[1]>350 and count>240 and position_cheddar[1]< 475) or (perso_x > (position_cheddar4[0]-80) and perso_x < (position_cheddar4[0]+25) and position_cheddar4[1]>350 and count>360 and position_cheddar[1]< 475):   
                    py.mixer.init() #initialisation de la musique
                    py.mixer.music.load("cheddar.wav")
                    py.mixer.music.play()
                    fenetre.blit(fond, (0,0))
                    fenetre.blit(persodead,((perso_x,perso_y)))  #met le personnage en postition 'dead' et relance le jeu lorsque le personnage perd une vie( touche un fromage)
                    py.display.flip()   
                    time.sleep(2)
                    continuer=0
                    break
                time.sleep(.002)
    if a==2:
        fenetre = py.display.set_mode((693, 400))
        youloose = py.image.load("youloose.png").convert()
        fenetre.blit(youloose, (0,0))
        py.display.flip()
        py.mixer.init() #initialisation de la musique
        py.mixer.music.load("clap.wav")
        py.mixer.music.play()
        time.sleep(4)
        py.quit()
    else:
        py.quit()                
    
#main()