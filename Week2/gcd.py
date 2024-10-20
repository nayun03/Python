import stdio
import sys

# Accept p (int) and q (int) as command-line arguments
p = int(sys.argv[1])
q = int(sys.argv[2])

# Repeating as long as p mod q ̸= 0, exchange p and q with q and p mod q
while p%q !=0 :
    p, q = q, p % q

# Write to standard output the greatest common divisor (gcd) of p and q.
stdio.writeln(q)
