The following provides full instructions to reproduce every figure submitted as part of the final project for the CMSC6950 course on the implementation of Python to analyze varitations in crustal thickness throughout the Orphan Basin, offshore Newfoundland. 

##2D Crustal Thickness Surface##

To reproduce the 2D crustal thickness surface in section 3.1 of the project report, the Python libraries Numpy, Matplotlib and SciPy must be installed on your system. If they are not installed, use "pip install numpy", "pip install scipy", and "python -m pip install -U matplotlib" in a terminal window. 

The next step is to download the XYZ dataset "Crustal_Thickness_CMSC6950.txt" and Python script "2D_Surface.py" from the GitHub Repository https://github.com/Nickson1593/CMSC6950_Project.git. Ensure that both of these files are saved in the same directory on your system.

Next, open a terminal window and navigate to the directory that contains the previously saved files using "cd project/path" where "project/path" is the location of the files. To reproduce the figure, run the line "python 2D_Surface.py" from the terminal. Note: The figure can also be reproduced in a Jupyter Notebook by ensuring the files are saved in the same location as the Notebook and the line "%load 2D_Surface.py" in a new cell and running the cell. 

Although the line of code to save the figure as a pdf is not included in any of the Python scripts, the figure can be saved as a pdf by adding the line plt.savefig("name_of_file.pdf") to the script, above plt.show().

##3D Crustal Thickness Surface##

To reproduce the 3D crustal thickness surface in section 3.2 of the project report, the Python libraries Numpy, Matplotlib, Plotly and SciPy must be installed on your system. If they are not installed, use "pip install numpy", "pip install scipy", "pip install plotly" and "python -m pip install -U matplotlib" in a terminal window. Depending on the program used to visualize the 3D Surface, the Kaleido Python library is required to view the 3D visualization using Plotly. To install Kaleido on your system, run "pip install kaleido --upgrade" from a terminal window or "%pip install kaleido --upgrade" in a new cell in a Jupyter Notebook. 

The next step is to download the XYZ dataset "Crustal_Thickness_CMSC6950.txt" and Python script "3D_Crustal_Thickness_Surface.py" from the GitHub Repository https://github.com/Nickson1593/CMSC6950_Project.git. Ensure that both of these files are saved in the same directory on your system.

Next, open a terminal window and navigate to the directory that contains the previously saved files using "cd project/path" where "project/path" is the location of the files. To reproduce the figure, run the line "python 3D_Crustal_Thickness_Surface.py" from the terminal. Note: The figure can also be reproduced in a Jupyter Notebook by ensuring the files are saved in the same location as the Notebook and the line "%load 3D_Crustal_Thickness_Surface.py" in a new cell and running the cell. 

Although the line of code to save the figure as a pdf is not included in any of the Python scripts, the figure can be saved as a pdf by adding the line fig.write_image("name_of_file.pdf") to the script, above fig.show().

##3D Crustal Thickness Surface with Boundary##

To reproduce the 3D crustal thickness surface with the boundary constraint in section 3.3 of the project report, the Python libraries Numpy, Matplotlib, Plotly, SciPy, and Pandas must be installed on your system. If they are not installed, use "pip install numpy", "pip install scipy", "pip install plotly", "python -m pip install -U matplotlib", and "pip install pandas" in a terminal window. Depending on the program used to visualize the 3D Surface, the Kaleido Python library is required to view the 3D visualization using Plotly. To install Kaleido on your system, run "pip install kaleido --upgrade" from a terminal window or "pip install -U kaleido" in a new cell in a Jupyter Notebook. 

The next step is to download the XYZ datasets "Crustal_Thickness_CMSC6950.txt", "basement_boundary_points.txt", and "Crustal_Thickness_With_Boundary_XYZ.txt", and Python script "3D_Crustal_Thickness_With_Boundary.py" from the GitHub Repository https://github.com/Nickson1593/CMSC6950_Project.git. Ensure that all of these files are saved in the same directory on your system.

Next, open a terminal window and navigate to the directory that contains the previously saved files using "cd project/path" where "project/path" is the location of the files. To reproduce the figure, run the line "python 3D_Crustal_Thickness_With_Boundary.py" from the terminal. Note: The figure can also be reproduced in a Jupyter Notebook by ensuring the files are saved in the same location as the Notebook and the line "%load 3D_Crustal_Thickness_With_Boundary.py" in a new cell and running the cell. 

Although the line of code to save the figure as a pdf is not included in any of the Python scripts, the figure can be saved as a pdf by adding the line fig.write_image("name_of_file.pdf") to the script, above fig.show(). 

##2D Crustal Thickness Surface##

To reproduce the 2D crustal thickness surface in section 3.1 of the project report, the Python libraries Numpy, Matplotlib and SciPy must be installed on your system. If they are not installed, use "pip install numpy", "pip install scipy", and "python -m pip install -U matplotlib" in a terminal window. 

The next step is to download the XYZ dataset "Crustal_Thickness_CMSC6950.txt" and Python script "2D_Surface.py" from the GitHub Repository https://github.com/Nickson1593/CMSC6950_Project.git. Ensure that both of these files are saved in the same directory on your system.

Next, open a terminal window and navigate to the directory that contains the previously saved files using "cd project/path" where "project/path" is the location of the files. To reproduce the figure, run the line "python 2D_Surface.py" from the terminal. Note: The figure can also be reproduced in a Jupyter Notebook by ensuring the files are saved in the same location as the Notebook and the line "%load 2D_Surface.py" in a new cell and running the cell. 

Although the line of code to save the figure as a pdf is not included in any of the Python scripts, the figure can be saved as a pdf by adding the line plt.savefig("name_of_file.pdf") to the script, above plt.show()



