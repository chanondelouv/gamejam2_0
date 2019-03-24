#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""

import pygame
from pygame.locals import *
import Louis
import test
import time
import ice_bucket
color = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#from classes import *
#from constantes import *  
def main():
    pygame.init()
    
    #Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((693, 626))
#    fenetre = pygame.transform.scale(fenetre, (600, 600))
    
    #Chargement et collage du fond
    picture = pygame.image.load("image_accueil.jpg")
#    picture = pygame.transform.scale(picture, (1280, 720))
    
    #Rafraîchissement de l'écran
#    pygame.display.flip()
    
    #BOUCLE INFINIE
    continuer = 1
    while continuer:
        accueil = pygame.image.load("image_accueil.png").convert()
        fenetre.blit(accueil, (0,0))
#        myfont = pygame.font.SysFont("Comic Sans MS", 45)
        
        image = pygame.Surface([50, 50])
        image.fill(BLUE)
        fenetre.blit(image, (330,300))
        pygame.display.flip()
        pygame.mixer.init() #initialisation de la musique
        pygame.mixer.music.load("intro.wav")
        pygame.mixer.music.play()
        continuer_jeu = 1
        continuer_accueil = 1
        while continuer_accueil:
            #Limitation de vitesse de la boucle
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                #Si l'utilisateur quitte, on met les variables 
                #de boucle à 0 pour n'en parcourir aucune et fermer
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    continuer_accueil = 0
                    continuer_jeu = 0
                    continuer = 0
                    #Variable de choix du niveau
                    choix = 0
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN and event.pos[0] < 380 and event.pos[0] >330 and event.pos[1] < 350 and event.pos[1] >300:
                    retour = pygame.image.load("retour.png").convert()
                    fenetre.blit(retour, (0,0))
                    pygame.mixer.init() #initialisation de la musique
                    pygame.mixer.music.load("chrono.wav")
                    pygame.mixer.music.play()
                    pygame.display.flip()
#                    print('ok')
                    time.sleep(3)
                    fenetre = pygame.display.set_mode((634, 404))
                    thefloor = pygame.image.load("bucket.jpg").convert()
                    fenetre.blit(thefloor, (0,0))
                    pygame.mixer.init()
                    pygame.mixer.music.load("shower.wav")
                    pygame.mixer.music.play()
                    pygame.display.flip()
                    time.sleep(4)
                    ice_bucket.main()




        #on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
#        if choix != 0:
#            #Chargement du fond
#            fond = pygame.image.load(image_fond).convert()
#            #Génération d'un niveau à partir d'un fichier
#            niveau = Niveau(choix)
#            niveau.generer()
#            niveau.afficher(fenetre)
#            #Création de Donkey Kong
#            dk = Perso("images/dk_droite.png", "images/dk_gauche.png", "images/dk_haut.png", "images/dk_bas.png", niveau)
main()