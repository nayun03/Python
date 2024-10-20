import stdio
import sys

# Accept n (int) as command-line argument
n = int(sys.argv[1])

# Set dragon and nogard to the string “F”.
dragon = str('F')
nogard = str('F')

# Repeating for each i ∈ [1, n], exchange dragon and nogard with dragon “L” nogard and dragon “R” nogard.
for i in range(1, n+1):
    dragon, nogard = (dragon+'L'+nogard), (dragon+'R'+nogard)


# Write to standard output the instructions for drawing a dragon curve of order n
stdio.writeln(dragon)