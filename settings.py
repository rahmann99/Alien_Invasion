class Settings:
    """A class for game settings and inintializing down there """
    def __init__(self):
        
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.ship_speed = 3

        #Bullet settings
        self.bullet_speed = 5
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (255, 255, 50)
        self.bullets_allowed = 10