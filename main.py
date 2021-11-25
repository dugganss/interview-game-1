###########
# ~IMPORTS~#
###########

# ~PYGAME MODULE IMPORTATION~#
import pygame

# ~EXTERNAL PYTHON FILES IMPORTATION~#
from settings import *

from player import Player

from enemy import Imp, DemonSoldier, Cacodemon, Marauder

from bullet import Bullet

from wall import Wall

from healthpotion import Healthpotion

from armour import Armour

from levelplatform import Levelplatform

from leveltext import Leveltext

from levelcomplete import Levelcomplete

from trigger import Trigger

# ~OTHER PYTHON MODULE IMPORTATION~#
import random

from pygame import mixer

import sys

import time

from pygame.locals import *

import re

#####################
# ~PYGAME INITIATION~#
#####################

pygame.init()

###################
# ~SCREEN CREATION~#
###################

# - I have created the size variable that holds the value of the height and width of the screen
#
# - WINDOW_W and WINDOW_H is defined in settings.py
#
# - I have also created the display and passed in the size variable
#
# - The name of the window is also given here

size = (WINDOW_W, WINDOW_H)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("DOOM 2D")

#################
# ~SPRITE GROUPS~#
#################

# - This is where I will create and define different sprite groups that will hold sprites that I will use for different purposes.

# "LIVING" SPRITES

players = pygame.sprite.Group()

enemies = pygame.sprite.Group()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# BULLETS

bulletsUp = pygame.sprite.Group()

bulletsDown = pygame.sprite.Group()

bulletsLeft = pygame.sprite.Group()

bulletsRight = pygame.sprite.Group()

allBullets = pygame.sprite.Group()

shotgunBullets = pygame.sprite.Group()

bulletsShotgunUpLeft = pygame.sprite.Group()

bulletsShotgunUpRight = pygame.sprite.Group()

bulletsShotgunDownLeft = pygame.sprite.Group()

bulletsShotgunDownRight = pygame.sprite.Group()

bulletsShotgunLeftUp = pygame.sprite.Group()

bulletsShotgunLeftDown = pygame.sprite.Group()

bulletsShotgunRightUp = pygame.sprite.Group()

bulletsShotgunRightDown = pygame.sprite.Group()

triggers = pygame.sprite.Group()

marauders = pygame.sprite.Group()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# WALLS

walls = pygame.sprite.Group()

blockade1s = pygame.sprite.Group()

blockade2s = pygame.sprite.Group()

blockade3s = pygame.sprite.Group()

blockade4s = pygame.sprite.Group()

blockade5s = pygame.sprite.Group()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PICKUPS

healthpotions = pygame.sprite.Group()

armours = pygame.sprite.Group()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# INTERACTABLE PLATFORMS

levelplatforms = pygame.sprite.Group()

levelcompletes = pygame.sprite.Group()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TEXT DISPLAY

leveltexts = pygame.sprite.Group()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ALL SPRITES

allsprites = pygame.sprite.Group()

####################
# ~DEFINING COLOURS~#
####################

# - This is where colours variables are created and given the RGB value for the colour that I selected

DARK_RED = (168, 32, 3)

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

DARK_GREY = (54, 55, 62)

LIGHT_GREY = (168, 168, 168)

YELLOW = (255, 255, 0)

##################
# ~CREATING LISTS~#
##################

# - This is where I will define lists

leaderboardList = ["", "", "", ""]

# ~CLOCK~#

# - The clock is how many times per second a loop will run. Here I have defined the name clock with the clock function.
#
# - Within the main game loop, I will give the clock a value. The loop will run that value amount of times per second.

clock = pygame.time.Clock()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


####################################
#                                  #
#         LOADING SCREEN           #
#                                  #
####################################

# - This screen will appear while the code is running and nothing is happening on screen.
# - it loads a background image and blits it to the screen and then blits some text to the screen that says 'LOADING...'

def LoadingScreen():
    Background = pygame.image.load('pauseback.png')
    Background = pygame.transform.scale(Background, (800, 600))
    screen.blit(Background, (0, 0))

    font = pygame.font.Font('8-BitMadness.ttf', 90)
    title = font.render("LOADING...", 1, DARK_RED)
    screen.blit(title, (240, 60))
    title = font.render("LOADING...", 1, WHITE)
    screen.blit(title, (237, 57))

    pygame.display.update()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#########################################
#                                       #
#         G     A     M     E           #
#                                       #
#########################################


