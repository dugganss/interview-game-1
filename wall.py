import pygame

#~Wall CLASS~#

class Wall(pygame.sprite.Sprite):
  
  # - Below is the initiation of the wall class.
  # - The base image for the wall sprite is loaded and its rect values are defined
  #   in self.rect
  
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load("bigwall.png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.rect = self.image.get_rect()
  
  #~blockade PROCEDURE~#
  
  # - The blockade procedure simply changes the image of the wall sprite when called
  
  def blockade(self):
    self.image = pygame.image.load("blockade.png")
    self.image = pygame.transform.scale(self.image,(40,40))