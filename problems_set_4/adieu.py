import inflect

def main():
    names = []
    try:
        while True:
            name = input("Name:")
            names.append(name)
    except EOFError:
        pass

    print_adieu(names)

def print_adieu(names):
    p = inflect.engine()

    for i, name in enumerate(names):
        if i == 0:
            print(f"Adieu, adieu, to {name}")
        elif i == 1:
            print(f"Adieu, adieu, to {names[0]} and {name}")
        elif i == len(names) - 1:
            print(f"Adieu, adieu, to {', '.join(names[:-1])}, and {name}")
        else:
            print(f"Adieu, adieu, to {', '.join(names[:i])}, and {name}")

if __name__ == "__main__":
    main()
