import pygame

#~Healthpotion CLASS~#

class Healthpotion(pygame.sprite.Sprite):
  
  # - Below is the initiation of the healthpotion class.
  # - The base image for the healthpotion sprite is loaded and its rect values are defined
  #   in self.rect
  
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load("healthpotion.png")
    self.image = pygame.transform.scale(self.image,(17,17))
    self.rect = self.image.get_rect()