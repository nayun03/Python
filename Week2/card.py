import stdio
import stdrandom

# Set rank to a random integer from [2, 14].
rank = stdrandom.uniformInt(2, 15)

# Use an if statement to set rankStr to a string corresponding to rank — the ranks are 2, 3, . . . , Jack, Queen, King, and Ace.
if rank == 11:
    setrank = "Jack"

elif rank == 12:
    setrank = "Queen"

elif rank == 13:
    setrank = "King"

elif rank == 14:
    setrank = "Ace"

else :
    setrank = str(rank)

# Set suit to a random integer from [1, 4].
suit = stdrandom.uniformInt(1,5)

# Use an if statement to set suitStr to a string corresponding to suit — the suits are Clubs, Diamonds, Hearts, and Spades.
if suit == 1 :
    setsuit = "Clubs"

elif suit == 2 :
    setsuit = "Diamonds"

elif suit == 3 :
    setsuit = "Hearts"

else:
    setsuit = "Spades"


# Write the desired output.
stdio.writeln(setrank+" of "+setsuit)