def game(level, val):
    # - Loading screen is called here because for about half a second, the code is being run through and the game is in a
    #   frozen state. The loading screen just breaks it up so it is clear that the game is processing.

    LoadingScreen()

    ###################################
    #                                 #
    #  ~~GAME SPECIFIC PROCEDURES~~#  #
    #                                 #
    ###################################

    ################################
    # ~DELETE ALL SPRITES PROCEDURE~#
    ################################

    # - This is a function that when called will clear all sprite groups
    #
    # - This removes them from the game so that they are not interactable or viewable anymore
    #
    # - It will be called when the game loop is to end so that the sprites do not still exist when the loop is run again to play a different level.

    def DELETE_ALL_SPRITES():
        players.empty()
        enemies.empty()
        bulletsUp.empty()
        bulletsDown.empty()
        bulletsLeft.empty()
        bulletsRight.empty()
        allBullets.empty()
        walls.empty()
        healthpotions.empty()
        armours.empty()
        levelplatforms.empty()
        leveltexts.empty()
        levelcompletes.empty()
        blockade1s.empty()
        blockade2s.empty()
        blockade3s.empty()
        blockade4s.empty()
        blockade5s.empty()
        triggers.empty()

        ##################
        # ~PAUSE FUNCTION~#
        ##################

        # - pos1 pos2 and pos3 hold the colour of the titles
        #
        # - an event detects for a key press
        #
        # - if pos1 is yellow and the down key is pressed then pos1 turns white and pos2 turns yellow
        #
        # - if pos2 is yellow and the down key is pressed then pos3 turns yellow and pos2 turns white
        #
        # - if pos2 is yellow and the up key is pressed then pos1 turns yellow and pos2 turns white
        #
        # - if pos3 is yellow the the up key is pressed then pos2 turns yellow and pos3 turns white
        #
        # - if pos1 is yellow and the enter key is pressed then the pause loop will end, returning the player to the game loop
        #
        # - if pos2 is yellow and the enter key is pressed then all sprites will be deleted and the pause loop ends,
        #   it will also return True from the pause function which will end the game loop, this will take the player back
        #   to the hub
        #
        # - if pos3 is yellow and the enter key is pressed then all sprites will be deleted and the pause loop ends,
        #   it will also return False from the pause function which will call the menu function, this will take the player back
        #   to the menu. the leaderboard text file will also be updated.

    def pause():

        pos1 = YELLOW
        pos2 = WHITE
        pos3 = WHITE

        pausemenu = True
        while pausemenu:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pos1 == YELLOW:
                        if event.key == pygame.K_DOWN:
                            pos1 = WHITE
                            pos2 = YELLOW
                            pos3 = WHITE
                    elif pos2 == YELLOW:
                        if event.key == pygame.K_DOWN:
                            pos1 = WHITE
                            pos2 = WHITE
                            pos3 = YELLOW
                        elif event.key == pygame.K_UP:
                            pos1 = YELLOW
                            pos2 = WHITE
                            pos3 = WHITE
                    elif pos3 == YELLOW:
                        if event.key == pygame.K_UP:
                            pos1 = WHITE
                            pos2 = YELLOW
                            pos3 = WHITE
                    if event.key == pygame.K_RETURN:
                        if pos1 == YELLOW:
                            pausemenu = False
                        elif pos2 == YELLOW:
                            DELETE_ALL_SPRITES()
                            timeEnd = time.perf_counter()
                            totalTime = timeEnd - timeStart
                            leave = True
                            pausemenu = False
                            return leave
                        elif pos3 == YELLOW:
                            DELETE_ALL_SPRITES()
                            timeEnd = time.perf_counter()
                            totalTime = timeEnd - timeStart
                            leaderboardUpdate()
                            leave = False
                            pausemenu = False
                            return leave

            pauseBackground = pygame.image.load('pauseback.png')
            pauseBackground = pygame.transform.scale(pauseBackground, (800, 600))
            screen.blit(pauseBackground, (0, 0))

            font = pygame.font.Font('8-BitMadness.ttf', 90)
            text = font.render("PAUSED", 1, DARK_RED)
            screen.blit(text, (250, 150))

            font = pygame.font.Font('8-BitMadness.ttf', 70)
            text = font.render("RESUME", 2, pos1)
            overlaytext = font.render("RESUME", 1, DARK_RED)
            screen.blit(text, (50, 270))
            screen.blit(overlaytext, (48, 268))

            overlaytext = font.render("RETURN TO HUB", 2, DARK_RED)
            text = font.render("RETURN TO HUB", 2, pos2)
            screen.blit(text, (50, 350))
            screen.blit(overlaytext, (48, 348))

            overlaytext = font.render("MAIN MENU", 2, DARK_RED)
            text = font.render("MAIN MENU", 2, pos3)
            screen.blit(text, (50, 430))
            screen.blit(overlaytext, (48, 428))

            pygame.display.update()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #######################################
    # ~~CREATING DECORATIVE PLAYER SPRITE~~#
    #######################################

    # - This sprite will be created and then placed at the bottom of the screen.
    #
    # - because it has a different name to the main player sprite the logic below will not apply to it so it will not be able to be controlled
    #
    # - It will replicate the position that the other sprite is facing due to it being part of the player class

    player2 = Player()
    player2.enlarge()

    player2.rect.x = 365
    player2.rect.y = 495

    players.add(player2)

    ######################
    # ~~BACKGROUND MUSIC~~#
    ######################

    # - Here I load the background music at play it on a loop once the game is run.

    mixer.init()
    mixer.music.load('d_e1m1.mp3')
    mixer.music.play(-1)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    #################
    ##~~VARIABLES~~##
    #################

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    ##########################
    # ~ACCELERATION VARIABLES~#
    ##########################

    # - This is where I will define the varibales used to accelerate the player across the screen at an increasing rate.

    upAccel = 0

    downAccel = 0

    leftAccel = 0

    rightAccel = 0

    #############
    # ~DIRECTION~#
    #############

    # - This is where I will define the variable that keeps track of the direction that the player sprite is facing

    directioncheck = 0

    ############
    # ~COUNTERS~#
    ############

    # - This is where I will define counters that will be variables that increment in a loop so that I can keep track
    #   of certain information

    enemyMovementCounter = 0

    bulletCount = 0

    enemydead = 0

    # ~WEAPON SELECTION~#

    weapon = 0

    ##########
    # ~HEALTH~#
    ##########

    # - This is where I will define health variables for the sprites that have a health system

    playerHealth = 100

    playerArmour = 100

    ###########
    # ~GODMODE~#
    ###########

    # - This is where the GODMODE variable is defined, it is placed before the game function because it changes throughout
    #   the gameplay. However it must initially be false so that GODMODE isn't active by default

    GODMODE = False

    ##########
    # ~SOUNDS~#
    ##########

    # - This is where sound files that will be used will be defined
    #  (not backing tracking because these are sound effects)

    bulletSound = mixer.Sound('dspistol.wav')

    enemyInjuredSound = mixer.Sound('dsskldth.wav')

    enemyDeathSound = mixer.Sound('dspopain.wav')

    shotgunSound = mixer.Sound('dsshotgn.wav')

    weaponChange = mixer.Sound('170273__knova__change-weapon-sound.wav')

    ########
    # ~TIME~#
    ########

    # - This is where I will define the minute variable that will increment by one every time 60 seconds passes
    #
    # (for in game timer)

    minute = 0

    ######################
    # ~LEADERBOARD UPDATE~#
    ######################

    # - This is a function that will append the contents of the leaderboard list array into the leaderboard text file.
    #
    # - Basically whenever it is called the leaderboard text file will be updated with the name and scores of the play in that session

    def leaderboardUpdate():
        f = open("leaderboard.txt", "a")
        f.write(leaderboardList[0] + "           ")
        f.write(leaderboardList[1] + "           ")
        f.write(leaderboardList[2] + "           ")
        f.write(leaderboardList[3] + "\n")
        f.close()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    notHUB = False

    ##################
    # ~~LEVEL LAYOUT~~#
    ##################

    # - The game function is called with a parameter passed into it. This is what layout the game function will run on
    #
    # - The level layout variables are defined in settings.py
    #
    # - The loop below runs for each row and column of the 2d array that is passed into it so it looks at every index
    #
    # - There are 20 columns because i would like my sprites to be 40 pixels wide and 800(screen width)/40 = 20
    #
    # - There are 12 rows because i would like my sprites to be 40 pixels high and 600(screen height)/40 = 12
    #
    # - If the index that it is on is equal to 1 then an instance of the wall class will be created and it will be placed
    #   in the position of the row and column multiplied by grid_size. for instance if there is a 1 at row 5 column 3 then the wall
    #   be placed at x 120 and y 200 on screen
    #
    # - If the index that it is on is equal to 2 then an instance of the enemy class will be created and placed on screen in its position
    #   notHUB will also be set to True, this is so I am able to determine whether the HUB is open or not. I do this here because there
    #   will never be an enemy sprite in the HUB so if the game function is runnng with no enemy sprites then I will know that the HUB is
    #   loaded
    #
    # - If the index that it is on is equal to 3 then an instance of the player class will be created and placed on screen in its position
    #
    # - If the index that it is on is equal to 4 then an instance of the healthpotion class will be created and placed on screen in its position
    #
    # - If the index that it is on is equal to 5 then an instance of the armour class will be created and placed on screen in its position
    #
    # - If the index that it is on is equal to 6 then an instance of the levelplatform class will be created and placed on screen in its position
    #
    # - If the index that it is on is equal to 7 then an instance of the leveltext class will be created and placed on screen in its position
    #
    # - If the index that it is on is equal to 8 then an instance of the leveltext class will be created with the e1m2 function called on it
    #   and will then be placed on screen in its position
    #
    # - If the index that it is on is equal to 9 then an instance of the leveltext class will be created with the e1m3 function called on it
    #   and will then be placed on screen in its position
    #
    # - If the index that it is on is equal to "a" then an instance of the levelcomplete class will be created and will then be placed on screen in its position
    #
    # - If the index that it is on is equal to "move" then an instance of the wall class will be created and placed in its position
    #   then an instance of the leveltext class will be created with the instructionsmove function called on it, it will then created another level text
    #   iteration with the instructionsshoot function called on it and it wil be placed further along the x axis

    for col in range(20):
        for row in range(12):
            if level[row][col] == 1:
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)
            if level[row][col] == 2:
                enemy = Imp()
                enemy.rect.x = col * grid_size
                enemy.rect.y = row * grid_size
                enemies.add(enemy)
                allsprites.add(enemy)
                notHUB = True
            if level[row][col] == 3:
                player = Player()
                player.rect.x = col * grid_size
                player.rect.y = row * grid_size
                players.add(player)
                allsprites.add(player)
            if level[row][col] == 4:
                healthpotion = Healthpotion()
                healthpotion.rect.x = col * grid_size + random.randint(8, 20)
                healthpotion.rect.y = row * grid_size + random.randint(8, 15)
                healthpotions.add(healthpotion)
            if level[row][col] == 5:
                armour = Armour()
                armour.rect.x = col * grid_size + random.randint(8, 15)
                armour.rect.y = row * grid_size + random.randint(8, 10)
                armours.add(armour)
            if level[row][col] == 6:
                levelplatform = Levelplatform()
                levelplatform.rect.x = col * grid_size + 12
                levelplatform.rect.y = row * grid_size + 12
                levelplatforms.add(levelplatform)
            if level[row][col] == 7:
                leveltext = Leveltext()
                leveltext.rect.x = col * grid_size + 9
                leveltext.rect.y = row * grid_size + 5
                leveltexts.add(leveltext)
            if level[row][col] == 8:
                leveltext = Leveltext()
                leveltext.e1m2()
                leveltext.rect.x = col * grid_size + 9
                leveltext.rect.y = row * grid_size + 5
                leveltexts.add(leveltext)
            if level[row][col] == 9:
                leveltext = Leveltext()
                leveltext.e1m3()
                leveltext.rect.x = col * grid_size + 9
                leveltext.rect.y = row * grid_size + 5
                leveltexts.add(leveltext)
            if level[row][col] == "a":
                levelcomplete = Levelcomplete()
                levelcomplete.rect.x = col * grid_size + 12
                levelcomplete.rect.y = row * grid_size + 12
                levelcompletes.add(levelcomplete)
            if level[row][col] == "d":
                enemy = DemonSoldier()
                enemy.rect.x = col * grid_size
                enemy.rect.y = row * grid_size
                enemies.add(enemy)
                allsprites.add(enemy)
            if level[row][col] == "e":
                enemy = Cacodemon()
                enemy.rect.x = col * grid_size
                enemy.rect.y = row * grid_size
                enemies.add(enemy)
                allsprites.add(enemy)

            if level[row][col] == "move":
                wall = Wall()
                wall.rect.x = col * grid_size
                wall.rect.y = row * grid_size
                walls.add(wall)

                wasd = Leveltext()
                wasd.instructionsMove()
                wasd.rect.x = col * grid_size + 9
                wasd.rect.y = row * grid_size + 5
                leveltexts.add(wasd)

                arrows = Leveltext()
                arrows.instructionsShoot()
                arrows.rect.x = col * grid_size + 500
                arrows.rect.y = row * grid_size + 5
                leveltexts.add(arrows)
            if level[row][col] == "j":
                trigger = Trigger()
                trigger.rect.x = col * grid_size
                trigger.rect.y = row * grid_size
                triggers.add(trigger)
            if level[row][col] == "i":
                trigger = Trigger()
                trigger.rect.x = col * grid_size
                trigger.rect.y = row * grid_size
                triggers.add(trigger)
            if level[row][col] == "k":
                marauder = Marauder()
                marauder.rect.x = col * grid_size
                marauder.rect.y = row * grid_size
                enemies.add(marauder)
                allsprites.add(marauder)

            # ~BLOCKADES~#

            # - Blockades are barriers in the HUB that block the player from accessing the level platforms for levels they
            #   haven't unlocked yet
            #
            # - val is what is returned from the game function if a player completes a level
            #
            # - If the player has completed level 1 then val will be 1
            #
            # - If the player has completed level 2 then val will be 2
            #
            # - Otheriwse val will = 0
            #
            # - If val is less than 1 then it will check the HUB 2D array for "b", wherever b is in the 2D array, a blockade
            #   will be created and placed in the respective place on screen. This blockade will be added to the blockade1 sprite group
            #   and the wall sprite group
            #
            # - If val is less than 2 then it will check the HUB 2D array for "c", wherever c is in the 2D array, a blockade
            #   will be created and placed in the respective place on screen. This blockade will be added to the blockade2 sprite group
            #   and the wall sprite group
            #
            # - Blockades will have the same features as walls as they are in the wall sprite group
            #
            # - This logic means that if val is 0 then both sets of blockades will be present in the HUB
            #
            # - If val = 1 then only the second set of blockades will be present in the HUB
            #
            # - If val = 2 then there will be no blockades

            if val < 1:
                if level[row][col] == "b":
                    blockade1s.empty()
                    blockade1 = Wall()
                    blockade1.blockade()
                    blockade1.rect.x = col * grid_size
                    blockade1.rect.y = row * grid_size
                    blockade1s.add(blockade1)
                    walls.add(blockade1)

            if val < 2:
                if level[row][col] == "c":
                    blockade2s.empty()
                    blockade2 = Wall()
                    blockade2.blockade()
                    blockade2.rect.x = col * grid_size
                    blockade2.rect.y = row * grid_size
                    blockade2s.add(blockade2)
                    walls.add(blockade2)

            if val < 3:
                if level[row][col] == "f":
                    blockade3s.empty()
                    blockade3 = Wall()
                    blockade3.blockade()
                    blockade3.rect.x = col * grid_size
                    blockade3.rect.y = row * grid_size
                    blockade3s.add(blockade3)
                    walls.add(blockade3)

            if val < 4:
                if level[row][col] == "g":
                    blockade4s.empty()
                    blockade4 = Wall()
                    blockade4.blockade()
                    blockade4.rect.x = col * grid_size
                    blockade4.rect.y = row * grid_size
                    blockade4s.add(blockade4)
                    walls.add(blockade4)

            if val < 5:
                if level[row][col] == "h":
                    blockade5s.empty()
                    blockade5 = Wall()
                    blockade5.blockade()
                    blockade5.rect.x = col * grid_size
                    blockade5.rect.y = row * grid_size
                    blockade5s.add(blockade5)
                    walls.add(blockade5)

    enemyLength = len(enemies)

    ###############
    # ~TIMER START~#
    ###############

    # - This is where the timer for the game loop will start.

    timeStart = time.perf_counter()
    displayTimeStart = time.perf_counter()

    #######################
    # ~~~~~~GAME LOOP~~~~~~#
    #######################

    # - I have created a condition controlled loop that will run as long as the variable run is True, this is how the game will run.
    #
    # - Below that, is my event loop. I have a multitude of events types that it checks. They will be detailed below.

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            ##########################
            # ------------------------#
            # +~~~~~~GAME LOGIC~~~~~~+#
            # ------------------------#
            ##########################

            # (all code below here is for game logic)

            # (checks if the event type is a key press)#

            if event.type == pygame.KEYDOWN:

                ######################
                # ~GODMODE ACTIVATION~#
                ######################

                # - If the event key is 'x' then the GODMODE variable will = True
                #
                # - This ultimately means, if the x key is pressed GODMODE will be activated

                if event.key == pygame.K_x:
                    GODMODE = True

                # - If the event key is 'c' and GODMODE is True (already active) then GODMODE is False
                #
                # - playerHealth is reset and set to 50
                #
                # - playerArmour is reset and set to 50
                #
                # - The bulletCount variable is then reset to the amount of bullets that exist so that it can keep track of how many bullets are on screen
                #   I have to do this because the bulletCount variable does not keep track of how many bullets there are when GODMODE is active

                if event.key == pygame.K_c and GODMODE == True:
                    GODMODE = False
                    playerHealth = 50
                    playerArmour = 50
                    bulletCount = len(allBullets)

                ###########################
                # ~CALLING PAUSE PROCEDURE~#
                ###########################

                # - If the event key is "p" then the pause fucntion will be called.
                #
                # - Whatever is returned from the pause function will be stored in HUBorMENU
                #
                # - If HUBorMENU is True then the game loop will end causing the player to return to the HUB
                #
                # - If HUBorMENU is False then the menu function will run and return 4 which breaks the loop in the menu function
                #   that takes the player back to the HUB when a level ends.

                if event.key == pygame.K_p:
                    HUBorMENU = pause()
                    if HUBorMENU == True:
                        run = False
                        DELETE_ALL_SPRITES()
                        value = 0
                        return value
                    elif HUBorMENU == False:
                        DELETE_ALL_SPRITES()
                        menu()
                        return 4

                ########################################
                # ~CALLING LEADERBOARD UPDATE PROCEDURE~#
                ########################################

                # - leaderboardUpdate is defined on line 2112
                #
                # - It will be called if the event key is 'u' (if 'u' is pressed at any time).

                if event.key == pygame.K_u:
                    leaderboardUpdate()

                # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #############
                # ~WEAPONS~ #
                #############

                ######################
                # ~~WEAPON SELECTION~~#
                ######################

                # - If the space key is pressed at any point during gameplay, the weapon change sound will play
                #
                # - If weapon = 0 (which is is by default) then weapon will now = 1. This means that the shotgun will now be selected
                #
                # - if weapon = 1 then weapon will now = 0. This means the pistol will now be selected

                if event.key == pygame.K_SPACE:
                    weaponChange.play()
                    if weapon == 0:
                        weapon = 1
                    elif weapon == 1:
                        weapon = 0

                #####################
                # ~~PLAYER SHOOTING~~#
                #####################

                # - Written within the event loop so that only one input can be taken at a time instead of being able to hold key down and spam an input
                #
                # - If the UP key is pressed, it will be checked what value the weapon variable is
                #
                # - if weapon = 1 then an instance of the bullet class will be created and will be given the x and y coordinates of the players
                #   current position. (this will be its origin point)
                #
                # - This instance will be added to the bulletsShotgunUpLeft group and will be travelling upwards and diagonally to the left
                #
                # - Another instance of a bullet is then created and is given the same origin point however it will instead be added to the
                #   bulletsShotgunUpRight sprite group and will be travelling upwards and diagonally to the right
                #
                # - Another instance of the bullet is then created and given the same origin point but is added to the bulletsUp group and the allBullets group
                #   This bullet will be travelling upwards in a straight line. (it is the only bullet out of the three being added to the allBullets group because
                #   all of the bullets together count as one shot)
                #
                # - The bulletCount variable will be incremented by one to count one shot from the shotgun.
                #
                # - directioncheck will = 3 so the player sprite is facing upwards
                #
                # - The shotgun sound will then play
                #
                # - If weapon = 2 then a single instance of the bullet class will be created and placed at the player sprite's x and y positions.
                #   The bullet will also be added to the bulletsUp sprite group and the allBullets sprite group. (so it can be updated)
                #
                # - bulletCount will be incremented by one so that the amount of bullets can be kept track of.
                #
                # - directioncheck will = 3 which will change the position that the player sprite is facing.
                #
                # - The pistol sound effet will then play.
                #
                # - I gave the example of the up direction however the same logic is applied to all directions
                if GODMODE == True:
                    bulletCount = 0

                if bulletCount < 3:

                    # ~~UP DIRECTION SHOOTING~~#

                    if event.key == pygame.K_UP:

                        # ~SHOTGUN~#

                        if weapon == 1:
                            if bulletCount < 1:
                                bullet = Bullet()
                                bullet.rect.x = player.rect.x + 10
                                bullet.rect.y = player.rect.y
                                bulletsShotgunUpLeft.add(bullet)
                                shotgunBullets.add(bullet)
                                bullet = Bullet()
                                bullet.rect.x = player.rect.x + 10
                                bullet.rect.y = player.rect.y
                                bulletsShotgunUpRight.add(bullet)
                                shotgunBullets.add(bullet)
                                bullet = Bullet()
                                bullet.rect.x = player.rect.x + 10
                                bullet.rect.y = player.rect.y
                                bulletsUp.add(bullet)
                                allBullets.add(bullet)
                                bulletCount += 1
                                directioncheck = 3
                                shotgunSound.play()

                        # ~PISTOL~#

                        else:
                            bullet = Bullet()
                            bullet.rect.x = player.rect.x + 10
                            bullet.rect.y = player.rect.y
                            bulletsUp.add(bullet)
                            allBullets.add(bullet)
                            bulletCount += 1
                            directioncheck = 3
                            bulletSound.play()

                    # ~~DOWN DIRECTION SHOOTING~~#
                    if event.key == pygame.K_DOWN:

                        # ~SHOTGUN~#

                        if weapon == 1:
                            if bulletCount < 1:
                                bullet = Bullet()
                                bullet.rect.x = player.rect.x + 10
                                bullet.rect.y = player.rect.y
                                bulletsShotgunDownLeft.add(bullet)
                                shotgunBullets.add(bullet)
                                bullet = Bullet()
                                bullet.rect.x = player.rect.x + 10
                                bullet.rect.y = player.rect.y
                                bulletsShotgunDownRight.add(bullet)
                                shotgunBullets.add(bullet)
                                bullet = Bullet()
                                bullet.rect.x = player.rect.x + 10
                                bullet.rect.y = player.rect.y
                                bulletsDown.add(bullet)
                                allBullets.add(bullet)
                                bulletCount += 1
                                directioncheck = 4
                                shotgunSound.play()

                        # ~PISTOL~#

                        else:
                            bullet = Bullet()
                            bullet.rect.x = player.rect.x + 10
                            bullet.rect.y = player.rect.y
                            bulletsDown.add(bullet)
                            allBullets.add(bullet)
                            bulletCount += 1
                            directioncheck = 4
                            bulletSound.play()

                    # ~~LEFT DIRECTION SHOOTING~~#
                    if event.key == pygame.K_LEFT:

                        # ~SHOTGUN~#

                        if weapon == 1:
                            if bulletCount < 1:
                                bullet = Bullet()
                                bullet.rect.x = player.rect.x
                                bullet.rect.y = player.rect.y + 11
                                bulletsShotgunLeftUp.add(bullet)
                                shotgunBullets.add(bullet)
                                bullet = Bullet()
                                bullet.rect.x = player.rect.x
                                bullet.rect.y = player.rect.y + 11
                                bulletsShotgunLeftDown.add(bullet)
                                shotgunBullets.add(bullet)
                                bullet = Bullet()
                                bullet.rect.x = player.rect.x
                                bullet.rect.y = player.rect.y + 11
                                bulletsLeft.add(bullet)
                                allBullets.add(bullet)
                                bulletCount += 1
                                directioncheck = 2
                                shotgunSound.play()

                        # ~PISTOL~#

                        else:
                            bullet = Bullet()
                            bullet.rect.x = player.rect.x
                            bullet.rect.y = player.rect.y + 11
                            bulletsLeft.add(bullet)
                            allBullets.add(bullet)
                            bulletCount += 1
                            directioncheck = 2
                            bulletSound.play()

                    # ~~RIGHT DIRECTION SHOOTING~~#
                    if event.key == pygame.K_RIGHT:

                        # ~SHOTGUN~#

                        if weapon == 1:
                            if bulletCount < 1:
                                bullet = Bullet()
                                bullet.rect.x = player.rect.x + 30
                                bullet.rect.y = player.rect.y + 11
                                bulletsShotgunRightUp.add(bullet)
                                shotgunBullets.add(bullet)
                                bullet = Bullet()
                                bullet.rect.x = player.rect.x + 30
                                bullet.rect.y = player.rect.y + 11
                                bulletsShotgunRightDown.add(bullet)
                                shotgunBullets.add(bullet)
                                bullet = Bullet()
                                bullet.rect.x = player.rect.x + 30
                                bullet.rect.y = player.rect.y + 11
                                bulletsRight.add(bullet)
                                allBullets.add(bullet)
                                bulletCount += 1
                                directioncheck = 1
                                shotgunSound.play()

                        # ~PISTOL~#

                        else:
                            bullet = Bullet()
                            bullet.rect.x = player.rect.x + 30
                            bullet.rect.y = player.rect.y + 11
                            bulletsRight.add(bullet)
                            allBullets.add(bullet)
                            bulletCount += 1
                            directioncheck = 1
                            bulletSound.play()

        ####################################################
        # ~~DIRECTIONAL BULLET UPDATES AND BOUNDARY CHECKS~~#
        ####################################################

        # - The first line in any example checks if there are any bullets in the respective bullet group (e.g. bulletUp, bulletsShotgunLeftDown)
        #   so that the code isn't run with no bullets existing.
        #
        # - If there is a bullet in the group, there is a loop that runs for how many bullets are in that group.
        #
        # - Each bullet in the group will then be updated by moving them using its respective movement procedure defined in bullet.py (e.g.
        #   shootUp(), shootLeftDown() )
        #
        # - It will then check if the bullet has gone out of the screen boundaries in the direction that it is headed
        #
        # - If it has then the sprite will be removed form all groups so that the program does not have to update it anymore and it is removed from view.
        #
        # - The loop then breaks so that there is no index error if a bullet has had to be removed from the list.
        #
        # - THE SAME APPLIES TO ALL DIRECTIONAL UPDATES AND BOUNDARY CHECKS

        # KEY:

        # - bulletsUp: Moves up in a straight line using the procedure: shootUp()
        #
        # - bulletsShotgunUpLeft: Moves up and diagonally to the left using the procedure: shootUpLeft()
        #
        # - bulletsShotgunUpRight: Moves up and diagonally to the right using the procedure: shootUpRight()
        #
        # - bulletsDown: Moves down in a straight line using the procedure: shootDown()
        #
        # - bulletsShotgunDownLeft: Moves down and diagonally to the left using the procedure: shootDownLeft()
        #
        # - bulletsShotgunDownRight: Moves down and diagonally to the right using the procedure: shootDownRight()
        #
        # - bulletsLeft: Moves left in a straight line using the procedure: shootLeft()
        #
        # - bulletsShotgunLeftUp: Moves left and diagonally upwards using the procedure: shootLeftUp()
        #
        # - bulletsShotgunLeftDown: Moves left and diagonally downwards using the procedure: shootLeftDown()
        #
        # - bulletsRight: Moves right in a straight line using the procedure: shootRight()
        #
        # - bulletsShotgunRightUp: Moves right and diagonally upwards using the procedure: shootRightUp()
        #
        # - bulletsShotgunRightDown: Moves right and diagonally downwards using the procedure: shootRightDown()

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # ~~PISTOL UP DIRECTION UPDATE AND BOUNDARY CHECK~~#
        if len(bulletsUp) > 0:  # (1*)
            for x in range(len(bulletsUp)):
                bulletsUp.sprites()[x].shootUp()
                if bulletsUp.sprites()[x].rect.y < 0:  # (2*)
                    bulletsUp.sprites()[x].kill()
                    bulletCount -= 1
                    break

        # ~SHOTGUN UP DIRECTION UPDATE AND BOUNDARY CHECK~#
        if len(bulletsShotgunUpLeft) > 0:
            for x in range(len(bulletsShotgunUpLeft)):
                bulletsShotgunUpLeft.sprites()[x].shootUpLeft()
                if bulletsShotgunUpLeft.sprites()[x].rect.y < 0:
                    bulletsShotgunUpLeft.sprites()[x].kill()
                    break

        if len(bulletsShotgunUpRight) > 0:
            for x in range(len(bulletsShotgunUpRight)):
                bulletsShotgunUpRight.sprites()[x].shootUpRight()
                if bulletsShotgunUpRight.sprites()[x].rect.y < 0:
                    bulletsShotgunUpRight.sprites()[x].kill()
                    break

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # ~~PISTOL DOWN DIRECTION UPDATE AND BOUNDARY CHECK~~#
        if len(bulletsDown) > 0:
            for x in range(len(bulletsDown)):
                bulletsDown.sprites()[x].shootDown()
                if bulletsDown.sprites()[x].rect.y > 590:
                    bulletsDown.sprites()[x].kill()
                    bulletCount -= 1
                    break

        # ~SHOTGUN DOWN DIRECTION UPDATE AND BOUNDARY CHECK~#

        if len(bulletsShotgunDownLeft) > 0:
            for x in range(len(bulletsShotgunDownLeft)):
                bulletsShotgunDownLeft.sprites()[x].shootDownLeft()
                if bulletsShotgunDownLeft.sprites()[x].rect.y > 590:
                    bulletsShotgunDownLeft.sprites()[x].kill()
                    break

        if len(bulletsShotgunDownRight) > 0:
            for x in range(len(bulletsShotgunDownRight)):
                bulletsShotgunDownRight.sprites()[x].shootDownRight()
                if bulletsShotgunDownRight.sprites()[x].rect.y > 590:
                    bulletsShotgunDownRight.sprites()[x].kill()
                    break

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # ~~PISTOL LEFT DIRECTION UPDATE AND BOUNDARY CHECK~~#
        if len(bulletsLeft) > 0:
            for x in range(len(bulletsLeft)):
                bulletsLeft.sprites()[x].shootLeft()
                if bulletsLeft.sprites()[x].rect.x < 0:
                    bulletsLeft.sprites()[x].kill()
                    bulletCount -= 1
                    break

        # ~SHOTGUN LEFT DIRECTION UPDATE AND BOUNDARY CHECK~#

        if len(bulletsShotgunLeftUp) > 0:
            for x in range(len(bulletsShotgunLeftUp)):
                bulletsShotgunLeftUp.sprites()[x].shootLeftUp()
                if bulletsShotgunLeftUp.sprites()[x].rect.x < 0:
                    bulletsShotgunLeftUp.sprites()[x].kill()
                    break

        if len(bulletsShotgunLeftDown) > 0:
            for x in range(len(bulletsShotgunLeftDown)):
                bulletsShotgunLeftDown.sprites()[x].shootLeftDown()
                if bulletsShotgunLeftDown.sprites()[x].rect.x < 0:
                    bulletsShotgunLeftDown.sprites()[x].kill()
                    break

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # ~~PISTOL RIGHT DIRECTION UPDATE AND BOUNDARY CHECK~~#
        if len(bulletsRight) > 0:
            for x in range(len(bulletsRight)):
                bulletsRight.sprites()[x].shootRight()
                if bulletsRight.sprites()[x].rect.x > 790:
                    bulletsRight.sprites()[x].kill()
                    bulletCount -= 1
                    break

        # ~SHOTGUN RIGHT DIRECTION UPDATE AND BOUNDARY CHECK~#

        if len(bulletsShotgunRightUp) > 0:
            for x in range(len(bulletsShotgunRightUp)):
                bulletsShotgunRightUp.sprites()[x].shootRightUp()
                if bulletsShotgunRightUp.sprites()[x].rect.x > 790:
                    bulletsShotgunRightUp.sprites()[x].kill()
                    break

        if len(bulletsShotgunRightDown) > 0:
            for x in range(len(bulletsShotgunRightDown)):
                bulletsShotgunRightDown.sprites()[x].shootRightDown()
                if bulletsShotgunRightDown.sprites()[x].rect.x > 790:
                    bulletsShotgunRightDown.sprites()[x].kill()
                    break

        ###########################
        # ~GODMODE HEALTH CHANGE~ #
        ###########################

        # - If GODMODE is active then playerHealth and playerArmour will be set to 1000
        #
        # - Due to the fact that this is contained within the game loop, these two variables are constantly being kept at 1000
        #
        # - This means that if either of these variables change then they will be instantaneously reset to 1000
        #
        # - This gives the effect of having infinite health and armour

        if GODMODE == True:
            playerHealth = 1000
            playerArmour = 1000

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #########################################
        # ~ enemyMovementCounter incrementation ~#
        #########################################

        # - enemyMovementCounter is incremented every time the loop runs so that it is possible to keep track of how much each enemy has moved

        enemyMovementCounter += 1

        ################
        # ~~ENEMY LOOP~~#
        ################

        # - This loop runs for the length of the enemies sprite group.
        #
        # - I am able to use it to check each enemy sprite individually so I can check for certain conditions

        for x in range(len(enemies)):

            ####################
            # ~~ENEMY TRACKING~~#
            ####################

            # - the first if statement checks whether the player sprite is within a 100 pixel radius above, below, to the left and to the right of the enemy sprite
            #
            # - if the player is within that radius, the next set of if statements will be run
            #
            # - (1*) checks if the player is to the right and if so it will travel 2 pixels to the right and will flip the image of the sprite to the right direction
            #
            # - (2*) checks if the player is the the left and if so will travel 2 pixels to the left will flip the image of the sprite to the left direction
            #
            # - For those two if statements, there doesn't need to be a check for if the enemy sprite has moved off screen because it is already present in the
            #   moveLeft and moveRight functions which run continuously anyway
            #
            # - (3*) checks if the player is below and if so will move 2 pixels downwards
            #
            # - (4*) will check if the enemy has moved off the bottom of the screen and will keep it return it on screen if it has.
            #
            # - (5*) checks if the player is above and if so it will travel 2 pixels upwards
            #
            # - (6*) checks if the enemy sprite has moved off of the top of the screen and if so it will return it on screen.
            #
            # - When combined, eventually all these movements will lead the enemy to the player and they will be at the exact same x and y positions as it

            if enemies.sprites()[x].rect.x + 135 >= player.rect.x and enemies.sprites()[
                x].rect.y + 135 >= player.rect.y and enemies.sprites()[x].rect.x - 135 <= player.rect.x and \
                    enemies.sprites()[x].rect.y - 135 <= player.rect.y:
                if player.rect.x > enemies.sprites()[x].rect.x:  # (1*)
                    enemies.sprites()[x].rect.x += 1
                    enemies.sprites()[x].transformRight()
                elif player.rect.x < enemies.sprites()[x].rect.x:  # (2*)
                    enemies.sprites()[x].rect.x -= 1
                    enemies.sprites()[x].transformLeft()
                if player.rect.y > enemies.sprites()[x].rect.y:  # (3*)
                    enemies.sprites()[x].rect.y += 1
                    if enemies.sprites()[x].rect.y > 395:  # (4*)
                        enemies.sprites()[x].rect.y = 395
                elif player.rect.y < enemies.sprites()[x].rect.y:  # (5*)
                    enemies.sprites()[x].rect.y -= 1
                    if enemies.sprites()[x].rect.y < 0:  # (6*)
                        enemies.sprites()[x].rect.y = 0

            ################################
            # ~~ENEMY AND PLAYER COLLISION~~#
            ################################

            # - If an enemy collides with the player and if the playerArmour variable is above 0 then playerArmour will have 20 taken off of it
            #   otherwise the playerHealth variable will have 20 taken off of it.
            #
            # - Then it will detected whether the enemy is above, below, to the left or to the right of the player.
            #
            # - Depending on what direction the player is in compared to the enemy, the corresponding knockback function will be called.
            #
            # - The knockback functions are defined in the enemy class in enemy.py

            if pygame.sprite.collide_mask(enemies.sprites()[x], player):
                if playerArmour > 0:
                    playerArmour -= 10
                else:
                    playerHealth -= 10
                if enemies.sprites()[x].rect.x > player.rect.x:
                    enemies.sprites()[x].knockbackRight()
                elif enemies.sprites()[x].rect.x < player.rect.x:
                    enemies.sprites()[x].knockbackLeft()
                if enemies.sprites()[x].rect.y > player.rect.y:
                    enemies.sprites()[x].knockbackDown()
                if enemies.sprites()[x].rect.y < player.rect.y:
                    enemies.sprites()[x].knockbackUp()

            ################################
            # ~~ENEMY AND BULLET COLLISION~~#
            ################################

            # - An if statement detects whether any enemy from the enemies group or any bullet from the bullets group has collided
            #   if so the other parameters in the pygame.sprite.collide function determine whether the olliding sprites are killed or not
            #   I set enemies as False and bullets as True. This means that whenever bullets and enemies collide, bullets will always be
            #   killed and enemies won't
            #
            # - As the function returns a boolean value for whether any items have collided, I am able to place it within an if statement
            #   to detect whether there has been a collision
            #
            # - if there has been a collision then a list will be made out of the sprites involved within the collision, that enemy will be
            #   stored in hitenemy
            #
            # - The enemyInjuredSound will then play and the healthDecrease function will be called on the hitenemy
            #
            # - bulletCount will also be decreased by 1 to compensate for the bullet killed in the collision
            #
            # - The same then occurs with the Shotgun bullets if that is the weapon that is being used except the bulletCount will not be decreased
            #   if there is a collision

            Enemy_Pistol_Collide_Check = pygame.sprite.groupcollide(enemies, allBullets, False, True)
            if Enemy_Pistol_Collide_Check:
                hitenemy = list(Enemy_Pistol_Collide_Check.keys())[0]
                enemyInjuredSound.play()
                hitenemy.healthDecrease()
                if weapon == 1:
                    hitenemy.healthDecrease()
                bulletCount -= 1

            Enemy_Shotgun_Collide_Check = pygame.sprite.groupcollide(enemies, shotgunBullets, False, True)
            if Enemy_Shotgun_Collide_Check:
                hitenemy = list(Enemy_Shotgun_Collide_Check.keys())[0]
                enemyInjuredSound.play()
                hitenemy.healthDecrease()
                hitenemy.healthDecrease()

            ###############################
            # ~~ENEMY AND ENEMY COLLISION~~#
            ###############################

            # - A for loop runs for the amount of enemy there are (this is to check an enemy and then check another enemy simultaneously)
            #
            # - It then checks if the enemy is in the area of the other enemy and if it is the it will check if the enemy is above, below,
            #   to the left or to the right of the other enemy.
            #
            # - If it is to the right then the enemy will be moved to the left
            #
            # - if it is to the left then the enemy will be moved to the right
            #
            # - If it is above then the enemy will be moved downwards
            #
            # - if it is below then the enemy will be moved upwards
            #
            # - This prevents enemies from going inside eachother because when they enter eachothers area, they will be repelled in the opposite direction

            for y in range(len(enemies)):
                if enemies.sprites()[x].rect.x + 25 >= enemies.sprites()[y].rect.x and enemies.sprites()[
                    x].rect.x - 25 <= enemies.sprites()[y].rect.x and enemies.sprites()[x].rect.y + 25 >= \
                        enemies.sprites()[y].rect.y and enemies.sprites()[x].rect.y - 25 <= enemies.sprites()[y].rect.y:
                    if enemies.sprites()[x].rect.x > enemies.sprites()[y].rect.x:
                        enemies.sprites()[x].rect.x = enemies.sprites()[y].rect.x + 25
                    elif enemies.sprites()[x].rect.x < enemies.sprites()[y].rect.x:
                        enemies.sprites()[x].rect.x = enemies.sprites()[y].rect.x - 25
                    elif enemies.sprites()[x].rect.y > enemies.sprites()[y].rect.y:
                        enemies.sprites()[x].rect.y = enemies.sprites()[y].rect.y + 25
                    elif enemies.sprites()[x].rect.y < enemies.sprites()[y].rect.y:
                        enemies.sprites()[x].rect.y = enemies.sprites()[y].rect.y - 25

            ####################
            # ~~ENEMY MOVEMENT~~#
            ####################

            # - Every time the loop runs, the enemyMovementCounter variable increments by 1.
            #
            # - As long as the counter is less than 60, the enemy will move right (the move right procedure is defined in enemy.py)
            #
            # - When the counter is greater than 60 but less than 120, the enemy will move left.
            #
            # - Whenever the counter exceeds 120, it will = 0
            #   This will allow for the enemy sprite to alternate between moving left and right continuously

            if enemyMovementCounter < 50:
                if enemies.sprites()[x].rect.x + 135 >= player.rect.x and enemies.sprites()[
                    x].rect.y + 135 >= player.rect.y and enemies.sprites()[x].rect.x - 135 <= player.rect.x and \
                        enemies.sprites()[x].rect.y - 135 <= player.rect.y:
                    pass
                else:
                    aorb = ["a", "b", "c"]
                    willmove = random.choice(aorb)
                    if willmove == "a":
                        enemies.sprites()[x].moveRight()
            elif enemyMovementCounter > 100:
                enemyMovementCounter = 0
            elif enemyMovementCounter > 50:
                if enemies.sprites()[x].rect.x + 135 >= player.rect.x and enemies.sprites()[
                    x].rect.y + 135 >= player.rect.y and enemies.sprites()[x].rect.x - 135 <= player.rect.x and \
                        enemies.sprites()[x].rect.y - 135 <= player.rect.y:
                    pass
                else:
                    aorb = ["a", "b", "c"]
                    willmove = random.choice(aorb)
                    if willmove == "a":
                        enemies.sprites()[x].moveLeft()

            ########################
            # ~~ENEMY HEALTH CHECK~~#
            ########################

            # - This will run the health check function (defined in enemy.py) on each enemy
            #
            # - The function wull check if each enemis health is < 0
            #
            # - If the function returns True then the enemy will be killed and the enemydead variable will be incremented

            if enemies.sprites()[x].healthCheck() == True:
                enemies.sprites()[x].kill()
                enemyDeathSound.play()
                enemydead += 1
                break

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #####################
        # ~~WALL BOUNDARIES~~#
        #####################

        # - Creates a for loop that runs for the length of sprites in the allsprites group
        #
        # - It then creates a for loop that runs for the amount of sprites in the wall sprite group
        #
        # - It will then check if the sprite from the allsprites group is within a particular area of the wall
        #
        # - If it is then it will check whether it is to the left or right of the wall, if it is to the left then
        #   the the colliding sprite will be moved 40 oixels to the right
        #
        # - if the wall is to the right then the sprite will be moved 40 pixles to the left
        #
        # - It will then do the exact same as above for the Up and down directions. I have done them separately
        #   because I found that it worked better when checked separately.

        # ~~LEFT OR RIGHT~~#

        for x in range(len(allsprites)):
            for y in range(len(walls)):
                if walls.sprites()[y].rect.x + 40 >= allsprites.sprites()[x].rect.x and walls.sprites()[
                    y].rect.x - 40 <= allsprites.sprites()[x].rect.x and walls.sprites()[y].rect.y + 30 >= \
                        allsprites.sprites()[x].rect.y and walls.sprites()[y].rect.y - 30 <= allsprites.sprites()[
                    x].rect.y:
                    if allsprites.sprites()[x].rect.x > walls.sprites()[y].rect.x:
                        allsprites.sprites()[x].rect.x = walls.sprites()[y].rect.x + 40
                    elif allsprites.sprites()[x].rect.x < walls.sprites()[y].rect.x:
                        allsprites.sprites()[x].rect.x = walls.sprites()[y].rect.x - 40

        # ~~ABOVE OR BELOW~~#

        for x in range(len(allsprites)):
            for y in range(len(walls)):
                if walls.sprites()[y].rect.y + 40 >= allsprites.sprites()[x].rect.y and walls.sprites()[
                    y].rect.y - 35 <= allsprites.sprites()[x].rect.y and walls.sprites()[y].rect.x + 30 >= \
                        allsprites.sprites()[x].rect.x and walls.sprites()[y].rect.x - 30 <= allsprites.sprites()[
                    x].rect.x:
                    if allsprites.sprites()[x].rect.y > walls.sprites()[y].rect.y:
                        allsprites.sprites()[x].rect.y = walls.sprites()[y].rect.y + 40
                    elif allsprites.sprites()[x].rect.y < walls.sprites()[y].rect.y:
                        allsprites.sprites()[x].rect.y = walls.sprites()[y].rect.y - 35

        # maraudercheck = pygame.sprite.groupcollide( marauders , walls , False , False )
        # if maraudercheck:
        #  hitenemy = list(maraudercheck.keys())
        #  print(hitenemy)
        # hitwall = list(maraudercheck.keys())[1]
        # if hitenemy.rect.x < hitwall.rect.x:
        #  hitenemy.rect.x -= 3
        # elif hitenemy.rect.x > hitwall.rect.x:
        #  hitenemy.rect.x += 3
        # if hitenemy.rect.y < hitwall.rect.y:
        #  hitenemy.rect.x -= 3
        # elif hitenemy.rect.y > hitwall.rect.y:
        #  hitenemy.rect.x += 3

        # ~~ABOVE OR BELOW~~#

        # for x in range (len(marauders)):
        #    for y in range (len(walls)):
        #      if walls.sprites()[y].rect.x +40 >= marauders.sprites()[x].rect.x and walls.sprites()[y].rect.x - 80 <= marauders.sprites()[x].rect.x and walls.sprites()[y].rect.y +30 >= marauders.sprites()[x].rect.y and  walls.sprites()[y].rect.y - 100 <= marauders.sprites()[x].rect.y:
        #        if marauders.sprites()[x].rect.y  > walls.sprites()[y].rect.y:
        #          marauders.sprites()[x].rect.y = walls.sprites()[y].rect.y +40
        #        elif marauders.sprites()[x].rect.y < walls.sprites()[y].rect.y:
        #          marauders.sprites()[x].rect.y = walls.sprites()[y].rect.y - 95

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #############################
        # ~~BULLETS WALL COLLISIONS~~#
        #############################

        # - A for loop wil run for the amount of sprites in the walls sprite group
        #
        # - Another loop wil run for the length of the amount of bullets that exist in the allbullets sprite group
        #
        # - If a bullet and wall collide then that bullet will be killed and the bullet count variable will be decreased by 1

        bullet_Collide = pygame.sprite.groupcollide(allBullets, walls, True, False)
        if bullet_Collide:
            bulletCount -= 1

        pygame.sprite.groupcollide(shotgunBullets, walls, True, False)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #####################
        # ~~DIRECTION CHECK~~#
        #####################

        # - Whenever the directioncheck variable = 1, the player sprite image will change to the right
        #
        # - Whenever the directioncheck variable = 2, the player sprite image will change to the left
        #
        # - Whenever the directioncheck variable = 3, the player sprite image will change to the upward facing state
        #
        # - Whenever the directioncheck variable = 4, the player sprite image will change to the downward facing state

        if directioncheck == 1:
            player.directionRightStill()
            player2.directionRightStill()
            player2.enlarge()
        elif directioncheck == 2:
            player.directionLeftStill()
            player2.directionLeftStill()
            player2.enlarge()
        elif directioncheck == 3:
            player.directionUpStill()
            player2.directionUpStill()
            player2.enlarge()
        elif directioncheck == 4:
            player.directionDownStill()
            player2.directionDownStill()
            player2.enlarge()

        #########################
        ###~~PLAYER MOVEMENT~~###
        #########################

        # - (1*) checks if the 'd' key has been pressed, if so, direction check will = 1 (linked above)
        #   and the right acceleration variable increases by 0.5 ( this means that whenever d is pressed the acceleration variable will increase)
        #
        # - If the acceleration variable is greater or the same as the value 4 then the acceleration variable will = 4
        #   (this caps the speed so that it doesn't just get exponentially faster)
        #
        # - Then the moveRight procedure is called from  the player class in player.py with the acceleration variable passed in
        #   this means that the player sprite will move the amount of pixels of the value of the acceleration variable
        #
        # - If the 'd' key is never pressed then the acceleration variable = 0 so that once d is pressed again, the variable is reset
        #   and the sprite is able to accelerate again from rest.
        #
        # - The same logic applies to all of the lines below but just in different directions and using a different named acceleration variable
        #   so that the values do not overlap.
        #
        # - (The direction of each is labled below)

        if GODMODE == True:
            rightAccel = 8
            leftAccel = 8
            upAccel = 8
            downAccel = 8

        # ~~RIGHT DIRECTION PLAYER MOVEMENT~~#
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:  # (1*)
            directioncheck = 1
            rightAccel += 0.5
            if rightAccel >= 4 and GODMODE == False:
                rightAccel = 4
            player.moveRight(rightAccel)
        else:
            rightAccel = 0

        # ~~LEFT DIRECTION PLAYER MOVEMENT~~#
        if keys[pygame.K_a]:
            directioncheck = 2
            leftAccel += 0.5
            if leftAccel >= 4 and GODMODE == False:
                leftAccel = 4
            player.moveLeft(leftAccel)
        else:
            leftAccel = 0

        # ~~UP DIRECTION PLAYER MOVEMENT~~#
        if keys[pygame.K_w]:
            directioncheck = 3
            upAccel += 0.5
            if upAccel >= 4 and GODMODE == False:
                upAccel = 4
            player.moveUp(upAccel)
        else:
            upAccel = 0

        # ~~DOWN DIRECTION PLAYER MOVEMENT~~#
        if keys[pygame.K_s]:
            directioncheck = 4
            downAccel += 0.5
            if downAccel >= 4 and GODMODE == False:
                downAccel = 4
            player.moveDown(downAccel)
        else:
            downAccel = 0

        #######################
        # ~~PLAYER COLLISIONS~~#
        #######################

        # - A for loop will run for the length of the healthpotions sprite group
        #
        # - if a healthpotion sprite and player sprite collide and the playerhealth variable is less than 100
        #   then the playerHealth varibale will be increased by 10
        #
        # - the healthpotion that the player collided with will be killed as well so that it is unable to be
        #   inteacted with again

        for x in range(len(healthpotions)):
            if pygame.sprite.collide_mask(healthpotions.sprites()[x], player):
                if playerHealth < 100:
                    playerHealth += 10
                    healthpotions.sprites()[x].kill()
                    break

        for x in range(len(armours)):
            if pygame.sprite.collide_mask(armours.sprites()[x], player):
                if playerArmour < 100:
                    playerArmour += 10
                    armours.sprites()[x].kill()
                    break

        #########################
        # ~~PLAYER HEALTH CHECK~~#
        #########################

        # - If the playerhealth variable is less than or equal to 0 then all sprites will be removed from the game
        #   and the game loop will cease to run
        #
        # - The deathscreen function will then run.

        if playerHealth <= 0:
            DELETE_ALL_SPRITES()
            run = False
            deathScreen()
            value = 0
            return value
            playerHealth = 100

        # - This if statement below will reset the playerArmour variables to 0 if they happen to fall below that value

        if playerArmour < 0:
            playerArmour = 0

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        ######################
        # ~~LEVEL COMPLETION~~#
        ######################

        # - The enemy dead variable increments by 1 when an enemy is kiiled
        #
        # - If the enemy dead variable is the same as the length of the enemy sprite group initially then all enemies will be dead
        #
        # - This is basically saying "if all enemies are dead"
        #
        # - there will then be a for loop that will run for the amount of sprites in the levelcompletes sprite group
        #
        # - if the player collides with a levelcomplets sprite, an enter key prompt will then appear above the player
        #
        # - Once the enter key is pressed, an end timer is created and the start timer is taken from it to get the time elapsed so far
        #
        # - It will then check the level 2d array for the string "ONE" "TWO" or "THREE"
        #
        # - If "ONE" is found in the array then the time elapsed will be saved in index 1 of leaderboardList
        #
        # - If "TWO" is found in the array then the time elapsed will be saved in index 2 of leaderboardList
        #
        # - If "THREE" is found in the array then the time elapsed will be saved in index 3 of leaderboardList
        #
        # - This is so that I am able to keep track of which time was acheived in each level
        #
        # - All sprites will then be cleared and the game function will stop, returning the player to the HUB

        if enemydead == enemyLength:
            for x in range(len(levelcompletes)):
                if pygame.sprite.collide_mask(levelcompletes.sprites()[x], player):
                    prompt = pygame.image.load('enter key.png')
                    prompt = pygame.transform.scale(prompt, (20, 20))
                    screen.blit(prompt, (player.rect.x + 35, player.rect.y))
                    if keys[pygame.K_RETURN]:
                        timeEnd = time.perf_counter()
                        totalTime = timeEnd - timeStart
                        totalTime = totalTime - 3
                        totalTime = str(totalTime)[0] + str(totalTime)[1] + str(totalTime)[2] + str(totalTime)[3]

                        if level[1][18] == "ONE":
                            leaderboardList.pop(1)
                            leaderboardList.insert(1, "," + totalTime)
                            value = 1
                            DELETE_ALL_SPRITES()
                            run = False
                            return value
                        elif level[1][18] == "TWO":
                            leaderboardList.pop(2)
                            leaderboardList.insert(2, "#" + totalTime)
                            value = 2
                            DELETE_ALL_SPRITES()
                            run = False
                            return value
                        elif level[1][18] == "THREE":
                            leaderboardList.pop(3)
                            leaderboardList.insert(3, "'" + totalTime)
                            value = 3
                            DELETE_ALL_SPRITES()
                            run = False
                            return value
                        elif level[1][18] == "FOUR":
                            # leaderboardList.pop(1)
                            # leaderboardList.insert(1,","+totalTime)
                            value = 4
                            DELETE_ALL_SPRITES()
                            run = False
                            return value
                        elif level[1][18] == "FIVE":
                            # leaderboardList.pop(1)
                            # leaderboardList.insert(1,","+totalTime)
                            value = 5
                            DELETE_ALL_SPRITES()
                            run = False
                            return value
                        elif level[1][18] == "SIX":
                            # leaderboardList.pop(1)
                            # leaderboardList.insert(1,","+totalTime)
                            value = 6
                            DELETE_ALL_SPRITES()
                            run = False
                            return value

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        ######################################################
        # ~~LEVEL CHANGER (ONLY RELEVANT WHEN IN HUB LAYOUT)~~#
        ######################################################

        # - Because level platform sprites will only exist in the HUB, this is only relevant when in the HUB layout
        #
        # - A for loop will run for the amount of level platforms there are in the levelplatforms list
        #
        # - If the player collides with the platform then an enter key prompt will appear above the player sprite
        #
        # - If the enter key is then pressed and the players yposition is less than 164, then levelNumber will = 1 and all sprites will be cleared
        #   the game loop will then end, returning the levelNumber to the Menu function. when 1 is returned, the game function runs with
        #   the levelONElayout
        #
        # - Else if the enter key is pressed and the players yposition is greater than 164 and less than 292, then levelNumber will = 2 and all sprites will be cleared
        #   the game loop will then end, returning the levelNumber to the Menu function. when 2 is returned, the game function runs with
        #   the levelTWOlayout
        #
        # - Else if the enter key is pressed and the players yposition is greater than 292, then levelNumber will = 3 and all sprites will be cleared
        #   the game loop will then end, returning the levelNumber to the Menu function. when 3 is returned, the game function runs with
        #   the levelTHREElayout

        levelNumber = 0
        for x in range(len(levelplatforms)):
            if pygame.sprite.collide_mask(levelplatforms.sprites()[x], player):
                prompt = pygame.image.load('enter key.png')
                prompt = pygame.transform.scale(prompt, (20, 20))
                screen.blit(prompt, (player.rect.x + 35, player.rect.y))
                if level[2][1] == "HUB2":
                    if keys[pygame.K_RETURN]:
                        if player.rect.y < 164:
                            levelNumber = 6
                            DELETE_ALL_SPRITES()
                            return levelNumber
                            run = False
                        elif player.rect.y > 164 and player.rect.y < 292:
                            levelNumber = 7
                            DELETE_ALL_SPRITES()
                            return levelNumber
                            run = False
                        elif player.rect.y > 292:
                            levelNumber = 8
                            DELETE_ALL_SPRITES()
                            return levelNumber
                            run = False
                else:
                    if keys[pygame.K_RETURN]:
                        if player.rect.y < 164:
                            levelNumber = 1
                            DELETE_ALL_SPRITES()
                            return levelNumber
                            run = False
                        elif player.rect.y > 164 and player.rect.y < 292:
                            levelNumber = 2
                            DELETE_ALL_SPRITES()
                            return levelNumber
                            run = False
                        elif player.rect.y > 292:
                            levelNumber = 3
                            DELETE_ALL_SPRITES()
                            return levelNumber
                            run = False

        trigger_collide = pygame.sprite.groupcollide(triggers, players, False, False)
        if trigger_collide:
            player.rect.y -= 20
            DELETE_ALL_SPRITES()
            if level[2][1] == "HUB2":
                number = 0
            else:
                number = 5
            return number

        pygame.display.update()

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        ########################
        # ~~DRAWING CODE BELOW~~#
        ########################

        # - All or most of the code below consists of drawing to the screen

        screen.fill(DARK_GREY)

        # - The code below is where all the sprite groups are drawn to the screen individually.

        enemies.draw(screen)
        bulletsUp.draw(screen)
        bulletsDown.draw(screen)
        bulletsLeft.draw(screen)
        bulletsRight.draw(screen)
        walls.draw(screen)
        healthpotions.draw(screen)
        armours.draw(screen)
        levelplatforms.draw(screen)
        leveltexts.draw(screen)
        levelcompletes.draw(screen)
        blockade1s.draw(screen)
        blockade2s.draw(screen)
        blockade3s.draw(screen)
        blockade4s.draw(screen)
        blockade5s.draw(screen)
        bulletsShotgunUpRight.draw(screen)
        bulletsShotgunUpLeft.draw(screen)
        bulletsShotgunDownLeft.draw(screen)
        bulletsShotgunDownRight.draw(screen)
        bulletsShotgunLeftUp.draw(screen)
        bulletsShotgunLeftDown.draw(screen)
        bulletsShotgunRightUp.draw(screen)
        bulletsShotgunRightDown.draw(screen)
        triggers.draw(screen)
        marauders.draw(screen)

        ################
        # ~HUB CONTROLS~#
        ################

        # - notHUB will be false if there are no enemy sprites in the enemy sprite group, this clarifies that the player is
        #   in the HUB
        #
        # - If notHUB is false then the game controls will be displayed at the bottom of the screen

        if notHUB == False:
            font = pygame.font.Font('8-BitMadness.ttf', 25)
            text = font.render(": MOVEMENT", 1, WHITE)
            screen.blit(text, (wasd.rect.x + 100, wasd.rect.y + 15))
            text = font.render(": SHOOTING", 1, WHITE)
            screen.blit(text, (arrows.rect.x + 100, arrows.rect.y + 15))

            ###########################
            # ~HUD INSTRUCTIONS PROMPT~#
            ###########################

            # - A timer is created and taken away from the displayTimeStart timer defined at the beginning of the game function
            #   , every time the game loop is run it will do this and store the value in 3secs
            #
            # - While 3secs is less than 3, "Move to a platform and press enter to select level" is blitted to the screen
            #
            # - Once that time has passed, it will not be blitted to the screen anymore.

            timer = time.perf_counter()
            secs = timer - displayTimeStart
            if secs < 3:
                pygame.draw.rect(screen, BLACK, (60, 20, 680, 40))
                font = pygame.font.Font('8-BitMadness.ttf', 30)
                title = font.render("Move to a platform and press enter to select level", 1, YELLOW)
                screen.blit(title, (80, 30))

        #########
        # ~~HUD~~#
        #########

        # - This code blits the HUD to the screen
        #
        # - (The HUD bar, the health text, the armour text and the weapon text)

        pygame.font.init()
        font = pygame.font.Font('8-BitMadness.ttf', 50)
        pygame.draw.rect(screen, LIGHT_GREY, (0, 470, 800, 130))
        pygame.draw.rect(screen, BLACK, (325, 470, 150, 130))
        if playerHealth <= 40:
            text = font.render("HEALTH: " + str(playerHealth), 1, (255, 0, 0))
            screen.blit(text, (20, 485))
        else:
            text = font.render("HEALTH: " + str(playerHealth), 1, WHITE)
            screen.blit(text, (20, 485))
        if playerArmour <= 40:
            text = font.render("ARMOUR: " + str(playerArmour), 1, (255, 0, 0))
            screen.blit(text, (20, 540))
        else:
            text = font.render("ARMOUR: " + str(playerArmour), 1, WHITE)
            screen.blit(text, (20, 540))
        text = font.render("WEAPON:", 1, WHITE)
        screen.blit(text, (550, 485))

        ###############
        # ~WEAPON VIEW~#
        ###############

        # - When weapon = 0, the pistol image will be displayed in the HUD and when weapon = 1 the shotgun image
        #   will be displayed in the HUD

        if weapon == 0:
            pistol = pygame.image.load('doom pistol.png')
            screen.blit(pistol, (615, 535))
        else:
            pistol = pygame.image.load('doom shotgun.png')
            screen.blit(pistol, (550, 535))

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        ################
        # ~CURRENT TIME~#
        ################

        # - If the player is playing a level then notHUB will = True
        #
        # - If notHUB is True then a currentTime variable will be created, to get the actual time I must take away a timer created at the start of
        #   the loop to have the time elapsed over the loop. I will store this value in displayTime
        #
        # - Due to the game loop updating continuously the displayTime variable will hold the current time elapsed since the level started
        #

        if notHUB:
            currentTime = time.perf_counter()
            displayTime = currentTime - displayTimeStart

            ###############################
            # ~(LEVEL INSTRUCTIONS PROMPT)~#
            ###############################

            # - An if statement will detect whether the time elapsed so far is greater than 0.1 seconds (so the level has time to appear) and is less than 1 second
            #   so that the prompt doesn't continue to appear after 1 second
            #
            # - Within the if statement if the time is within the boundary of 0.1 secs and 1 sec, then a while loop will run that creates a timer
            #   this timer is taken from the displayTimeStart timer as well to give the screenTime (how long this while loop will run for)
            #
            # - A prompt will then be blitted to the screen that will explain to the player how the levels work
            #
            # - If screenTime is greater than 3 then the while loop will stop running (so the prompt is only displayed for 3 seconds and everything in the
            #   background is paused.)
            #
            # - After this the game will continue running and 3 seconds will be taken off of the displayTime so account for the time lost while
            #   the prompt was being shown

            if minute == 0 and displayTime <= 1 and displayTime > 0.1:
                start = True
                while start:
                    bufferTime = time.perf_counter()
                    screenTime = bufferTime - displayTimeStart
                    pygame.draw.rect(screen, BLACK, (210, 140, 330, 200))
                    font = pygame.font.Font('8-BitMadness.ttf', 30)
                    title = font.render("MISSION:", 2, WHITE)
                    screen.blit(title, (220, 150))
                    title = font.render("- Kill all enemies", 2, WHITE)
                    screen.blit(title, (220, 200))
                    title = font.render("- Leave on red platform", 2, WHITE)
                    screen.blit(title, (220, 250))
                    title = font.render("- As fast as possible!", 2, WHITE)
                    screen.blit(title, (220, 300))
                    pygame.display.update()
                    if screenTime > 3:
                        start = False
            if minute < 1:
                displayTime -= 3

            # ~CURRENT TIME (CONTINUED)~#

            # - if one minute = 1 and 40 seconds has elapsed then all sprites will be removed, the game loop will end and the death screen will be displayed
            #   (this creates a level time limit)

            if minute == 1 and displayTime >= 40:
                DELETE_ALL_SPRITES()
                deathScreen()
                run = False

            # - Because one game loop takes a very small amount of time, the time elapsed between each loop is miniscule which means the value of time is measured
            #   is very long in characters
            #
            # - To combat this problem I will only read the first 4 characters of display time when it is greater than ten, this means the format of time in
            #   seconds will be for example: 10.10 or 23.55. This will be stored in newTime
            #
            # - if newTime is greater than 60 then the minute variable defined earlier as 0 will increment by one and the timer will reset to 0
            #
            # - The minute variable and the newTime variable will then be bliited to the screen and will display when the player is playing a level.

            if displayTime > 10:
                newTime = str(displayTime)[0] + str(displayTime)[1] + str(displayTime)[2] + str(displayTime)[3] + \
                          str(displayTime)[4]
            else:
                newTime = str(displayTime)[0] + str(displayTime)[1] + str(displayTime)[2] + str(displayTime)[3]
            if displayTime >= 60:
                minute += 1
                displayTimeStart = time.perf_counter()
            if minute == 1 and displayTime >= 20:
                font = pygame.font.Font('8-BitMadness.ttf', 40)
                text = font.render(str(minute) + "m", 1, (255, 0, 0))
                screen.blit(text, (10, 5))
                text = font.render(str(newTime) + "s", 1, (255, 0, 0))
                screen.blit(text, (70, 5))
            else:
                font = pygame.font.Font('8-BitMadness.ttf', 40)
                text = font.render(str(minute) + "m", 1, WHITE)
                screen.blit(text, (10, 5))
                text = font.render(str(newTime) + "s", 1, WHITE)
                screen.blit(text, (70, 5))

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # ~PLAYERS DRAWING TO SCREEN~#

        # - The player group is drawn to screen here so that it overlaps everything else.

        players.draw(screen)

        ############
        # ~~CURSOR~~#
        ############

        # - The original cursor is made invisible
        #
        # - The x and y positions of the mouse is then stored in x and y variables
        #
        # - I will then oad the cursor image I made and then blit it in on the screen in the x and y position of the mouse

        pygame.mouse.set_visible(False)
        x, y = pygame.mouse.get_pos()
        cursor = pygame.image.load('cursor.png')
        cursor = pygame.transform.scale(cursor, (20, 20))
        screen.blit(cursor, (x, y))

        ##################################
        # REFRESH SCREEN AND SHOW DRAWINGS#
        ##################################

        pygame.display.flip()

        #########
        # SET FPS#
        #########

        clock.tick(60)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#######################################
