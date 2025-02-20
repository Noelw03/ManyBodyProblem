import numpy as np


class Body:
    def __init__(self, mass, position, velocity, acceleration):
        """Initializes the Body class with mass, position, velocity, and acceleration"""
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.acceleration = np.array(acceleration)

    def update_acceleration(self, force):
        """Updates the acceleration of the body"""
        self.acceleration = force / self.mass
        return self.acceleration
    
    def update_velocity(self, dt):
        """Updates the velocity of the body"""
        self.velocity += self.acceleration * dt
        return self.velocity

    def update_position(self, dt):
        """Updates the position of the body"""
        self.position += self.velocity * dt
        return self.position
    
    def calculate_force(self, other_body,):
        """Calculates the force between two bodies"""
        G = 6.67430e-11
        r = other_body.position - self.position
        r_norm = np.linalg.norm(r)
        if r_norm < 1: #prevents singularities
            r_norm = 1
        force = G * self.mass * other_body.mass / r_norm**3 * r
        return force

    def __str__(self):
        """Returns the relevant information about the body"""
        return(
            f"mass: {self.mass}\n"
            f"position: {self.position}\n"
            f"velocity: {self.velocity}\n"
            f"acceleration: {self.acceleration}\n"
        )
    


    