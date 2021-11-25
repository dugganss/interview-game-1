import pygame

#~Levelcomplete CLASS~#

class Trigger(pygame.sprite.Sprite):
  
  # - Below is the initiation of the Levelcomplete class.
  # - The base image for the Levelcomplete sprite is loaded and its rect values are defined
  #   in self.rect
  
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load("art (22).png")
    self.image = pygame.transform.scale(self.image,(40,40))
    self.rect = self.image.get_rect()