import numpy as np
import pygame
from math import *
import random
import Louis
import time
# Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FOND=(248,136,75)
 
# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

BLOC_WIDTH=50
BLOC_HEIGHT=10
COTE_WIDTH=100
l=3
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
        global l
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
#        width = 40
#        height = 60
#        self.image = pygame.Surface([width, height])
#        self.image.fill(RED)
        self.image = pygame.image.load("image/Idle(1).png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 100))
        self.life=l
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None
 
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
        global l
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        block_hit_list_lave = pygame.sprite.spritecollide(self, self.level.platform_list_lave, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
        for block in block_hit_list_lave:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            print("LOST")
            l-=1
            
            pygame.mixer.init() #initialisation de la musique
            a=random.randint(0,2)
            if(a==1):
                pygame.mixer.music.load("aie.wav")
            else:
                pygame.mixer.music.load("animejaponaissensuel.wav")
            pygame.mixer.music.load("vent.wav")
            pygame.mixer.music.play()
            time.sleep(0.5)
            main()
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        block_hit_list_lave = pygame.sprite.spritecollide(self, self.level.platform_list_lave, False)

        #print(pygame.sprite.spritecollide(self, self.level.platform_list, False))
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
            
        for block in block_hit_list_lave:
            # Reset our position based on the top/bottom of the object.
            l-=1
            pygame.mixer.init() #initialisation de la musique
            a=random.randint(0,2)
            if(a==1):
                pygame.mixer.music.load("aie.wav")
            else:
                pygame.mixer.music.load("animejaponaissensuel.wav")
            pygame.mixer.music.play()
            time.sleep(0.5)
#            life-=1
            main()
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
        
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 0.8
        else:
            self.change_y += 1
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        platform_hit_list_lave = pygame.sprite.spritecollide(self, self.level.platform_list_lave, False)

        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:

            self.change_y = -25
            
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list_lave) > 0 or self.rect.bottom >= SCREEN_HEIGHT:

            self.change_y = -25
            
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.image = pygame.image.load("image/Walk(2)l.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.change_x = -9
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.image = pygame.image.load("image/Walk(2)r.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.change_x = 9
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.image = pygame.image.load("image/Idle(1).png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 100))
        self.change_x = 0
 
 
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height, var): #variable ajouté!!
        # var = True si lave
        # var = False si pas lave
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()
        
        
        if var==1:
            self.image = pygame.image.load("stone.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(width, height))
 
            self.rect = self.image.get_rect()
        elif var==2:
            self.image = pygame.image.load("Volcano.jpg").convert_alpha()
            self.image = pygame.transform.scale(self.image,(width, height))
 
            # Set a referance to the image rect.
            self.rect = self.image.get_rect()         
        elif var==3:
            self.image = pygame.image.load("lava.jpg").convert_alpha()
            self.image = pygame.transform.scale(self.image,(width, height))
 
            # Set a referance to the image rect.
            self.rect = self.image.get_rect()
 
 
class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player, valeurs):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.platform_list_lave = pygame.sprite.Group() #pour la lave

        self.player = player
        self.valeurs = valeurs
         
        # Background image
        self.background = None
 
    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.platform_list_lave.update()

 
    def draw(self, screen):
        """ Draw everything on this level. """
        global l
        # Draw the background
        
        screen.fill(FOND)
        pygame.font.init() #initialisation du texte de fond 
        font=pygame.font.Font(None,36)
        text= font.render("The Floor is Lava Challenge 2017",1,(0,0,0))
        screen.blit(text,(50,20))

        if l==0:
            pygame.display.quit()
            pygame.quit()
            
        elif l==1:
            coeur = pygame.image.load("coeur.png").convert_alpha()

            screen.blit(coeur, (800,20))
            
            self.platform_list.draw(screen)
            self.platform_list_lave.draw(screen)
            
        elif l==2:
            coeur = pygame.image.load("coeur.png").convert_alpha()

            screen.blit(coeur, (800,20))
            screen.blit(coeur,(840,20))
            
            self.platform_list.draw(screen)
            self.platform_list_lave.draw(screen)
            
        else:            
            coeur = pygame.image.load("coeur.png").convert_alpha()
            screen.blit(coeur, (800,20))
            screen.blit(coeur,(840,20))
            screen.blit(coeur,(880,20))
            self.platform_list.draw(screen)
            self.platform_list_lave.draw(screen) 
        

def valeur():
    boo = [2,2,2,2,2,2,1,1] #if 2 lave
    boosol=[1,2,2,2,2,2]
    boocote=[1,1,2,2,2,2]
    val = [[random.randint(150,SCREEN_WIDTH-300), 600, boo.pop(random.randrange(len(boo)))],
            [random.randint(150,SCREEN_WIDTH-300), 600, boo.pop(random.randrange(len(boo)))],
            [random.randint(150,SCREEN_WIDTH-300), 500, boo.pop(random.randrange(len(boo)))],
            [random.randint(150,SCREEN_WIDTH-300), 500,boo.pop(random.randrange(len(boo)))],
            [random.randint(150,SCREEN_WIDTH-300), 400,boo.pop(random.randrange(len(boo)))],
            [random.randint(150,SCREEN_WIDTH-300), 300,boo.pop(random.randrange(len(boo)))],
            [random.randint(150,SCREEN_WIDTH-300), 200,boo.pop(random.randrange(len(boo)))],
            [random.randint(150,SCREEN_WIDTH-300), 100,boo.pop(random.randrange(len(boo)))],
            [0, SCREEN_HEIGHT-50, boosol.pop(random.randrange(len(boosol)))],#sol
            [200, SCREEN_HEIGHT-50, boosol.pop(random.randrange(len(boosol)))],
            [400, SCREEN_HEIGHT-50, boosol.pop(random.randrange(len(boosol)))],
            [600, SCREEN_HEIGHT-50, boosol.pop(random.randrange(len(boosol)))],
            [800, SCREEN_HEIGHT-50, boosol.pop(random.randrange(len(boosol)))],
            [1000, SCREEN_HEIGHT-50, boosol.pop(random.randrange(len(boosol)))],
            [0, SCREEN_HEIGHT-150, boocote.pop(random.randrange(len(boocote)))],#cote
            [0, (2*(SCREEN_HEIGHT)/3)-150, boocote.pop(random.randrange(len(boocote)))],
            [0, ((SCREEN_HEIGHT)/3)-150, boocote.pop(random.randrange(len(boocote)))],
            [SCREEN_WIDTH-150, SCREEN_HEIGHT-150, boocote.pop(random.randrange(len(boocote)))],
            [SCREEN_WIDTH-150,(2*(SCREEN_HEIGHT)/3)-150, boocote.pop(random.randrange(len(boocote)))],
            [SCREEN_WIDTH-150,((SCREEN_HEIGHT)/3)-150, boocote.pop(random.randrange(len(boocote)))],
            ]   
    return val             
 
# Create platforms for the level
# tout vert
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player, valeurs):
        """ Create level 1. """
    
        # Array with width, height, x, and y of platform
#        valeurs = valeur()
        level = [[ BLOC_WIDTH, BLOC_HEIGHT,valeurs[0][0],valeurs[0][1], 1],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[1][0],valeurs[1][1], 1],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[2][0],valeurs[2][1], 1],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[3][0],valeurs[3][1], 1],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[4][0],valeurs[4][1], 1],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[5][0],valeurs[5][1], 1],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[6][0],valeurs[6][1], 1],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[7][0],valeurs[7][1], 1],
                 [ 200, 100,valeurs[8][0],valeurs[8][1], 1],#sol
                 [ 200, 100,valeurs[9][0],valeurs[9][1], 1],
                 [ 200, 100,valeurs[10][0],valeurs[10][1], 1],
                 [ 200, 100,valeurs[11][0],valeurs[11][1], 1],
                 [ 200, 100,valeurs[12][0],valeurs[12][1], 1],
                 [ 200, 100,valeurs[13][0],valeurs[13][1], 1],
                 [ 150, BLOC_HEIGHT,valeurs[14][0],valeurs[14][1], 1],#cote
                 [ 150, BLOC_HEIGHT,valeurs[15][0],valeurs[15][1], 1],
                 [ 150, BLOC_HEIGHT,valeurs[16][0],valeurs[16][1], 1],
                 [ 150, BLOC_HEIGHT,valeurs[17][0],valeurs[17][1], 1],
                 [ 150, BLOC_HEIGHT,valeurs[18][0],valeurs[18][1], 1],
                 [ 150, BLOC_HEIGHT,valeurs[19][0],valeurs[19][1], 1],
                 ]
        
        # Call the parent constructor
        Level.__init__(self, player, valeurs)
        
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1],platform[4]) # platform[i] = sprite => colonne et pas ligne!
            block.rect.x = platform[2] #coor x
            block.rect.y = platform[3] #coor y
            block.player = self.player
            if platform[4]==1 or platform[4]==2:     
                self.platform_list.add(block)
            else:
                self.platform_list_lave.add(block)
                
                
