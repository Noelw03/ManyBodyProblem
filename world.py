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

    def record_simulation_step(self, time_step):
        """Record the current state of the simulation.
        """
        for i, body in enumerate(self.humans):
                self.simuation_data["time_step"].append(time_step)
                self.simuation_data["body_index"].append(i)
                self.simuation_data["position_x"].append(body.position[0])
                self.simuation_data["position_y"].append(body.position[1])
                self.simuation_data["position_z"].append(body.position[2])


        
