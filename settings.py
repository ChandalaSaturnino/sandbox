class Settings():
    """ A class to store our games settings. """

    def __init__(self):
        """ Initialize our games settings and screen settings. """
        # Screen settings
        self.screen_width = 1200
        self.screen_height =700
        self.bg_color = (19, 120, 160)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

        # Alien settings        
        self.fleet_drop_speed = 30

        # How quickly the game speeds up
        self.speedup_scale = 1.2
        # How quickly the alien_point value increases
        self.score_scale = 1.5

        self.Initialize_dynamic_settings()

    def Initialize_dynamic_settings(self):
        """ Initialize settings that change during the game. """
        self.ship_speed = 3.5
        self.bullet_speed = 8
        self.alien_speed_factor = 2

        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 100
    
    def increase_speed(self):
        """ Increase speed settings and alien_point values. """
        self.ship_speed += self.speedup_scale
        self.bullet_speed += self.speedup_scale
        self.alien_speed_factor += self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
