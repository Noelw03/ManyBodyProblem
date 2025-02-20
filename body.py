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

    def update_acceleration(self, force):
        """
        Updates the acceleration of the body.
        
        Parameters:
        new_acceleration (np.array): New acceleration
        """
        self.acceleration = force / self.mass
        return self.acceleration
    
    def update_velocity(self, dt, force):
        """
        Updates the velocity of the body.
        
        Parameters:
        dt (float): Time step
        
        Returns:
        np.array: Updated velocity
        """
        new_acceleration = self.update_acceleration(force)
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
    
    def calculate_acceleration(self, other):
        """
        Calculates the gravitational force between two bodies.
        
        Parameters:
        other_body (Body): The other body to calculate the force with
        
        Returns:
        np.array: Gravitational force vector
        """
        r = other.position - self.position
        r_norm = np.linalg.norm(r)
        if r_norm < 1:  # Prevents singularities
            r_norm = 1
        force = (self.G * self.mass * other.mass * r) / r_norm**3
        new_acceleration = force / self.mass
        return new_acceleration
    
    def update_acceleration(self, other):
        """
        Updates the acceleration of the body.
        
        Parameters:
        force (np.array): Force acting on the body
        
        Returns:
        np.array: Updated acceleration
        """
        self.acceleration = self.calculate_acceleration(other)

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