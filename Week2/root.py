import stdio
import sys

# Accept k (int), c (float), epsilon (float) as command-line arguments.
k = int(sys.argv[1])
c = float(sys.argv[2])
epsilon = float(sys.argv[3])

# Set t (our guess) to c.
t=c

# Repeating as long as |1 − c/t^k| > ϵ, replace t by t − f(t)/f′(t), where f(t) = t^k − c and f′(t) = kt^(k−1).
while abs(1 - c / (t ** k)) > epsilon:
    t = t-(t**k - c) / (k * t**(k - 1))


# Write to standard output the kth root of c, up to epsilon decimal places.
stdio.writeln(t)