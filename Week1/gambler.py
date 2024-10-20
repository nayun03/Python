import stdio
import sys

# Accept integers n1,n2 and float p as command-line arguments
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])

# Compute and write the values of p1 and p2, separated by a space
q=1-p
p1 = (1-(p/q)**n2)/(1-(p/q)**(n1+n2))
p2 = (1-(q/p)**n1)/(1-(q/p)**(n1+n2))
stdio.writeln(str(p1)+' '+str(p2))
