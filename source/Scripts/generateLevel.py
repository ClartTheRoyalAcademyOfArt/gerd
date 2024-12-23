import random





class generateLevel:

    def __init__(self, level_scale:str):

        self.scale_options = {
            "small" : 50,
            "medium" : 75,
            "large" : 100
        }

        # TEMP TERRAIN TYPES FOR TESTING
        self.terrain_types = {
            # type    # color (r, g, b)
            "flats" : (87, 244, 92),
            "forest" : (33, 137, 15)
        }

        # Initialize arguments
        self.level_scale = level_scale

    

    def fill_level(self):

        grid_size = self.scale_options[self.level_scale]
        terrain_keys = list(self.terrain_types.keys())


        grid = [random.choice(terrain_keys) for _ in range(grid_size) for _ in range(grid_size)]

        return grid