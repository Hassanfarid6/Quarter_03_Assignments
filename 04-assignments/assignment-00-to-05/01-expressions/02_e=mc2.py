# Write a program that continually reads in mass from the user and then outputs the equivalent energy using
# Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2
# Enter kilos of mass: 100

# e = m * C^2...
# m = 100.0 kg
# C = 299792458 m/s
# 8.987551787368176e+18 joules of energy!



c = 299792458 # Constant Value Speed of Light in m/s

def mass_to_energy(mass):
    energy = mass *  (c** 2)
    return energy

def main():
    user_input = float(input("Enter the mass in kilograms: "))
    energy = mass_to_energy(user_input)
    print("The energy is:", energy, "Joules")
    



if __name__ == '__main__':
    main()