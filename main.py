from body import Body
from world import World

import numpy as np

def main():
    """Main function that initializes the bodies and calculates the simulation data"""


    border_yes_or_no = input("Would you like to implement a border? (yes/no): ")


  
    size_ = float(input("Enter the size of the world: "))
    dt_ = float(input("Enter the time step: "))
    time_steps = int(input("Enter the number of time steps: "))
    body_count = int(input("Enter the number of bodies: "))

    # Initialize the world
    world = World(size = size_, dt = dt_ )

    random_or_not = input("Would you like to use predefinded intervalls(type 1) for the values or define them yourself(type 2): ")
    if random_or_not == "1":
        for i in range(body_count):
            mass1 = np.random.uniform(100000, 200000)
            position1 = np.array([np.random.uniform(-world.size, world.size), np.random.uniform(-world.size, world.size), np.random.uniform(-world.size, world.size)])
            velocity1 = np.array([np.random.uniform(-2, 2), np.random.uniform(-2, 2), np.random.uniform(-2, 2)])
            acceleration1 = np.array([np.random.uniform(-2, 2), np.random.uniform(-2, 2), np.random.uniform(-2, 2)])
            force = np.array([0, 0, 0])
            world.bodies.append(Body(mass=mass1, position=position1, velocity=velocity1, acceleration=acceleration1))

    


        
        #main loop which calculates the data for each time step
        for i in range(time_steps):
            for body in world.bodies:
                force = np.array([0, 0, 0])
                for other_body in world.bodies:
                    if other_body != body:
                        force += body.calculate_force(other_body)
                body.update_acceleration(force)
                body.update_velocity(world.dt)
                body.update_position(world.dt)
            world.record_simulation_step(i)

    world.save_to_json("simulation_data.json")
    print("Simulation data saved to simulation_data.json")
    return world.size
            
            


if __name__ == "__main__":
    main()
