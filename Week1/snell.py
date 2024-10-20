import math
import stdio
import sys

# Accept three floats θ1, n1, and n2 as command-line arguments
theta1_deg = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

# Compute and write the value of the angle of refraction θ2 in degrees
# Use math.radians() and math.degrees() to convert degrees to radians and vice versa
# To calculate the arcsine of a number, use math.asin()
theta1_rad = math.radians(theta1_deg)
sin_theta2 = n1*math.sin(theta1_rad)/n2
theta2_rad = math.asin(sin_theta2)
theta2_deg = math.degrees(theta2_rad)

stdio.writeln(theta2_deg)