#                                     #
#         NAME INPUT SCREEN           #
#                                     #
#######################################


def nameInput():
    # - A variable named text is created and is given a value of " " I then render it with a font and store it in a variable named TEXT
    #
    # - I then give it its top left x coordinate and create a rectangle that will folow the top right coordinate of the text called the cursor.
    #
    # - At the moment the top left and the top right coordinate are the same.
    #
    # - I then create a while loop and an event
    #
    # - If the event is a key press then it will detect whether the backspace key was pressed. If the length of the text is greater than 0
    #   then the last character will be removed
    #
    # - if the key press is the return key then the loop will end, taking the player to the HUB, the leaderboard list will also be updated with the name
    #   inputted
    #
    # - If the key press is any other key then the input will be converted into unicode and the character will be added to the end of the text string
    #
    # - the text will then be rerendered so that it can update live
    #
    # - the position of the cursor will also then be updated to the new top right coordinate of the text.
    #
    # - The decoration is then added, such as the background and the text is blitted to the screen
    #
    # - I will also create an if statement that checks if half a second has passed and if it has then the cursor will be blitted to the screen
    #
    # - This will create a blinking cursor that follows the end of the text live on screen.

    text = ''
    font = pygame.font.Font('8-BitMadness.ttf', 40)
    TEXT = font.render(text, True, WHITE)
    rect = TEXT.get_rect()
    rect.topleft = (150, 300)
    cursor = Rect(rect.topright, (6, rect.height + 10))

    nameRun = True
    while nameRun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nameRun = False
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text) > 0:
                        text = text[:-1]
                elif event.key == K_RETURN:
                    nameRun = False
                    leaderboardList.insert(0, text)
                else:
                    text += event.unicode
                    text = ('%.4s' % text)
                TEXT = font.render(text, True, WHITE)
                rect.size = TEXT.get_size()
                cursor.topleft = rect.topright

        Background = pygame.image.load('pauseback.png')
        Background = pygame.transform.scale(Background, (800, 600))
        screen.blit(Background, (0, 0))

        font = pygame.font.Font('8-BitMadness.ttf', 30)
        title = font.render("(4 characters max)", 1, YELLOW)
        screen.blit(title, (280, 190))

        font = pygame.font.Font('8-BitMadness.ttf', 70)
        title = font.render("Enter Name", 1, WHITE)
        screen.blit(title, (245, 120))

        pygame.draw.rect(screen, BLACK, (130, 280, 540, 90))

        screen.blit(TEXT, rect)
        if time.time() % 1 > 0.5:
            pygame.draw.rect(screen, WHITE, cursor)
        pygame.display.update()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


