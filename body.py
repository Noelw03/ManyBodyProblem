import numpy as np


class Body:
    def __init__(self, mass, position, velocity, acceleration):
        """Initializes the Body class with mass, position, velocity, and acceleration"""
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

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
        force = G * self.mass * other_body.mass / r_norm**3 * r
        return force



    