from body import Body
from world import World

import numpy as np

def main():
    """Main function that initializes the bodies and calculates the simulation data"""

    border_yes_or_no = input("Would you like to implement a border? (yes/no): ")
    size_ = input("Enter the size of the world (press 'Enter' for the standard size of 10^6): ")
    if size_ == "":
        size_ = 1e6
    else:
        size_ = float(size_)
    dt_ = input("Enter the time step (press 'Enter' for the recommended timestep of 0.1): ")
    if dt_ == "":
        dt_ = 0.1
    else:
        dt_ = float(dt_)
    time_steps = int(input("Enter the number of time steps: "))
    body_count = input("Enter the number of bodies (just press 'Enter' for the 3-body-problem): ")
    if body_count == "":
        body_count = 3
    else:
        body_count = int(body_count)

    # Initialize the world
    world = World(size = size_, dt = dt_)

    random_or_not = input("Would you like to use predefined intervals (type 1) for the values or define them yourself (type 2): ")
    if random_or_not == "1": # Predefined intervals
        for i in range(body_count):
            mass1 = 1e25
            position1 = np.array([np.random.uniform(-world.size/1.5, world.size/1.5), np.random.uniform(-world.size/1.5, world.size/1.5), np.random.uniform(-world.size/1.5, world.size/1.5)])
            velocity1 = np.zeros(3)
            acceleration1 = np.zeros(3)
            world.bodies.append(Body(mass=mass1, position=position1, velocity=velocity1, acceleration=acceleration1, force=np.zeros(3)))

    if random_or_not == "2": # User-defined intervals
        min_mass_range = float(input("Enter the min. mass of the bodies "))
        max_mass_range = float(input("Enter the max. mass of the bodies "))
        min_velocity_range = float(input("Enter the min. velocity of the bodies "))
        max_velocity_range = float(input("Enter the max. velocity of the bodies "))
        min_acceleration_range = float(input("Enter the min. acceleration of the bodies "))
        max_acceleration_range = float(input("Enter the max. acceleration of the bodies "))

        for i in range(body_count):
            mass1 = np.array([np.random.uniform(min_mass_range, max_mass_range), np.random.uniform(min_mass_range, max_mass_range), np.random.uniform(min_mass_range, max_mass_range)])
            position1 = np.array([np.random.uniform(-world.size/1.5, world.size/1.5), np.random.uniform(-world.size/1.5, world.size/1.5), np.random.uniform(-world.size/1.5, world.size/1.5)])
            velocity1 = np.array([np.random.uniform(min_velocity_range, max_velocity_range), np.random.uniform(min_velocity_range, max_velocity_range), np.random.uniform(min_velocity_range, max_velocity_range)])
            acceleration1 = np.array([np.random.uniform(min_acceleration_range, max_acceleration_range), np.random.uniform(-min_acceleration_range, max_acceleration_range), np.random.uniform(min_acceleration_range, max_acceleration_range)])
            world.bodies.append(Body(mass=mass1, position=position1, velocity=velocity1, acceleration=acceleration1, force=np.zeros(3)))

    for n in range(time_steps):  # Updates the simulation for every time step
        if border_yes_or_no == "yes":
            world.border(size = world.size)
        for i, body in enumerate(world.bodies):
            for j, other in enumerate(world.bodies):
                if i != j:  # Prevents the body from interacting with itself
                    body.update_force(other)
            body.update_acceleration(other)
            body.update_velocity(world.dt, other)
            body.update_position(world.dt)
            body.reset_force()
        world.record_simulation_step(n)

    world.save_to_json("simulation_data.json")
    print("Simulation data saved to simulation_data.json")
    return world.size

if __name__ == "__main__":
    main()