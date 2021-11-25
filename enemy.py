import pygame
import random
import time

#~IMP CLASS~#

class Imp(pygame.sprite.Sprite):
  
  # - Below is the initiation of the enemy class.
  # - The base image for the enemy sprite is loaded and its rect values are defined
  #   in self.rect
  # - The speed variable is then defined
  # - The health variable is also defined 
  
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load("Doom imp still.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    self.rect = self.image.get_rect()
    self.speed = 1
    self.health = 50
  
  #~moveRight PROCEDURE~#
  
    # - The procedure below loads the walking variant of the enemy sprite image
    #   in the right direction
    # - There is then a timer that starts and if the current time % 0.7 is 
    #   greater than 0.35, the sprite image will change back to the original state
    # - This causes the effect of a walking animation.
    # - The main purpose of this procedure though is to move the enemy sprite 
    #   to the right, it does this by moving the sprites x position in the positive direction
    #   at the rate of the speed variable which is given as a parameter.
    # - The code below that then checks whether the enemy sprite has moved out of the
    #   the right of the screen boundaries.
  
  def moveRight (self):
    self.image = pygame.image.load("doom imp run.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    if time.time() % 0.7 > 0.35:
      self.image = pygame.image.load("Doom imp still.png")
      self.image = pygame.transform.scale(self.image,(30,30))
    self.rect.x += self.speed
    if self.rect.x > 760:
      self.rect.x = 760
  
  #~moveLeft PROCEDURE~#
  
    # - The procedure below loads the walking variant of the enemy sprite image
    #   in the left direction
    # - There is then a timer that starts and if the current time % 0.7 is 
    #   greater than 0.35, the sprite image will change back to the original state
    # - This causes the effect of a walking animation.
    # - The main purpose of this procedure though is to move the enemy sprite 
    #   to the left, it does this by moving the sprites x position in the negative direction
    #   at the rate of the speed variable which is given as a parameter.
    # - The code below that then checks whether the enemy sprite has moved out of the
    #   the left of the screen boundaries.
  
  def moveLeft (self):
    self.image = pygame.image.load("doom imp run.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    self.image = pygame.transform.flip(self.image,True,False)
    if time.time() % 0.7 > 0.35:
      self.image = pygame.image.load("Doom imp still.png")
      self.image = pygame.transform.scale(self.image,(30,30))
      self.image = pygame.transform.flip(self.image,True,False)
    self.rect.x -= self.speed
    if self.rect.x < 0:
      self.rect.x = 0
  
  #~transformRight PROCEDURE~#
  
  # - This procedure changes the enemy sprite image to the still right
  #   direction variant
  
  def transformRight(self):
    self.image = pygame.image.load("Doom imp still.png")
    self.image = pygame.transform.scale(self.image,(30,30))
  
  #~transformLeft PROCEDURE~#
  
  # - This procedure changes the enemy sprite image to the still left
  #   direction variant
  
  def transformLeft(self):
    self.image = pygame.image.load("Doom imp still.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    self.image = pygame.transform.flip(self.image,True,False)
  
  #~knockbackLeft PROCEDURE~#
  
  # - This procedure moves the Imp sprite 15 pixels to the left
  
  def knockbackLeft(self):
    self.rect.x -= 15
  
  #~knockbackRight PROCEDURE~#
  
  # - This procedure moves the Imp sprite 15 pixels to the right
  
  def knockbackRight(self):
    self.rect.x += 15

  #~knockbackDown PROCEDURE~#
  
  # - This procedure moves the Imp sprite 15 pixels downwards

  def knockbackDown(self):
    self.rect.y += 15
  
  #~knockbackUp PROCEDURE~#
  
  # - This procedure moves the Imp sprite 15 pixels up
  
  def knockbackUp(self):
    self.rect.y -= 15
  
  #~healthDecrease PROCEDURE~#
  
  # - This procedure removes a value of 10 from the self.health variable
  
  def healthDecrease (self):
    self.health -= 10
  
  #~healthCheck FUNCTION~#
  
  # - This function will return True if the self.health variable is less
  #   than or equal to 0
  # - Otherwise it will return False

  def healthCheck (self):
    if self.health <=0:
      return True
    else:
      return False

#~DemonSoldier SUBCLASS~#

# - This class is completely identical to the IMP class however,
# - The images are different
# - The self.speed variable is 2 instead of 1 (moves faster)
# - The self.health variable is 100 instead of 50 (harder to defeat)

class DemonSoldier(Imp):
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load("doom zombie still.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    self.rect = self.image.get_rect()
    self.speed = 2
    self.health = 100
  
  def moveRight (self):
    self.image = pygame.image.load("doom zombie walk.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    if time.time() % 0.7 > 0.35:
      self.image = pygame.image.load("doom zombie still.png")
      self.image = pygame.transform.scale(self.image,(30,30))
    self.rect.x += self.speed
    if self.rect.x > 760:
      self.rect.x = 760
  
  def moveLeft (self):
    self.image = pygame.image.load("doom zombie walk.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    self.image = pygame.transform.flip(self.image,True,False)
    if time.time() % 0.7 > 0.35:
      self.image = pygame.image.load("doom zombie still.png")
      self.image = pygame.transform.scale(self.image,(30,30))
      self.image = pygame.transform.flip(self.image,True,False)
    self.rect.x -= self.speed
    if self.rect.x < 0:
      self.rect.x = 0
  
  def transformRight(self):
    self.image = pygame.image.load("doom zombie still.png")
    self.image = pygame.transform.scale(self.image,(30,30))

  def transformLeft(self):
    self.image = pygame.image.load("doom zombie still.png")
    self.image = pygame.transform.scale(self.image,(30,30))
    self.image = pygame.transform.flip(self.image,True,False)


#~Cacodemon SUBCLASS~#

# - This class is completely identical to the IMP class however,
# - The images are different
# - The self.speed variable is 2 instead of 1 (moves faster)
# - The self.health variable is 200 instead of 50 (harder to defeat)


class Cacodemon(Imp):
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load("cacodemon look right.png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.rect = self.image.get_rect()
    self.speed = 2
    self.health = 200
  
  def moveRight (self):
    self.image = pygame.image.load("cacodemon look right.png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.rect.x += self.speed
    if self.rect.x > 760:
      self.rect.x = 760
  
  def moveLeft (self):
    self.image = pygame.image.load("cacodemon look left.png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.rect.x -= self.speed
    if self.rect.x < 0:
      self.rect.x = 0
  
  def transformRight(self):
    self.image = pygame.image.load("cacodemon look right.png")
    self.image = pygame.transform.scale(self.image,(40,40))

  def transformLeft(self):
    self.image = pygame.image.load("cacodemon look left.png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.image = pygame.transform.flip(self.image,True,False)

class Marauder(Imp):
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load("doom marauder.png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.rect = self.image.get_rect()
    self.speed = 2
    self.health = 800
  
  def moveRight (self):
    self.image = pygame.image.load("doom marauder.png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.rect.x += self.speed
    if self.rect.x > 760:
      self.rect.x = 760
  
  def moveLeft (self):
    self.image = pygame.image.load("doom marauder.png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.rect.x -= self.speed
    if self.rect.x < 0:
      self.rect.x = 0
  
  def transformRight(self):
    self.image = pygame.image.load("doom marauder.png")
    self.image = pygame.transform.scale(self.image,(40,40))

  def transformLeft(self):
    self.image = pygame.image.load("doom marauder.png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.image = pygame.transform.flip(self.image,True,False)

