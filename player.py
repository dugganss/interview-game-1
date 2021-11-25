import pygame

import time

#~PLAYER CLASS~#

class Player(pygame.sprite.Sprite):
  
  # - Below is the initiation of the player class.
  # - The base image for the player sprite is loaded and its rect values are defined
  #   in self.rect
  
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load("doom guy still.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    self.rect = self.image.get_rect()
  
  #~enlarge PROCEDURE~#
  
    # - The procedure below makes the player sprite larger. (from 30x30 to 80x80)
  
  def enlarge (self):
    self.image = pygame.transform.scale(self.image,(80,80))
  
  #~moveUP PROCEDURE~#
  
    # - The procedure below loads the walking variant of the player sprite image
    #   in the up direction
    # - There is then a timer that starts and if the current time % 0.7 is 
    #   gretaer than 0.35, the sprite image will change back to the original state
    # - This causes the effect of a walking animation.
    # - The main purpose of this procedure though is to move the player sprite 
    #   upward, it does this by moving the sprites y position in the negative direction
    #   at the rate of the speed variable which is given as a parameter.
    # - The code below that then checks whether the player sprite has moved out of the
    #   the top of the screen boundaries.
  
  def moveUp (self, speed):
    self.image = pygame.image.load("doom guy up walk.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    if time.time() % 0.7 > 0.35:
      self.image = pygame.image.load("doom guy up still.png")
      self.image = pygame.transform.scale(self.image,(30,30))
    self.rect.y -= speed
    if self.rect.y < 0:
      self.rect.y = 0
  
  
  #~moveDown PROCEDURE~#
  
    # - The procedure below loads the walking variant of the player sprite image
    #   in the down direction
    # - There is then a timer that starts and if the current time % 0.7 is 
    #   greater than 0.35, the sprite image will change back to the original state
    # - This causes the effect of a walking animation.
    # - The main purpose of this procedure though is to move the player sprite 
    #   downward, it does this by moving the sprites y position in the positive direction
    #   at the rate of the speed variable which is given as a parameter.
    # - The code below that then checks whether the player sprite has moved out of the
    #   the bottom of the screen boundaries.
  
  def moveDown(self, speed):
    self.image = pygame.image.load("doom guy down walk.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    if time.time() % 0.7 > 0.35:
      self.image = pygame.image.load("doom guy down still.png")
      self.image = pygame.transform.scale(self.image,(30,30))
    self.rect.y += speed
    if self.rect.y > 420:
      self.rect.y = 420
  
  
  #~moveLeft PROCEDURE~#
  
    # - The procedure below loads the walking variant of the player sprite image
    #   in the left direction
    # - There is then a timer that starts and if the current time % 0.7 is 
    #   greater than 0.35, the sprite image will change back to the original state
    # - This causes the effect of a walking animation.
    # - The main purpose of this procedure though is to move the player sprite 
    #   to the left, it does this by moving the sprites x position in the negative direction
    #   at the rate of the speed variable which is given as a parameter.
    # - The code below that then checks whether the player sprite has moved out of the
    #   the left of the screen boundaries.
  
  def moveLeft(self, speed):
    self.image = pygame.image.load("doom guy walk.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    self.image = pygame.transform.flip(self.image,True,False)
    if time.time() % 0.7 > 0.35:
      self.image = pygame.image.load("doom guy still.png")
      self.image = pygame.transform.scale(self.image,(30,30))
      self.image = pygame.transform.flip(self.image,True,False)
    self.rect.x -= speed
    if self.rect.x < 0:
      self.rect.x = 0
  
  
  #~moveRight PROCEDURE~#
  
    # - The procedure below loads the walking variant of the player sprite image
    #   in the right direction
    # - There is then a timer that starts and if the current time % 0.7 is 
    #   greater than 0.35, the sprite image will change back to the original state
    # - This causes the effect of a walking animation.
    # - The main purpose of this procedure though is to move the player sprite 
    #   to the right, it does this by moving the sprites x position in the positive direction
    #   at the rate of the speed variable which is given as a parameter.
    # - The code below that then checks whether the player sprite has moved out of the
    #   the right of the screen boundaries.
  
  def moveRight(self, speed):
    self.image = pygame.image.load("doom guy walk.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    if time.time() % 0.7 > 0.35:
      self.image = pygame.image.load("doom guy still.png")
      self.image = pygame.transform.scale(self.image,(30,30))
    self.rect.x += speed
    if self.rect.x > 770:
      self.rect.x = 770
  
  
  #~directionUpStill PROCEDURE~#
  
  # - This procedure changes the player sprite image to the still up
  #   direction variant
  
  def directionUpStill (self):
    self.image = pygame.image.load("doom guy up still.png")
    self.image = pygame.transform.scale(self.image,(30,30))
  
  
  #~directionDownStill PROCEDURE~#
  
  # - This procedure changes the player sprite image to the still down
  #   direction variant
  
  def directionDownStill (self):
    self.image = pygame.image.load("doom guy down still.png")
    self.image = pygame.transform.scale(self.image,(30,30))
  
  
  #~directionRightStill PROCEDURE~#
  
  # - This procedure changes the player sprite image to the still right
  #   direction variant
  
  def directionRightStill (self):
    self.image = pygame.image.load("doom guy still.png")
    self.image = pygame.transform.scale(self.image,(30,30))
  
  
  #~directionLeftStill PROCEDURE~#
  
  # - This procedure changes the player sprite image to the still left
  #   direction variant
  
  def directionLeftStill (self):
    self.image = pygame.image.load("doom guy still.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    self.image = pygame.transform.flip(self.image,True,False)