# Create platforms for the level
# vert et clignotant
class Level_02(Level):
    """ Definition for level 2. """
 
    def __init__(self, player, valeurs):
        """ Create level 2. """
 

        # Array with width, height, x, and y of platform
        
        level = [[ BLOC_WIDTH, BLOC_HEIGHT,valeurs[0][0],valeurs[0][1], valeurs[0][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[1][0],valeurs[1][1], valeurs[1][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[2][0],valeurs[2][1], valeurs[2][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[3][0],valeurs[3][1], valeurs[3][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[4][0],valeurs[4][1], valeurs[4][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[5][0],valeurs[5][1], valeurs[5][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[6][0],valeurs[6][1], valeurs[6][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[7][0],valeurs[7][1], valeurs[7][2]],
                 [ 200, 100,valeurs[8][0],valeurs[8][1], valeurs[8][2]],#sol
                 [ 200, 100,valeurs[9][0],valeurs[9][1], valeurs[9][2]],
                 [ 200, 100,valeurs[10][0],valeurs[10][1], valeurs[10][2]],
                 [ 200, 100,valeurs[11][0],valeurs[11][1], valeurs[11][2]],
                 [ 200, 100,valeurs[12][0],valeurs[12][1], valeurs[12][2]],
                 [ 200, 100,valeurs[13][0],valeurs[13][1], valeurs[13][2]],
                 [ 150, BLOC_HEIGHT,valeurs[14][0],valeurs[14][1], valeurs[14][2]],#cote
                 [ 150, BLOC_HEIGHT,valeurs[15][0],valeurs[15][1], valeurs[15][2]],
                 [ 150, BLOC_HEIGHT,valeurs[16][0],valeurs[16][1], valeurs[16][2]],
                 [ 150, BLOC_HEIGHT,valeurs[17][0],valeurs[17][1], valeurs[17][2]],
                 [ 150, BLOC_HEIGHT,valeurs[18][0],valeurs[18][1], valeurs[18][2]],
                 [ 150, BLOC_HEIGHT,valeurs[19][0],valeurs[19][1], valeurs[19][2]],
                 ]
        
        # Call the parent constructor
        Level.__init__(self, player, valeurs)
        
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1],platform[4]) # platform[i] = sprite => colonne et pas ligne!
            block.rect.x = platform[2] #coor x
            block.rect.y = platform[3] #coor y
            block.player = self.player
            if platform[4]==1 or platform[4]==2:     
                self.platform_list.add(block)
            else:
                self.platform_list_lave.add(block)
                
                
# Create platforms for the level
# lave et vert
class Level_03(Level):
    """ Definition for level 3. """
 
    def __init__(self, player, valeurs):
        """ Create level 3. """
 

        # Array with width, height, x, and y of platform

        for i in range(len(valeurs)):
            if valeurs[i][2]==2:
                valeurs[i][2]=3
        
        # Array with width, height, x, and y of platform
        level = [[ BLOC_WIDTH, BLOC_HEIGHT,valeurs[0][0],valeurs[0][1], valeurs[0][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[1][0],valeurs[1][1], valeurs[1][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[2][0],valeurs[2][1], valeurs[2][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[3][0],valeurs[3][1], valeurs[3][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[4][0],valeurs[4][1], valeurs[4][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[5][0],valeurs[5][1], valeurs[5][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[6][0],valeurs[6][1], valeurs[6][2]],
                 [ BLOC_WIDTH, BLOC_HEIGHT,valeurs[7][0],valeurs[7][1], valeurs[7][2]],
                 [ 200, 100,valeurs[8][0],valeurs[8][1], valeurs[8][2]],#sol
                 [ 200, 100,valeurs[9][0],valeurs[9][1], valeurs[9][2]],
                 [ 200, 100,valeurs[10][0],valeurs[10][1], valeurs[10][2]],
                 [ 200, 100,valeurs[11][0],valeurs[11][1], valeurs[11][2]],
                 [ 200, 100,valeurs[12][0],valeurs[12][1], valeurs[12][2]],
                 [ 200, 100,valeurs[13][0],valeurs[13][1], valeurs[13][2]],
                 [ 150, BLOC_HEIGHT,valeurs[14][0],valeurs[14][1], valeurs[14][2]],#cote
                 [ 150, BLOC_HEIGHT,valeurs[15][0],valeurs[15][1], valeurs[15][2]],
                 [ 150, BLOC_HEIGHT,valeurs[16][0],valeurs[16][1], valeurs[16][2]],
                 [ 150, BLOC_HEIGHT,valeurs[17][0],valeurs[17][1], valeurs[17][2]],
                 [ 150, BLOC_HEIGHT,valeurs[18][0],valeurs[18][1], valeurs[18][2]],
                 [ 150, BLOC_HEIGHT,valeurs[19][0],valeurs[19][1], valeurs[19][2]],
                 ]
        
        # Call the parent constructor
        Level.__init__(self, player, valeurs)
        
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1],platform[4]) # platform[i] = sprite => colonne et pas ligne!
            block.rect.x = platform[2] #coor x
            block.rect.y = platform[3] #coor y
            block.player = self.player
            if platform[4]==1 or platform[4]==2:     
                self.platform_list.add(block)
            else:
                self.platform_list_lave.add(block)
            
# Create platforms for the level     
#class Background(pygame.sprite.Sprite):
#    def __init__(self, image_file, location):
#        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
#        self.image = pygame.image.load(image_file)
#        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
#        self.rect = self.image.get_rect()
#        self.rect.left, self.rect.top = location
#        
def main():
    """ Main Program """
#    global l
#    if(l==0):
#        pygame.display.quit()
#        pygame.quit()
#   
#    if l==0:
#        fenetre = pygame.display.set_mode((693, 400))
#        youloose = pygame.image.load("youloose.png").convert()
#        fenetre.blit(youloose, (0,0))
#        
#        pygame.mixer.init() #initialisation de la musique
#        pygame.mixer.music.load("clap.wav")
#        pygame.mixer.music.play()
#        pygame.display.flip()
#        time.sleep(2)
#        pygame.quit()
    pygame.init()
    pygame.mixer.init() #initialisation de la musique
    pygame.mixer.music.load("sound.wav")
    pygame.mixer.music.play() #démarage de la musique
#    pygame.font.init() #initialisation du texte de fond 
#    font=pygame.font.Font(None,36)
#    text= font.render("Cheddar Challenge 2019",1,(0,0,0))
#    fond.blit(text,(10,10))
    val = valeur()
    
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Platformer Jumper")
 
    # Create the player
    
    player = Player()
    
    # Create all the levels
    level_list = []

    
    level_list.append(Level_01(player,val))
    level_list.append(Level_02(player,val))
    level_list.append(Level_03(player,val))
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    
        
    
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    ((SCREEN_HEIGHT)/3)-150
    player.rect.x = 10
    player.rect.y = ((SCREEN_HEIGHT)/3)-150 - player.rect.height
    active_sprite_list.add(player)
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    test=1
    boo = False
    a=0
    
    
    
    
    # -------- Main Program Loop -----------
    while not done and l!=0 and a!=3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
        
#            
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
#        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left < 0:
            player.rect.left = 0
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        


        modulo=10
        timep1=int(pygame.time.get_ticks() / 500 % modulo)
        timep2=int(pygame.time.get_ticks() / 500 % modulo)+ ((modulo-1)/3)%modulo
        timep3=int(pygame.time.get_ticks() / 500 % modulo)+ (2*(modulo-1))/3
#        print(timep1,timep2,timep3,test)
        #level 1
        if (timep1 == modulo-1 and test==1):
#            level_list=(Level_01(player,val),Level_02(player,val),Level_03(player,val))
            current_level=level_list[0]
#            level_list[0]=Level_01(player,val)
            test=0
#            print('ok1')
        if(timep1==0):
                test=3
           
        #level2    
        if (timep3 == modulo-1 and test==3):
            current_level=level_list[1]
#            level_list[1]=Level_02(player,val)
            test=0 
            boo=True
#            print('ok3')
        if(timep3==modulo and boo):
            test=2
            boo=False
                
        #level 3   
        if (timep2 == modulo-1 and test==2):
            current_level=level_list[2]
#            level_list=Level_03(player,val)
            test=0
            boo=True
#            print('ok2')
            val = valeur()
            level_list=(Level_01(player,val),Level_02(player,val),Level_03(player,val))
            
        if(timep2==modulo and boo):
            test=1
            boo=False
            a+=1
        
        player.level = current_level
  
                       
            
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    if l==0:
        fenetre = pygame.display.set_mode((693, 400))
        youloose = pygame.image.load("youloose.png").convert()
        fenetre.blit(youloose, (0,0))
        pygame.mixer.init() #initialisation de la musique
        pygame.mixer.music.load("clap.wav")
        pygame.mixer.music.play()
        pygame.display.flip()
        time.sleep(4)
        pygame.quit()
    else:
        fenetre = pygame.display.set_mode((700, 680))
        youloose = pygame.image.load("intro_cheddar.png").convert()
        fenetre.blit(youloose, (0,0))
        pygame.display.flip()
        pygame.mixer.init() #initialisation de la musique
        pygame.mixer.music.load("clap.wav")
        pygame.mixer.music.play()
        pygame.display.flip()
        time.sleep(4)
        Louis.main()
#if __name__ == "__main__":
#    main()