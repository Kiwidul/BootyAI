"""
This script finds the circumference of a circle.
The imput is the radius of the circle.

The formula is:

C = 2*pi*r


Created by Mattis Stene-Johansen for the project BootyAI
"""


find_radius = raw_input("Radius? > ") #in BooyAI, the radius is found using computer vision

radius = find_radius

pi = 3.14159265359


def Find_circumference(radius, pi):
    circumference = 2 * float(pi) * float(radius)

    print "circumference: " + str(circumference)

print Find_circumference(radius, pi)


