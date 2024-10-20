import stdio
import sys


# Entry point. [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writef('zeros = %d, ones = %d, total = %d\n', _zeros(s), _ones(s), len(s))


# Return the number of zeros in s.
def _zeros(s):
    # Base case: if s is the empty string, return 0.
    if len(s) == 0:
        return 0

    # Recursive step: if the first character in s is 0, return 1 + _zeros(rest of s). Otherwise,
    # return _zeros(rest of s).
    if s[0] == '0':
        s = s[1:]
        return 1 + _zeros(s)
    else :
        s = s[1:]
        return _zeros(s)

# Return the number of ones in s.
def _ones(s):
    # Base case: if s is the empty string, return 0.
    if len(s) == 0:
        return 0

    # Recursive step: if the first character in s is 1, return 1 + _ones(rest of s). Otherwise,
    # return _ones(rest of s).
    if s[0] == '1':
        s = s[1:]
        return 1 + _ones(s)
    else :
        s = s[1:]
        return _ones(s)


if __name__ == '__main__':
    main()
