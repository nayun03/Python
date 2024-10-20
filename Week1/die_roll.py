import stdio
import stdrandom
import sys

# Accept an integer n as command-line argument
n = int(sys.argv[1])

# Use stdrandom.uniformInt() with suitable arguments to simulate a single roll of an n-sided die.
roll1 = stdrandom.uniformInt(1,n+1)
roll2 = stdrandom.uniformInt(1,n+1)

# Write the sum of the numbers rolled
stdio.writeln(roll1+roll2)