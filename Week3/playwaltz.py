import stdaudio
import stdio
import sys

# Read the waltz measures from standard input into a 1D list.
waltz = stdio.readAllInts()

# Handle the input errors described below.
# If the number of measures is not 32, exit with the message “A waltz must contain exactly 32 measures”.
# If a minuet measure is not from [1, 176], exit with the message “A minuet measure must be from [1, 176]”.
# If a trio measure is not from [1, 96], exit with the message “A trio measure must be from [1, 96]”.
if len(waltz) != 32:
    sys.exit('A waltz must contain exactly 32 measures')

for i in range(16):
    if waltz[i] not in range(1, 177):
        sys.exit('A minuet measure must be from [1, 176]')

for i in range(16,32):
    if waltz[i] not in range(1, 97):
        sys.exit('A trio measure must be from [1, 96]')

# Play each of the first 16 minuet measures by calling stdaudio.playFile(f), where f is the filename of the minuet (eg, if the
# measure is 123, then f = ’data/M123’).
for i in range(16):
    f = 'data/M' + str(waltz[i])
    stdaudio.playFile(f)

# Play each of the last 16 trio measures by calling stdaudio.playFile(f), where f is the filename of the trio (eg, if the measure
# is 57, then f = ’data/T57’)
for i in range(16, 32):
    f = 'data/T' + str(waltz[i])
    stdaudio.playFile(f)




