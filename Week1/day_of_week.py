import stdio
import sys


# Accept three integers m, d, and y as command-line arguments
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# Compute and write the value of day of the week dow
# Use // (floored division) for / and % for mod
y0 = y - (14 - m) // 12
x0 = y0 + y0 // 4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
dow = (d + x0 + 31 * m0 // 12) % 7

stdio.writeln(dow)