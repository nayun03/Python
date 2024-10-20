import stdio
import sys

# Accept two floats t and v as command-line arguments
t = float(sys.argv[1])
v = float(sys.argv[2])

# Compute and write the value of wind chill w
# Use ** for exponentiation, ie, use x ** y for x^y
w = 35.74 + 0.6215*t + (0.4275*t-35.75)*v**0.16

stdio.writeln(w)
