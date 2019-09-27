import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from our spaceship. """

    def __init__(self, infrompy_settings, screen, ship):
        """" Create a bullet object at the ship's position. """
        super(Bullet, self).__init__()
        self.screen = screen

        #Create a bullet at position (0,0) and then set the correct position.
        self.rect = pygame.Rect(0,0, infrompy_settings.bullet_width, infrompy_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = infrompy_settings.bullet_color
        self.speed = infrompy_settings.bullet_speed

    def update(self):
        """ Move the bullet up the screen. """
        # update the decimal position of the bullet
        self.y -= self.speed
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet to the screen. """
        pygame.draw.rect(self.screen, self.color, self.rect)