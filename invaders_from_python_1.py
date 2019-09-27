import sys

import pygame
from pygame.sprite import Group


from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien 
import game_functions as gf

def run_game():
    """initialize game and create a screen object."""
    pygame.init()
    infrompy_settings = Settings()
    screen = pygame.display.set_mode((infrompy_settings.screen_width, infrompy_settings.screen_height))
    pygame.display.set_caption("Invaders from python")

    # Make a play button
    play_button = Button(infrompy_settings, screen, "Play")

    # Create an instance to store game stats and create a scoreboard
    stats = GameStats(infrompy_settings)
    sb = Scoreboard(infrompy_settings, screen, stats)

    # Make a ship, a broup of bullets and a group of aliens
    ship = Ship(infrompy_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(infrompy_settings, screen, ship, aliens)


    # Start the main loop for the game.
    while True:
        gf.check_events(infrompy_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
                ship.update()
                gf.update_bullets(infrompy_settings, screen, stats, sb, ship, aliens, bullets)
                gf.update_aliens(infrompy_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(infrompy_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()