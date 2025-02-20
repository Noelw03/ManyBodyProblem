import numpy as np


class Body:
    def __init__(self, mass, position, velocity, acceleration):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def update_acceleration(self, force):
        self.acceleration = force / self.mass
        return self.acceleration
    
    def update_velocity(self, dt):
        self.velocity += self.acceleration * dt
        return self.velocity

    def update_position(self, dt):
        self.position += self.velocity * dt
        return self.position
    
    def calculate_force(self, other_body,):
        G = 6.67430e-11
        r = other_body.position - self.position
        r_norm = np.linalg.norm(r)
        force = G * self.mass * other_body.mass / r_norm**3 * r
        return force



    