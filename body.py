import numpy as np

class Body:
    G = 6.67430e-11  # Gravitational constant

    def __init__(self, mass, position, velocity, acceleration):
        """
        Initializes the Body class with mass, position, velocity, and acceleration.
        
        Parameters:
        mass (float): Mass of the body
        position (list or np.array): Initial position of the body
        velocity (list or np.array): Initial velocity of the body
        acceleration (list or np.array): Initial acceleration of the body
        """
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.acceleration = np.array(acceleration)

    def update_acceleration(self, other):
        """
        Updates the acceleration of the body based on the gravitational force from another body.
        
        Parameters:
        other (Body): The other body to calculate the force with
        
        Returns:
        np.array: Updated acceleration
        """
        r = other.position - self.position
        r_norm = np.linalg.norm(r)
        if r_norm < 1:  # Prevents singularities
            r_norm = 1
        force = (self.G * self.mass * other.mass * r) / r_norm**3
        self.acceleration = force / self.mass
        return self.acceleration
    
    def update_velocity(self, dt, other):
        """
        Updates the velocity of the body.
        
        Parameters:
        dt (float): Time step
        other (Body): The other body to calculate the force with
        
        Returns:
        np.array: Updated velocity
        """
        new_acceleration = self.update_acceleration(other)
        self.velocity += 0.5 * (self.acceleration + new_acceleration) * dt
        return self.velocity

    def update_position(self, dt):
        """
        Updates the position of the body.
        
        Parameters:
        dt (float): Time step
        
        Returns:
        np.array: Updated position
        """
        self.position += self.velocity * dt + 0.5 * self.acceleration * dt**2
        return self.position
    
    def __str__(self):
        """
        Returns the relevant information about the body.
        
        Returns:
        str: String representation of the body's properties
        """
        return (
            f"mass: {self.mass}\n"
            f"position: {self.position}\n"
            f"velocity: {self.velocity}\n"
            f"acceleration: {self.acceleration}\n"
        )