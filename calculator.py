# Home-Made Scientific Calculator

import math

def menu():
    print("=== Scientific Calculator ===")
    print("1. Velocity (v = d / t)")
    print("2. Kinetic Energy (Ec = 1/2 * m * v²)")
    print("3. Law of Universal Gravitation")
    print("4. Exit")

def velocity():
    d = float(input("Distance (m): "))
    t = float(input("Time (s): "))
    print("Velocity:", d / t, "m/s")

def kinetic_energy():
    m = float(input("Mass (kg): "))
    v = float(input("Velocity (m/s): "))
    ke = 0.5 * m * v**2
    print("Kinetic Energy:", ke, "J")

def gravity():
    G = 6.67430e-11  # Gravitational constant
    m1 = float(input("Mass 1 (kg): "))
    m2 = float(input("Mass 2 (kg): "))
    r = float(input("Distance (m): "))
    F = G * m1 * m2 / r**2
    print("Gravitational Force:", F, "N")

while True:
    menu()
    option = input("Choose an option: ")
    if option == "1":
        velocity()
    elif option == "2":
        kinetic_energy()
    elif option == "3":
        gravity()
    elif option == "4":
        print("Thanks for using <3")
        break
    else:
        print("Option not valid")
