import stdio
import sys

# Accept three integers x, y, and z as command-line arguments
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Find the smallest value α and largest value ω using min() and max() functions
α = min(x,y,z)
ω = max(x,y,z)

# Find the middle value as an arithmetic combination of x, y, z, α, and ω
mid = x+y+z - (α+ω)

# Write the numbers in ascending order, separated by a space
stdio.writeln(str(α)+' '+str(mid)+' '+str(ω))
