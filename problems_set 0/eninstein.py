def main():
    mass = input("Mass:")
    try:
        mass =float(mass)
        energy = equation(mass)
        print(f"Energy:{equation(mass)}")
    except ValueError:
        print("Value Error: Please enter valid number..")


def equation(mass):
    speed_of_light = 300000000
    energy = mass * pow(speed_of_light,2)
    return energy 

main()


