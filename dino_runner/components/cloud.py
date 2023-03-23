import random 
from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD

class Cloud():
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self, game):
        self.x -= game.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2000, 2500)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
