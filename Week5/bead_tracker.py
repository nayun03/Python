import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    # Accept command-line arguments pixels (int), tau (float), and delta (float).
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])

    # Construct a BlobFinder object for the frame sys.argv[4] and from it get a list of beads prevBeads that have at least pixels.
    prev_frame = Picture(sys.argv[4])
    blob_finder = BlobFinder(prev_frame, tau)
    prev_beads = blob_finder.getBeads(pixels)

    # For each frame starting at sys.argv[5]:
    for i in range(5, len(sys.argv)):
        # Construct a BlobFinder object for the current frame and get a list of beads currBeads that have at least pixels.
        curr_frame = Picture(sys.argv[i])
        blob_finder = BlobFinder(curr_frame, tau)
        curr_beads = blob_finder.getBeads(pixels)

        # For each bead currBead in currBeads:
        for curr_bead in curr_beads:
            min_distance = math.inf

            # Find the closest bead in prevBeads that is no further than delta from currBead.
            for prev_bead in prev_beads:
                distance = prev_bead.distanceTo(curr_bead)
                if distance <= delta and distance < min_distance:
                    min_distance = distance

            # If a closest bead is found, write its distance to currBead.
            if min_distance != math.inf:
                stdio.write('%.4f\n' % min_distance)
            else:
                stdio.writeln()  # Write a newline character.

        stdio.writeln()

        # Set prevBeads to currBeads for the next iteration.
        prev_beads = curr_beads

if __name__ == '__main__':
    main()
