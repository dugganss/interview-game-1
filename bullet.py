import pygame

#~Bullet CLASS~#

class Bullet(pygame.sprite.Sprite):
  
  # - Below is the initiation of the bullet class.
  # - The base image for the bullet sprite is loaded and its rect values are defined
  #   in self.rect
  
  def __init__ (self):
    super().__init__()
    self.image = pygame.image.load("doom bullet.png")
    self.image = pygame.transform.scale(self.image,(5,5))
    self.rect = self.image.get_rect()
  
  #~shootLeft PROCEDURE~#
  
  # - This procedure changes the x position of the bullet sprite by -8
  #   (to the left)
  
  def shootLeft (self):
    self.rect.x -= 8
  
  #~shootRight PROCEDURE~#
  
  # - This procedure changes the x position of the bullet sprite by +8
  #   (to the right)
  
  def shootRight (self):
    self.rect.x += 8
  
  #~shootUp PROCEDURE~#
  
  # - This procedure changes the y position of the bullet sprite by -8
  #   (upwards)
  
  def shootUp (self):
    self.rect.y -= 8
  
  #~shootDown PROCEDURE~#
  
  # - This procedure changes the y position of the bullet sprite by +8
  #   (downwards)
  
  def shootDown (self):
    self.rect.y += 8
  
  #~shootUpLeft PROCEDURE~#
  
  # - This procedure changes the y position of the bullet sprite by -8
  #   and the x position of the bullet by -3 (up and slightly to the left)
  
  def shootUpLeft (self):
    self.rect.y -= 8
    self.rect.x -= 3
  
  #~shootUpRight PROCEDURE~#
  
  # - This procedure changes the y position of the bullet sprite by -8
  #   and the x position of the bullet by +3 (up and slightly to the right)
  
  def shootUpRight (self):
    self.rect.y -= 8
    self.rect.x += 3
  
  #~shootDownLeft PROCEDURE~#
  
  # - This procedure changes the y position of the bullet sprite by +8
  #   and the x position of the bullet by -3 (down and slightly to the left)
    
  def shootDownLeft (self):
    self.rect.y += 8
    self.rect.x -= 3
    
  #~shootDownRight PROCEDURE~#
  
  # - This procedure changes the y position of the bullet sprite by +8
  #   and the x position of the bullet by +3 (down and slightly to the right)
  
  def shootDownRight (self):
    self.rect.y += 8
    self.rect.x += 3
    
  #~shootLeftUp PROCEDURE~#
  
  # - This procedure changes the x position of the bullet sprite by +8
  #   and the y position of the bullet by +3 (left and slightly upwards)
    
  def shootLeftUp (self):
    self.rect.x -= 8
    self.rect.y -= 3
  
  #~shootLeftDown PROCEDURE~#
  
  # - This procedure changes the x position of the bullet sprite by -8
  #   and the y position of the bullet by +3 (left and slightly downwards)
  
  def shootLeftDown (self):
    self.rect.x -= 8
    self.rect.y += 3
  
  #~shootRightUp PROCEDURE~#
  
  # - This procedure changes the x position of the bullet sprite by +8
  #   and the y position of the bullet by -3 (right and slightly upwards)
  
  def shootRightUp (self):
    self.rect.x += 8
    self.rect.y -= 3
  
  #~shootRightUp PROCEDURE~#
  
  # - This procedure changes the x position of the bullet sprite by +8
  #   and the y position of the bullet by +3 (right and slightly downwards)
  
  def shootRightDown (self):
    self.rect.x += 8
    self.rect.y += 3