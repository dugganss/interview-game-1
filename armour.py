import pygame

#~Armour CLASS~#

class Armour(pygame.sprite.Sprite):
  
  # - Below is the initiation of the Armour class.
  # - The base image for the Armour sprite is loaded and its rect values are defined
  #   in self.rect
  
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load("armour.png")
    self.image = pygame.transform.scale(self.image,(23,18))
    self.rect = self.image.get_rect()