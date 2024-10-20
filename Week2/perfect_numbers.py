import stdio
import sys

# Accept n (int) as command-line argument
n = int(sys.argv[1])

# Repeating for each i ∈ [2, n], set total (sum of divisors of i) to 0.
for i in range(2, n+1) :
    total = 0

# Repeat for each j ∈ [1, i/2].
    for j in range(1, i//2+1):
        # If i mod j = 0, increment total by j.
        if i%j==0 :
            total+=j
    # If total = i, write i (perfect number).
    if total == i :
        stdio.writeln(i)

