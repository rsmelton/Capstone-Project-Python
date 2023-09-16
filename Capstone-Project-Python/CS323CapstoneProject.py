'''
Robert Scott Melton
CS323-001
Capstone Project
4/15/2023

This project made use out of the skills that we learned over
this semester. In this project I read over a file and grabbed each
line from the file to then process each line and grab the needed info
from each line to then store into a dictionary of shapes.
We then use this dictionary of shapes to create a dataframe.
After creating the dataframe we then can create a table with preferred
styling to show all the info about the shapes from the file.

If you would like to test the program with other shapes please follow similar format
in the shapes file that I have provided. Also the file name should be the same as the
file I provided: shapes.txt

Note that this program only handles the surface area and volumes for the following shapes:
    Box, Sphere, Cylinder, Torus

Each line in the file should be in the format: 
    ShapeName Shape Dimensions

Such as:
    Cube#1 box 1 1 1
    Donut#1 torus 1 1
    Cyl#1 cylinder 1 1
    LargeSphere sphere 100
'''

from tabulate import tabulate
import pandas as pd
import math

# Here are all of our classes for our shapes.

class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    def computeSurfaceArea(self):
        surfaceArea = (2 * self.length * self.width) + (2 * self.length * self.height) + (2 * self.height * self.width)
        return surfaceArea

    def computeVolume(self):
        volume = self.length * self.width * self.height
        return volume

class Sphere:
    def __init__(self, radius):
        self.radius = radius
    
    def computeSurfaceArea(self):
        surfaceArea = 4 * math.pi * (self.radius * self.radius)
        return surfaceArea

    def computeVolume(self):
        volume = 4.0/3.0 * math.pi * (self.radius * self.radius * self.radius)
        return volume
    
class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def computeSurfaceArea(self):
        surfaceArea = (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius * self.radius))
        return surfaceArea

    def computeVolume(self):
        volume = math.pi * (self.radius * self.radius) * self.height
        return volume
    
class Torus:
    def __init__(self, small_radius, big_radius):
        self.small_radius = small_radius
        self.big_radius = big_radius
    
    def computeSurfaceArea(self):
        surfaceArea = 4.0 * (math.pi * math.pi) * self.small_radius * self.big_radius
        return surfaceArea

    def computeVolume(self):
        volume = 2 * (math.pi * math.pi) * (self.small_radius * self.small_radius) * self.big_radius
        return volume


def processEachLineFromFile(linesFromFile):

    # So we create a new dictionary of shapes to hold all the information about them.
    shapes_dictionary = {'Name': [],
                         'Shape': [],
                         'Dimensions': [],
                         'Surface Area': [],
                         'Volume': []
                         }

    for line in linesFromFile:
        words = line.split()
        nameOfShape = words[0]
        shape = words[1]

        shapes_dictionary['Name'].append(nameOfShape)
        shapes_dictionary['Shape'].append(shape)

        # Checks to see what shape we found.
        if (shape == "box"):
            # find our Dimensions
            length = float(words[2])
            width = float(words[3])
            height = float(words[4])

            Dimensions = "Length: " + str(length) + ", Width: " + str(width) + ", Height: " + str(height) 
            shapes_dictionary["Dimensions"].append(Dimensions)

            # Creates a new instance of a Box.
            box = Box(length, width, height)

            # Compute the surface area and volume
            surfaceArea = box.computeSurfaceArea()
            surfaceArea = "{:.2f}".format(surfaceArea)
            shapes_dictionary['Surface Area'].append(surfaceArea)

            volume = box.computeVolume()
            volume = "{:.2f}".format(volume)
            shapes_dictionary['Volume'].append(volume)
        elif (shape == "sphere"):
            # find our Dimensions
            radius = float(words[2])

            Dimensions = "Radius: " + str(radius)
            shapes_dictionary["Dimensions"].append(Dimensions)

            # Creates a new instance of a Sphere.
            sphere = Sphere(radius)

            # Compute the surface area and volume
            surfaceArea = sphere.computeSurfaceArea()
            surfaceArea = "{:.2f}".format(surfaceArea)
            shapes_dictionary['Surface Area'].append(surfaceArea)

            volume = sphere.computeVolume()
            volume = "{:.2f}".format(volume)
            shapes_dictionary['Volume'].append(volume)
        elif (shape == "cylinder"):
            # find our Dimensions
            radius = float(words[2])
            height = float(words[3])

            Dimensions = "Radius: " + str(radius) + ", Height: " + str(height)
            shapes_dictionary["Dimensions"].append(Dimensions)

            # Creates a new instance of a Cylinder.
            cylinder = Cylinder(radius, height)

            # Compute the surface area and volume
            surfaceArea = cylinder.computeSurfaceArea()
            surfaceArea = "{:.2f}".format(surfaceArea)
            shapes_dictionary['Surface Area'].append(surfaceArea)

            volume = cylinder.computeVolume()
            volume = "{:.2f}".format(volume)
            shapes_dictionary['Volume'].append(volume)
        elif (shape == "torus"):
            # find our Dimensions
            small_radius = float(words[2])
            big_radius = float(words[3])

            Dimensions = "Small Radius: " + str(small_radius) + ", Big Radius: " + str(big_radius)
            shapes_dictionary["Dimensions"].append(Dimensions)

            # Creates a new instance of a Torus.
            torus = Torus(small_radius, big_radius)

            # Compute the surface area and volume
            surfaceArea = torus.computeSurfaceArea()
            surfaceArea = "{:.2f}".format(surfaceArea)
            shapes_dictionary['Surface Area'].append(surfaceArea)

            volume = torus.computeVolume()
            volume = "{:.2f}".format(volume)
            shapes_dictionary['Volume'].append(volume)

    return shapes_dictionary

# --- Start of program ---

# shapes.txt is a file with various shapes with their attributes such as
# Name of the shape, the shape itself, and the shapes Dimensions.
with open("shapes.txt", "r") as file:
    contents = file.read()

linesFromFile = contents.splitlines()

# Passing the lines from the file to our process function
# that will then process each line and find the shape with its
# name and Dimensions.
shapes_dictionary = processEachLineFromFile(linesFromFile)

# Now we create our shapes dataframe using the dictionary we got back.
shapes_dataframe = pd.DataFrame(shapes_dictionary)

# Convert the DataFrame to a list of lists
data = shapes_dataframe.values.tolist()

# Get the column headers
headers = shapes_dataframe.columns.tolist()

# Now we can create our shapes table with our preferred styling.
shapes_table = tabulate(data, headers=headers, tablefmt="grid", floatfmt=".2f", numalign="left")

print("\nBelow is my table of all the shapes with their names, dimensions, surface areas, and volumes.\n")
print(shapes_table)
print()