########################################
#                                      #
#         LEADERBOARD SCREEN           #
#                                      #
########################################


def leaderboardScreen():
    LoadingScreen()

    # ~OPENING LEADERBOARD.TXT~#

    # - leaderboard.txt is read line by line then saved as an array in results

    f = open("leaderboard.txt", "r")
    results = f.readlines()

    # ~VARIBALE NAMES~#

    totalscoreE1M1 = 0
    totalscoreE1M2 = 0
    totalscoreE1M3 = 0

    textHeight = 200

    # ~DEFINING LISTS~#
    numlist = []

    # ~TOTAL TIME EXTRACTION FROM RESULTS~#

    # - Ive created a loop that runs for the length of the results array and then for as long as the amount of characters in each
    #   index of the results array
    #
    # - if a "," is found then the three characters after it are saved into totalscoreE1M1
    #
    # - if a "#" is found then the three characters after it are saved into totalscoreE1M2
    #
    # - if a " ' " is found then the three characters after it are saved into totalscoreE1M3
    #
    # - It will then append all of the results into numlist combined together as one value

    for x in range(len(results)):
        for z in range(len(results[x])):
            if results[x][z] == ",":
                totalscoreE1M1 = results[x][z + 1] + results[x][z + 2] + results[x][z + 3] + results[x][z + 4]
            elif results[x][z] == "#":
                totalscoreE1M2 = results[x][z + 1] + results[x][z + 2] + results[x][z + 3] + results[x][z + 4]
            elif results[x][z] == "'":
                totalscoreE1M3 = results[x][z + 1] + results[x][z + 2] + results[x][z + 3] + results[x][z + 4]
        numlist.append(float(totalscoreE1M1) + float(totalscoreE1M2) + float(totalscoreE1M3))

    # ~TIMES AND RESULTS BUBBLE SORT~#

    # - A large number is added to the end of numlist so that it is always at the end (it can't be exceeded
    #   due to the 1 minute 40 seconds time limit of levels).
    #
    # - A for loop then runs for the length of the numlist multiplied by 10000 so that it goes through the list
    #   a thorough amount of times. This ensures that all items are truly in order.
    #
    # - Within the loop, it will check if the current item being checked is greater than or less than the value in the index next to it.
    #
    # - If it is greater than the one after it then they will be swapped
    #
    # - This happens repeatedly until they are in order from lowest to highest
    #
    # - if the item currently being checked is 1000000 then the loop will end because the end of the list has been reached. This prevents the error
    #   of the final item being checked but there isnt a value after it to compare.

    swaps = True

    while swaps:
        swaps = False
        for x in range(0, len(numlist) - 1):

            if numlist[x] > numlist[x + 1]:
                swaps = True
                results[x], results[x + 1] = results[x + 1], results[x]
                numlist[x], numlist[x + 1] = numlist[x + 1], numlist[x]

    # ~REMOVING UNNEEDED CHARACTERS~#

    # - This for loop checks through results and will replace any ' , or # with a space so that they arent displayed on screen

    for x in range(len(results)):
        results[x] = re.sub("'|,|#", " ", results[x])

    # ~LOOP TO DISPLAY SCREEN~#

    # - The While loop below runs as long as ldrbRun is True, it will blit the results to the screen
    #
    # - If the return key is pressed then the loop will end and the menu function will run.

    ldrbRun = True
    while ldrbRun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ldrbRun = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    ldrbRun = False
                    menu()
                elif event.key == pygame.K_SPACE:
                    for x in range(len(results)):
                        print("pos.", x + 1, "Name: ", results[x][0] + results[x][1] + results[x][2] + results[x][3],
                              " Overall score: ", numlist[x])

        Background = pygame.image.load('pauseback.png')
        Background = pygame.transform.scale(Background, (800, 600))
        screen.blit(Background, (0, 0))

        pygame.draw.rect(screen, BLACK, (90, 140, 600, 350))

        font = pygame.font.Font('8-BitMadness.ttf', 60)
        title = font.render("LEADERBOARD", 1, DARK_RED)
        screen.blit(title, (240, 60))
        title = font.render("LEADERBOARD", 1, WHITE)
        screen.blit(title, (237, 57))

        font = pygame.font.Font('8-BitMadness.ttf', 40)

        title = font.render("NAMES", 1, DARK_RED)
        screen.blit(title, (100, 150))
        title = font.render("NAMES", 1, YELLOW)
        screen.blit(title, (98, 148))

        title = font.render("E1M1", 1, DARK_RED)
        screen.blit(title, (270, 150))
        title = font.render("E1M1", 1, YELLOW)
        screen.blit(title, (268, 148))

        title = font.render("E1M2", 1, DARK_RED)
        screen.blit(title, (420, 150))
        title = font.render("E1M2", 1, YELLOW)
        screen.blit(title, (418, 148))

        title = font.render("E1M3", 1, DARK_RED)
        screen.blit(title, (570, 150))
        title = font.render("E1M3", 1, YELLOW)
        screen.blit(title, (568, 148))

        text = font.render("#1", 3, DARK_RED)
        screen.blit(text, (30, 230))
        text = font.render("#1", 3, YELLOW)
        screen.blit(text, (28, 228))

        text = font.render("#2", 3, DARK_RED)
        screen.blit(text, (30, 270))
        text = font.render("#2", 3, YELLOW)
        screen.blit(text, (28, 268))

        text = font.render("#3", 3, DARK_RED)
        screen.blit(text, (30, 320))
        text = font.render("#3", 3, YELLOW)
        screen.blit(text, (28, 318))

        text = font.render("#4", 3, DARK_RED)
        screen.blit(text, (30, 370))
        text = font.render("#4", 3, YELLOW)
        screen.blit(text, (28, 368))

        text = font.render("#5", 3, DARK_RED)
        screen.blit(text, (30, 420))
        text = font.render("#5", 3, YELLOW)
        screen.blit(text, (28, 418))

        text = font.render(results[0], 3, WHITE)
        screen.blit(text, (100, 230))

        text = font.render(results[1], 3, WHITE)
        screen.blit(text, (100, 270))

        text = font.render(results[2], 3, WHITE)
        screen.blit(text, (100, 320))

        text = font.render(results[3], 3, WHITE)
        screen.blit(text, (100, 370))

        text = font.render(results[4], 3, WHITE)
        screen.blit(text, (100, 420))

        enterKeyImage = pygame.image.load('enter key.png')
        enterKeyImage = pygame.transform.scale(enterKeyImage, (40, 50))
        screen.blit(enterKeyImage, (40, 510))

        font = pygame.font.Font('8-BitMadness.ttf', 30)
        title = font.render(": RETURN TO MENU", 1, WHITE)
        screen.blit(title, (90, 525))

        font = pygame.font.Font('8-BitMadness.ttf', 30)
        title = font.render("PRESS SPACE TO SEE ENTIRE LEADERBOARD", 1, YELLOW)
        screen.blit(title, (240, 555))

        # ~~CURSOR~~#

        # - The original cursor is made invisible
        #
        # - The x and y positions of the mouse is then stored in x and y variables
        #
        # - I will then oad the cursor image I made and then blit it in on the screen in the x and y position of the mouse

        x, y = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        cursor = pygame.image.load('cursor.png')
        cursor = pygame.transform.scale(cursor, (20, 20))
        screen.blit(cursor, (x, y))

        pygame.display.update()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


