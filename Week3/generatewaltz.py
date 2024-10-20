import stdarray
import stdrandom
import stdio

# Read the minuet measures from standard input into a 2D list with dimensions 11 × 16.
minuet = stdarray.create2D(11, 16)
for i in range(11):
    for j in range(16):
        minuet[i][j] = stdio.readInt()

# Read the trio measures from standard input into a 2D list with dimensions 6 × 16.
trio = stdarray.create2D(6,16)
for i in range(6):
    for j in range(16):
        trio[i][j] = stdio.readInt()

# Write to standard output a random sequence of 16 minuet measures, each of which is a value from the minuet table
# —the column index j is a value from [0, 15] and the row index i ∈ [0, 10] is obtained from the sum of two die rolls.
for j in range(16):
    m = stdrandom.uniformInt(1, 6)
    n = stdrandom.uniformInt(1, 6)
    i = m+n
    stdio.write(str(minuet[i][j]) + ' ')

# Write to standard output a random sequence of 16 trio measures, each of which is a value from the trio table
# — the column index j is a value from [0, 15] and the row index i ∈ [0, 5] is obtained from a die roll.
for j in range(16):
    i = stdrandom.uniformInt(0, 6)
    if j == 15:
        stdio.writeln(str(trio[i][j]))
    else:
        stdio.write(str(trio[i][j]) + ' ')