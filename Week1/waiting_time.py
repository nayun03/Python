import math
import stdio
import sys

# Accept two floats lambda and t as command-line arguments
lambd = float(sys.argv[1])
t = float(sys.argv[2])

# Compute and write the value of p
# Use math.exp(x) for e^x
p = math.exp(-lambd*t)

stdio.writeln(p)
