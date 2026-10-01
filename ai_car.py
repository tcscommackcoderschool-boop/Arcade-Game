from tracking_car import TrackingCar
import random
import arcade
rng = random.Random(42)

class AICar(TrackingCar):
    def __init__(self, cur_checkpoint, checkpoints, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if checkpoints is None:
            self.checkpoints = {}
        else:
            self.checkpoints = checkpoints

        self.cur_checkpoint = cur_checkpoint if cur_checkpoint is not None else None

        self.replay_movements = True  # AI car always replays movements
        self.movements = self.generate_movements(1000)  # Generate movements for 1000 frames
        

    def generate_movements(self, num_frames: int):
        """ Generates random movements for the AI car """
        
        for _ in range(num_frames):
            frame = []

            fb_move =rng.choice([0, 1, 2, 3, 6])
            if fb_move != 0:
                frame.append(fb_move)
           
            rl_move = rng.choice([0, 4, 5])
            if rl_move != 0:
                frame.append(rl_move)

            if len(frame) == 0:
                frame.append(0)  # Ensure at least one action per frame
            
            yield frame 

    def check_checkpoint(self):
        if self.cur_checkpoint in self.checkpoints:
            if arcade.check_for_collision_with_list(self, self.checkpoints[self.cur_checkpoint]):
                self.cur_checkpoint += 1
                if self.cur_checkpoint not in self.checkpoints:
                    self.cur_checkpoint = min(self.checkpoints.keys())

    def check_distance(self):
        if self.cur_checkpoint in self.checkpoints:
            min_distance = float('inf')
            for tile in self.checkpoints[self.cur_checkpoint]:
                distance = arcade.math.get_distance(*self.position, *tile.position)
                if distance < min_distance:
                    min_distance = distance
            return min_distance
        return float('inf')  # Return infinity if no checkpoint is current

    
   