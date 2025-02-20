class World:
    def __init__(self, size, dt):
        """Initializes the World class with a list of bodies"""
        self.bodies = []
        self.size = size
        self.dt = dt
        self.simuation_data = {
            "body_index": [],
            "position_x": [],
            "position_y": [],
            "position_z": [],
        }

    def border(self, size):
        """Creates a border if the user decides to implement a position limit"""

        
