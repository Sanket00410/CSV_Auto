def main():
    number = get_int("what's X? ")
    print(f"number is {number}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()