######################################
#                                    #
#         DEATH     SCREEN           #
#                                    #
######################################


def deathScreen():
    # - Loading screen is called here so that the player is aware that the game is processing.

    LoadingScreen()

    # pos1 is initially yellow (selected) because it is at the top of the screen
    # pos2 is white (unselected) initially because it is below pos1 on screen

    pos1 = YELLOW
    pos2 = WHITE

    # - Condition controlled loop runs as long as deathmenu is true
    # - there is then an event loop
    # - if there is a key press and that key press is the down arrow key then if pos1 is yellow
    #   then pos2 will be yellow and pos1 will be white
    # - if pos2 is yellow then nothing will happen
    # - if the key press is the up arrow key and if pos2 is yelow, then pos1 will be yellow and pos2 will be white
    # - If the key press is the return key and pos1 is yellow then deathmenu will become false which will end
    #   the loop, it will consequently rturn the player back to the HUB
    # - if pos2 is yellow when the return key is pressed then the menu screen will run.

    deathmenu = True
    while deathmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                deathmenu = False
            elif event.type == pygame.KEYDOWN:
                if pos1 == YELLOW:
                    if event.key == pygame.K_DOWN:
                        pos1 = WHITE
                        pos2 = YELLOW
                elif pos2 == YELLOW:
                    if event.key == pygame.K_UP:
                        pos1 = YELLOW
                        pos2 = WHITE
                if event.key == pygame.K_RETURN:
                    if pos1 == YELLOW:
                        deathmenu = False
                    elif pos2 == YELLOW:
                        run = False
                        menu()

        # - The code below is what is drawn to the screen
        # - RETURN TO HUB and MAIN MENU will be blitted to the screen
        # - the RETURN TO HUB text will have the colour pos1
        # - the MAIN MENU text will have the colour pos2

        deathBackground = pygame.image.load('death back.png')
        deathBackground = pygame.transform.scale(deathBackground, (800, 600))
        screen.blit(deathBackground, (0, 0))

        font = pygame.font.Font('8-BitMadness.ttf', 70)
        text = font.render("RETURN TO HUB", 2, pos1)
        screen.blit(text, (190, 300))

        text = font.render("MAIN MENU", 2, pos2)
        screen.blit(text, (240, 400))

        # ~~CURSOR~~#

        # - The original cursor is made invisible
        #
        # - The x and y positions of the mouse is then stored in x and y variables
        #
        # - I will then oad the cursor image I made and then blit it in on the screen in the x and y position of the mouse

        x, y = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        cursor = pygame.image.load('cursor.png')
        cursor = pygame.transform.scale(cursor, (20, 20))
        screen.blit(cursor, (x, y))

        pygame.display.update()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#########################################
