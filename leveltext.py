import pygame

#~Leveltext CLASS~#

class Leveltext(pygame.sprite.Sprite):
  
  # - Below is the initiation of the Leveltext class.
  # - The base image for the Leveltext sprite is loaded and its rect values are defined
  #   in self.rect
  
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load("e1m1text.png")
    self.image = pygame.transform.scale(self.image,(35,12))
    self.rect = self.image.get_rect()
  
  #~e1m2 PROCEDURE~#
  
  # - The e1m2 procedure simply changes the image of the Leveltext sprite when called
  
  def e1m2(self):
    self.image = pygame.image.load("e1m2text.png")
    self.image = pygame.transform.scale(self.image,(35,12))
  
  #~e1m3 PROCEDURE~#
  
  # - The e1m3 procedure simply changes the image of the Leveltext sprite when called
  
  def e1m3(self):
    self.image = pygame.image.load("e1m3text.png")
    self.image = pygame.transform.scale(self.image,(35,12))
  
  #~instructionsShoot PROCEDURE~#
  
  # - The instructionsShoot procedure simply changes the image of the Leveltext sprite when called
  
  def instructionsShoot(self):
    self.image = pygame.image.load("arrow keys.png")
    self.image = pygame.transform.scale(self.image,(90,50))
  
  #~instructionsMove PROCEDURE~#
  
  # - The instructionsMove procedure simply changes the image of the Leveltext sprite when called
  
  def instructionsMove(self):
    self.image = pygame.image.load("wasd keys.png")
    self.image = pygame.transform.scale(self.image,(90,50))