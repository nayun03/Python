import stdio
import sys

# Accept t (float), v (float) as command-line arguments.
t = float(sys.argv[1])
v = float(sys.argv[2])

# Use an if statement to decide when to report the error messages and when to compute and write the wind chill w.
if t > 50 and v <= 3 :
    stdio.writeln("Value of t must be <= 50 F")
    stdio.writeln("Value of v must be > 3 mph")
    # If v is less than 30, write the message "Value of v must be > 3 mph" to standard output
    # If t is larger than 50, write the message "Value of t must be <= 50 F" to standard output.

elif v <= 3:
    stdio.writeln("Value of v must be > 3 mph")
    # If v is less than 30, write the message "Value of v must be > 3 mph" to standard output

elif t > 50:
    stdio.writeln("Value of t must be <= 50 F")
    # If t is larger than 50, write the message "Value of t must be <= 50 F" to standard output.

else:
    # Compute and write the value of the wind chill
    # Use the formula w = 35.74+0.6215t+(0.4275t-35.75)v^0.16 for the value of w
    w = 35.74 + 0.6215*t + (0.4275*t-35.75)*(v**0.16)
    # Write w to standard output
    stdio.writeln(w)