"""
This script finds the diameter of a circle.
The imput is the radius of the circle.

The formula is:

D = 2*r


Created by Mattis Stene-Johansen for the project BootyAI
"""

find_radius = raw_input("Radius? > ") #in BooyAI, the radius is found using computer vision

radius = find_radius


def Find_Diameter(radius):
    diameter = int(radius) * 2

    print "Diameter: " + str(diameter)

print Find_Diameter(radius)

