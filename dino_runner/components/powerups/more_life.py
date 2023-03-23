from dino_runner.utils.constants import HEART, HEART_TYPE
from dino_runner.components.powerups.power_up import PowerUp


class MoreLife(PowerUp):
    def __init__(self):
        self.image = HEART
        self.type = HEART_TYPE
        super().__init__(self.image, self.type)