#                                       #
#         INSTRUCTIONS SCREEN           #
#                                       #
#########################################


def instructionScreen():
    LoadingScreen()

    ##################
    # ~~ PAGE ONE ~~ #
    ##################

    def pageOne():

        # - The code below simply blits the instructions text and images to the screen in an arranged position so that all text is readable
        #   and all images are viewable
        # - Page one shows the player the controls so I have created and included some images that depict the key the player must press to
        #   perform a particular action. These images will clearly accompany some text that will explain what pressing that button will do.

        Background = pygame.image.load('pauseback.png')
        Background = pygame.transform.scale(Background, (800, 600))
        screen.blit(Background, (0, 0))

        font = pygame.font.Font('8-BitMadness.ttf', 70)
        title = font.render("INSTRUCTIONS", 1, DARK_RED)
        screen.blit(title, (220, 60))
        title = font.render("INSTRUCTIONS", 1, WHITE)
        screen.blit(title, (217, 57))

        font = pygame.font.Font('8-BitMadness.ttf', 45)

        title = font.render("CONTROLS", 1, DARK_RED)
        screen.blit(title, (310, 130))
        title = font.render("CONTROLS", 1, WHITE)
        screen.blit(title, (307, 127))

        text = font.render("MOVEMENT", 3, DARK_RED)
        screen.blit(text, (75, 170))

        wasdImage = pygame.image.load('wasd keys.png')
        wasdImage = pygame.transform.scale(wasdImage, (135, 95))
        screen.blit(wasdImage, (95, 220))

        text = font.render("SHOOTING", 3, DARK_RED)
        screen.blit(text, (540, 170))

        arrowImage = pygame.image.load('arrow keys.png')
        arrowImage = pygame.transform.scale(arrowImage, (135, 95))
        screen.blit(arrowImage, (460, 220))

        text = font.render("SELECTION", 3, DARK_RED)
        screen.blit(text, (70, 360))

        arrowImage = pygame.image.load('enter key.png')
        arrowImage = pygame.transform.scale(arrowImage, (70, 90))
        screen.blit(arrowImage, (130, 420))

        text = font.render("OTHER", 3, DARK_RED)
        screen.blit(text, (570, 360))

        arrowImage = pygame.image.load('p key.png')
        arrowImage = pygame.transform.scale(arrowImage, (50, 50))
        screen.blit(arrowImage, (530, 410))

        font = pygame.font.Font('8-BitMadness.ttf', 40)
        text = font.render("PAUSE", 3, WHITE)
        screen.blit(text, (600, 420))

        arrowImage = pygame.image.load('u key.png')
        arrowImage = pygame.transform.scale(arrowImage, (50, 50))
        screen.blit(arrowImage, (480, 490))

        text = font.render("LEADERBOARD", 3, WHITE)
        screen.blit(text, (550, 490))

        text = font.render("UPDATE", 3, WHITE)
        screen.blit(text, (550, 520))

        font = pygame.font.Font('8-BitMadness.ttf', 30)
        text = font.render("(PRESS ENTER FOR NEXT PAGE)", 3, YELLOW)
        screen.blit(text, (20, 540))

        text = font.render("(SPACE TO", 3, WHITE)
        screen.blit(text, (620, 230))
        text = font.render("CHANGE", 3, WHITE)
        screen.blit(text, (620, 260))
        text = font.render("WEAPON)", 3, WHITE)
        screen.blit(text, (620, 290))

        pygame.draw.line(screen, WHITE, (390, 190), (390, 550), )

        pygame.display.update()

    ##################
    # ~~ PAGE TWO ~~ #
    ##################

    def pageTwo():

        # - Similarly to page one, page two simply displays some text on the screen. There are no images in page two.
        # - Page two explains to the player how to play the game and what the objectives are.

        Background = pygame.image.load('pauseback.png')
        Background = pygame.transform.scale(Background, (800, 600))
        screen.blit(Background, (0, 0))

        font = pygame.font.Font('8-BitMadness.ttf', 70)
        title = font.render("HOW TO PLAY", 1, DARK_RED)
        screen.blit(title, (220, 60))
        title = font.render("HOW TO PLAY", 1, WHITE)
        screen.blit(title, (217, 57))

        font = pygame.font.Font('8-BitMadness.ttf', 30)

        title = font.render("- COMPLETE LEVELS BY KILLING ALL ENEMIES AND LEAVING", 1, WHITE)
        screen.blit(title, (30, 127))
        title = font.render("VIA THE RED PLATFORM", 1, WHITE)
        screen.blit(title, (30, 157))

        title = font.render("- ENEMIES WILL TRACK YOU DOWN WHEN YOU GET CLOSE", 1, WHITE)
        screen.blit(title, (30, 197))

        title = font.render("- CHOOSE LEVEL IN THE HUB BY SELECTING A PLATFORM", 1, WHITE)
        screen.blit(title, (30, 237))

        title = font.render("- ONCE ALL LEVELS COMPLETE, IF YOU WOULD LIKE TO", 1, WHITE)
        screen.blit(title, (30, 277))
        title = font.render("SAVE YOUR TIME EITHER EXIT TO MENU OR PRESS 'U' ", 1, WHITE)
        screen.blit(title, (30, 307))

        title = font.render("- PICK UP ARMOUR BY WALKING OVER PICKUP WHEN ARMOUR", 1, WHITE)
        screen.blit(title, (30, 347))
        title = font.render("IS LOW", 1, WHITE)
        screen.blit(title, (30, 377))

        title = font.render("- PICK UP HEALTH BY WALKING OVER PICKUP WHEN HEALTH", 1, WHITE)
        screen.blit(title, (30, 417))
        title = font.render("IS LOW", 1, WHITE)
        screen.blit(title, (30, 437))

        title = font.render("- GOAL IS TO FINISH LEVEL AS FAST AS POSSIBLE", 1, WHITE)
        screen.blit(title, (30, 477))

        title = font.render("(PRESS ENTER TO RETURN TO MENU)", 1, YELLOW)
        screen.blit(title, (180, 527))

        pygame.display.update()

    # - Below is a condition controlled loop that runs as long as instruct is True
    # - pgOne is created and given the boolean value True
    # - Within the count controlled loop, an if statement detects whether pgOne = True, if it is then the pageOne procedure is called
    # - Otherwise, the pageTwo procedure will be called.
    # - There is then a count controlled loop that checks for events.
    # - If the event type is quit then instruct will = False which will end the condition controlled loop
    # - If the event type is a key press then it will check whether pgOne is True or False
    # - if it is True and the event key is the return key, then the pgOne variable will = False.
    # - If it is False and the event key is the return key then the instruct variable will be false, ending the conditon controlled loop
    #   and the menu function will be called

    pgOne = True
    instruct = True
    while instruct:
        if pgOne == True:
            pageOne()
        else:
            pageTwo()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instruct = False
            elif event.type == pygame.KEYDOWN:
                if pgOne:
                    if event.key == pygame.K_RETURN:
                        pgOne = False
                elif pgOne == False:
                    if event.key == pygame.K_RETURN:
                        instruct = False
                        menu()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#########################################
