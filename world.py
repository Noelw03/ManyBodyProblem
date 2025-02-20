import json

class World:
    def __init__(self, size, dt):
        """Initializes the World class with a list of bodies"""
        self.bodies = []
        self.size = size
        self.dt = dt
        self.simulation_data = {
            "time_step": [],
            "body_index": [],
            "position_x": [],
            "position_y": [],
            "position_z": [],
        }

    def border(self, size):
        """Creates a border if the user decides to implement a position limit"""

    def save_to_json(self, filename):
        """Saves the simulation data to a JSON file"""
        simulation_output = {}
        max_time_step = max(self.simulation_data["time_step"])  # Find the total number of time steps
        for time_step in range(max_time_step + 1):  # Iterate through each time step
            indices = [i for i, t in enumerate(self.simulation_data["time_step"]) if t == time_step]
            
            x_positions = [self.simulation_data["position_x"][i] for i in indices]
            y_positions = [self.simulation_data["position_y"][i] for i in indices]
            z_positions = [self.simulation_data["position_z"][i] for i in indices]

            # Store in the desired format
            simulation_output[time_step] = {
                "positions": [x_positions, y_positions, z_positions]
            }
        # Save the reformatted data to a JSON file
        with open(filename, 'w') as json_file:
            json.dump(simulation_output, json_file)

    def record_simulation_step(self, time_step):
        """Record the current state of the simulation.
        """
        for i, body in enumerate(self.bodies):
                self.simulation_data["time_step"].append(time_step)
                self.simulation_data["body_index"].append(i)
                self.simulation_data["position_x"].append(body.position[0])
                self.simulation_data["position_y"].append(body.position[1])
                self.simulation_data["position_z"].append(body.position[2])

