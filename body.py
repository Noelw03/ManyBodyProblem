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
        force (np.array): Force acting on the body
        
        Returns:
        np.array: Updated acceleration
        """
        self.acceleration = force / self.mass
        return self.acceleration
    
    def update_velocity(self, dt):
        """
        Updates the velocity of the body.
        
        Parameters:
        dt (float): Time step
        
        Returns:
        np.array: Updated velocity
        """
        self.velocity += self.acceleration * dt
        return self.velocity

    def update_position(self, dt):
        """
        Updates the position of the body.
        
        Parameters:
        dt (float): Time step
        
        Returns:
        np.array: Updated position
        """
        self.position += self.velocity * dt
        return self.position
    
    def calculate_force(self, other_body):
        """
        Calculates the gravitational force between two bodies.
        
        Parameters:
        other_body (Body): The other body to calculate the force with
        
        Returns:
        np.array: Gravitational force vector
        """
        r = other_body.position - self.position
        r_norm = np.linalg.norm(r)
        if r_norm < 1:  # Prevents singularities
            r_norm = 1
        force = (self.G * self.mass * other_body.mass) / r_norm**3 * r
        return force

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