import stdio
import sys

# Accept n (int) as command-line argument
n = int(sys.argv[1])

# Use four nested while loops, with the bounds on the loop variables
a = 1
while a <= n:
    if a*a*a > n:
        break
    b = a
    while b <= n:
        if a*a*a + b*b*b > n:
            break

        c = a+1
        while c <= n:
            if c*c*c > a*a*a + b*b*b:
                break

            d = c
            while d <= n:
                if c*c*c + d*d*d > a*a*a + b*b*b:
                    break

                # Inside the innermost loop, if a^3 + b^3 = c^3 + d^3, write the desired output
                if c*c*c + d*d*d == a*a*a + b*b*b :
                    stdio.write(str(a*a*a + b*b*b) + ' = ')
                    stdio.write(str(a) + '^3 + ' + str(b) + '^3 = ')
                    stdio.write(str(c) + '^3 + ' + str(d) + '^3')
                    stdio.writeln()
                d += 1
            c += 1
        b += 1
    a += 1