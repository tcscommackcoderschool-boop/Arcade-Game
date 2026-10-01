import arcade 
from ai_car import AICar

class AICarList(arcade.SpriteList):
    def __init__(self, num_cars, checkpoints, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for car in range(num_cars):
            self.append(AICar(cur_checkpoint=0, checkpoints=checkpoints))