#                                       #
#         M     E     N     U           #
#                                       #
#########################################


def menu():
    LoadingScreen()

    mixer.music.load('d_e1m2 (1).mp3')
    mixer.music.play(-1)

    # - pos1, pos2, pos3 and pos4 have been defined below, pos1 referring to the first option in the menu
    #   pos2 being the second, and so on. these varibales will hold the colours of the text displayed on the menu
    #   screen. If it is yellow then it has been selected, if it is white then it has not been selected.

    pos1 = YELLOW
    pos2 = WHITE
    pos3 = WHITE
    pos4 = WHITE

    # ~NAVIGATION LOGIC~#
    # - Below is a condition controlled loop that runs so long as menuRun = True.
    # - There is then an event loop that will be used to detect the inputs from the user.
    # - If the event type is quit then menuRun will = False, which will end the condition controlled loop which will
    #   subsequently end the game
    # - If the event type is a key press, an if statement will check which pos variable is YELLOW.
    # - If pos1 = YELLOW and the event key is the down arrow then pos1 will become white, pos2 will become yellow and the
    #   other two options will stay white
    # - If pos2 = YELLOW and the event key is the down arrow then pos2 will become white and pos3 will become white
    #   , the other two will stay white. if the event key is the up arrow then pos1 will become yellow, pos2 will become
    #   white and the other two will stay white.
    # - If pos3 = YELLOW and the event key is the down arrow, then pos4 will become yellow, pos3 will become white and
    #   the other two will stay white. If the even tkey is the up arrow then pos2 will become yellow, pos3 will become
    #   white and the other two will stay white
    # - If pos4 = YELLOW and the event key is the up arrow then pos3 will beocme yellow, pos4 will become white and the
    #   other two will stay white.
    # - The logic above allows the user to be able to scroll down and up the menu using the arrow keys.

    # ~SELECTION LOGIC~#
    # - If the player wants to select an option in the menu, the must press the return key.
    # - If the event key is the return key at any point then it will check which pos variable is YELLOW and then
    #   run the corresponding function or procedure so that the action occurs.
    # - Read through the annotated code below to see where each option is being selected

    # ~pos1 SELECTION~#
    # - If pos1 is YELLOW and the event key is return then the play option has been selected which means
    #   menuRun will = False, ending the condition controlled loop, the nameInput procedure is called to
    #   get the user's name and the val variable is created which keeps track of which level in the game
    #   has been completed. a condition controlled loop is then created which runs so long as the variable
    #   play = True. The game function is then called with HUB and val passed in as parameters. For the game
    #   function, the first parameter is the layout of the level that the function will run on and val is
    #   what keeps track of what levels have been completed already.
    # - When the game function is ran with the HUB layout, it will return a value for the level that has been
    #   selected. This is stored in the variable level.
    # - If level = 1 then the game function will run with the levelONElayout and 0 as val because there are
    #   no blockades
    # - if level = 2 then the game function will run with the levelTWOlayout and 0 as val
    # - If level = 3 then the game function will run with the levelTHREElayout and 0 as val

    # ~pos2 SELECTION~#
    # - If pos2 is YELLOW and the event key is return then the leaderboard option has been chosen which means
    #   that menuRun will become False, ending the condition controlled loop and the leaderboardScreen procedure
    #   will be called

    # ~pos3 SELECTION~#
    # - If pos3 is YELLOW and the event key is return then the instructions option has been chosen which means
    #   that menuRun will become False, ending the condition controlled loop and the instructionsScreen
    #   procedure will be called

    # ~pos4 SELECTION~#
    # - If pos4 is YELLOW and the event key is return then the quit option has been chosen which means that the
    #   sys module will be used to exit the game using the sys.exit() procedure.

    menuRun = True
    while menuRun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuRun = False
            elif event.type == pygame.KEYDOWN:
                if pos2 == YELLOW:
                    if event.key == pygame.K_DOWN:
                        pos1 = WHITE
                        pos2 = WHITE
                        pos3 = YELLOW
                        pos4 = WHITE
                    elif event.key == pygame.K_UP:
                        pos1 = YELLOW
                        pos2 = WHITE
                        pos3 = WHITE
                        pos4 = WHITE
                elif pos4 == YELLOW:
                    if event.key == pygame.K_UP:
                        pos1 = WHITE
                        pos2 = WHITE
                        pos3 = YELLOW
                        pos4 = WHITE
                elif pos1 == YELLOW:
                    if event.key == pygame.K_DOWN:
                        pos1 = WHITE
                        pos2 = YELLOW
                        pos3 = WHITE
                        pos4 = WHITE
                elif pos3 == YELLOW:
                    if event.key == pygame.K_DOWN:
                        pos1 = WHITE
                        pos2 = WHITE
                        pos3 = WHITE
                        pos4 = YELLOW
                    elif event.key == pygame.K_UP:
                        pos1 = WHITE
                        pos2 = YELLOW
                        pos3 = WHITE
                        pos4 = WHITE
                if event.key == pygame.K_RETURN:

                    # If pos1 has been selected (PLAY)

                    if pos1 == YELLOW:
                        menuRun = False
                        nameInput()
                        val = 0
                        level = 0
                        play = True
                        while play:
                            if level == 1:
                                val = game(levelONElayout, 0)
                                level = 0
                            elif level == 2:
                                val = game(levelTWOlayout, 0)
                                level = 0
                            elif level == 3:
                                val = game(levelTHREElayout, 0)
                                level = 0
                            elif level == 4:
                                break
                            elif level == 5:
                                level = game(HUB2, val)
                            elif level == 6:
                                val = game(levelFOURlayout, 0)
                                level = 0
                            elif level == 7:
                                val = game(levelFIVElayout, 0)
                                level = 0
                            elif level == 8:
                                game(levelSIXlayout, 0)
                                level = 0
                            else:
                                level = game(HUB, val)

                        # If pos2 has been selected (LEADERBOARD)

                    elif pos2 == YELLOW:
                        menuRun = False
                        leaderboardScreen()
                        pos1 = YELLOW
                        pos2 = WHITE

                        # If pos3 has been selected (INSTRUCTIONS)

                    elif pos3 == YELLOW:
                        menuRun = False
                        instructionScreen()

                        # If pos4 has been selected (QUIT)

                    elif pos4 == YELLOW:
                        sys.exit()

        # The code below draws the Menu screen to the display, starting with the background

        menuBackground = pygame.image.load('menubackground.png')
        menuBackground = pygame.transform.scale(menuBackground, (800, 600))
        screen.blit(menuBackground, (0, 0))

        # The text below is given the colour pos1, this will be the first option on the menu
        # so its position will be above all the other text

        font = pygame.font.Font('8-BitMadness.ttf', 70)
        text = font.render("PLAY", 2, pos1)
        overlaytext = font.render("PLAY", 1, DARK_RED)
        screen.blit(text, (50, 260))
        screen.blit(overlaytext, (48, 258))

        # The text below is given the colour pos2, this will be the second option on the menu
        # so its position will be above all the other text but below the first option

        overlaytext = font.render("LEADERBOARD", 2, DARK_RED)
        text = font.render("LEADERBOARD", 2, pos2)
        screen.blit(text, (50, 320))
        screen.blit(overlaytext, (48, 318))

        # The text below is given the colour pos3, this will be the third option on the menu
        # so its position will be above the bottom option but below everything else

        overlaytext = font.render("INSTRUCTIONS", 2, DARK_RED)
        text = font.render("INSTRUCTIONS", 2, pos3)
        screen.blit(text, (50, 380))
        screen.blit(overlaytext, (48, 378))

        # The text below is given the colour pos4, this will be the second option on the menu
        # so its position will be at the bottom of all the other text

        overlaytext = font.render("QUIT", 2, DARK_RED)
        text = font.render("QUIT", 2, pos4)
        screen.blit(text, (50, 440))
        screen.blit(overlaytext, (48, 438))

        UpDownKeyImage = pygame.image.load('up down keys.png')
        UpDownKeyImage = pygame.transform.scale(UpDownKeyImage, (25, 50))
        screen.blit(UpDownKeyImage, (30, 515))

        font = pygame.font.Font('8-BitMadness.ttf', 30)
        title = font.render(": NAVIGATE", 1, WHITE)
        screen.blit(title, (60, 525))

        enterKeyImage = pygame.image.load('enter key.png')
        enterKeyImage = pygame.transform.scale(enterKeyImage, (40, 50))
        screen.blit(enterKeyImage, (220, 515))

        font = pygame.font.Font('8-BitMadness.ttf', 30)
        title = font.render(": SELECT", 1, WHITE)
        screen.blit(title, (265, 525))

        # ~~CURSOR~~#
        x, y = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        cursor = pygame.image.load('cursor.png')
        cursor = pygame.transform.scale(cursor, (20, 20))
        screen.blit(cursor, (x, y))

        pygame.display.update()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#####################
# ~WHERE CODE STARTS~#
#####################

menu()

