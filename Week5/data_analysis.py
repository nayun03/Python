import math
import stdio


# Entry point.
def main():
    # Initialize ETA, RHO, T, and R to appropriate values.
    ETA = 9.135e-4  # Viscosity of water in Ns/m^2
    RHO = 0.5e-6  # Radius of bead in meters
    T = 297  # Absolute temperature in Kelvin
    R = 8.31457  # Universal gas constant in J/K/mol

    # Calculate var as the sum of the squares of the n displacements (each converted from pixels to meters) read from standard
    # input.
    var = 0.0
    n = 0
    METERS_PER_PIXEL = 0.175e-6
    for x in stdio.readAllFloats():
        var += (METERS_PER_PIXEL * x) ** 2
        n += 1

    # Divide var by 2 * n.
    var /= (2 * n)
    # Estimate Boltzmann’s constant as 6 * math.pi * var * ETA * RHO / T.
    boltzmann_constant = 6 * math.pi * var * ETA * RHO / T
    #  Estimate Avogadro’s constant as R / k.
    avogadro_constant = R / boltzmann_constant
    #  Write to standard output the two constants in scientific notation (using the format string ’%e’) and separated by a
    # space.
    stdio.writeln("%e %e" %(boltzmann_constant, avogadro_constant))


if __name__ == '__main__':
    main()
