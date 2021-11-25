import pygame

#~Levelplatform CLASS~#

class Levelplatform(pygame.sprite.Sprite):
  
  # - Below is the initiation of the Levelplatform class.
  # - The base image for the Levelplatform sprite is loaded and its rect values are defined
  #   in self.rect
  
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load("levelplatform.png")
    self.image = pygame.transform.scale(self.image,(30,19))
    self.rect = self.image.get_rect()