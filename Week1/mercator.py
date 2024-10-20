import math
import stdio
import sys

# Accept two floats φ and λ as command-line arguments
latitude = float(sys.argv[1])
longitude = float(sys.argv[2])

# Compute and write the values of x and y, separated by a space
x=longitude

# Use math.radians() to convert degrees to radians.
# Use math.log() for natural logarithm.
y=math.log((1+math.sin(math.radians(latitude)))/(1-math.sin(math.radians(latitude))))/2

stdio.writeln(str(x)+' '+str(y))
