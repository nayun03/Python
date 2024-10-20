import stdio
import sys

# Accept n (int) as command-line argument
n = int(sys.argv[1])

# Set a, b (the first two Fibonacci numbers) to 1, and i to 3.
a = 1
b = 1
i = 3

#Repeating as long as i ≤ n, exchange a and b with b and a + b
while i <= n:
    a, b = b, a+b

    # Increment i by 1.
    i += 1

# Write to standard output the nth number from the Fibonacci sequence
stdio.writeln(b)