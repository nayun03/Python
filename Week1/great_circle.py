import math
import stdio
import sys

# Accept four floats x1, y1, x2, and y2 as command-line arguments
x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

# Compute and write the value of great-circle distance d
# Use math.radians() to convert degrees to radians
# To calculate the arccosine of a number, use math.acos()
x1_rad = math.radians(x1)
y1_rad = math.radians(y1)
x2_rad = math.radians(x2)
y2_rad = math.radians(y2)
d = 6359.83*math.acos(math.sin(x1_rad) * math.sin(x2_rad) + math.cos(x1_rad) * math.cos(x2_rad) * math.cos(y1_rad - y2_rad))

stdio.writeln(d)


