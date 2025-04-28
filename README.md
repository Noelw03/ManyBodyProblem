# ThreeBodyProblem
Little project in which I try to numerically visualize the three body problem with Python in a object oriented way.

To run the code, you have to install the librarys given in the "requirements.txt" file. 

The programe works by usind two classes: "World" and "Body" to calculate the simulation data in the main.py file and write it into the simulaton_data.json file. By running it wit python, it'll guide you through the process
To have a visualization of the data, just run the "visualisation.ipynb" jupyter notebook. It'll run the main.py file.

Note that if you don't use the recommended values in the prompts, your result can be quite dissapointing. 
Durations of >2000 timesteps can cause the simulation to take quite long to compute. The reason for this is probably the funcanimation library, since the calculation of the data itself gets done really quickly.

There's already a computed simulation given named "example_simulation.mp4".

Enjoy!


