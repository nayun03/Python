import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    # Get a list of primes from the interval [lo, hi)
    primes_lohi = _primes(lo, hi)

    # Sample two distinct random primes p and q from that list.
    start = primes_lohi[0]
    end = primes_lohi[len(primes_lohi)-1]

    p = primes_lohi[stdrandom.uniformInt(0, len(primes_lohi))]
    q = primes_lohi[stdrandom.uniformInt(0, len(primes_lohi))]
    while p == q:
        q = primes_lohi[stdrandom.uniformInt(0,len(primes_lohi))]

    # Set n and m to pq and (p − 1)(q − 1), respectively.
    n = p * q
    m = (p-1) * (q-1)

    # Get a list primes from the interval [2, m).
    primes_2m = _primes(2, m)

    # Choose a random prime e from the list such that e does not divide m using a loop.
    e = primes_2m[stdrandom.uniformInt(0, len(primes_2m))]
    while e % m == 0:
        e = primes_2m[stdrandom.uniformInt(0, len(primes_2m))]

    # Find a d ∈ [1,m)  such that ed mod m = 1 using a loop.
    for d in range(1, m):
        if (e * d) % m == 1:
            break

    # Return the tuple1 (n, e, d)
    return n, e, d

# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n,e):
    # Implement the function E(x) = x^e mod n.
    return (x ** e) % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    # Implement the function D(y) = y^d mod n.
    return (y ** d) % n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    # Create an empty list.
    primes = []

    # For each p ∈ [lo,hi), if p is a prime, add p to the list.
    for p in range(lo, hi):
        if p == 0 or p == 1 :
            continue

        i = 2
        while i <= p / i:
            if p % i == 0:
                break
            i += 1

        if i > p / i:
            primes += [p]

    return primes

# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    # Create a list b that is a copy (not an alias) of a.
    b = a[:]

    # Shuffle the first k elements of b.
    for i in range(k):
        value = stdrandom.uniformInt(0, k)
        temp = b[i]
        b[i] = b[value]
        b[value] = temp

    # Return a list containing the first k elements of b.
    return b[0:k]


# Returns a random item from the list a.
def _choice(a):
    # Get a random number r ∈ [0, l), where l is the number of elements in a.
    l = len(a)
    r = stdrandom.uniformInt(0, l)

    # Return the element in a at the index r.
    return a[r]



# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
