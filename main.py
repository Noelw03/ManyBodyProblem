from body import Body
from world import World

import numpy as np

def main():
    """Main function that initializes the bodies and calculates the simulation data"""

    # Initialize the world
    world = World(size = None, dt = None, bodies = [], )

    border_yes_or_no = input("Would you like to implement a border? (yes/no): ")
    if border_yes_or_no == "yes":
        world.size = float(input("Enter the size of the border: "))
        body_count = int(input("Enter the number of bodies: "))
        dt = float(input("Enter the time step: "))
        time_steps = int(input("Enter the number of time steps the simulation should last: "))


    elif border_yes_or_no == "no":
        world.size = None
        body_count = int(input("Enter the number of bodies: "))
        random_or_not = input("Would you like to use predefinded intervalls(type 1) for the values or define them yourself(type 2): ")
        if random_or_not == "1":
            n = 0
            for i in range(body_count):
                mass = np.random.uniform(1, 2)
                position = np.array(np.random.uniform(-world.size, world.size), np.random.uniform(-world.size, world.size), np.random.uniform(-world.size, world.size))
                velocity = np.array(np.random.uniform(1, 2), np.random.uniform(1, 2), np.random.uniform(1, 2))
                acceleration = np.array(np.random.uniform(1, 2), np.random.uniform(1, 2), np.random.uniform(1, 2))
                world.bodies.append(Body(mass, position, velocity, acceleration))
                body = body(mass, position, velocity, acceleration)
                world.bodies.append(body)

    

        elif random_or_not == "2":
        
        #main loop which calculates the data for each time step
        for n in range(time_steps):
            for 

            


    if __name__ == '__main__':
        main()
