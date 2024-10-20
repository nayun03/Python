import stdio
import sys

# Accept n (int) and k (int) as command-line arguments
n = int(sys.argv[1])
k = int(sys.argv[2])

# Set total to 0
total = 0

# Repeating for each i ∈ [1, n], Incrementing total by i^k
for i in range(1,n+1):
    total += i**k

# Write s to standard output the sum 1^k + 2^k + · · · + n^k
stdio.writeln(total)