def main():
    x = int(input("what's X? "))
    y = int(input("what's Y? "))

    print(f"{add(x,y):,}") # :, is used to add coma before three zeros

            # round() is used to round the value if user uses float value
    print(f"{division(x,y):.2f}") # .2f is used to print two values after point
    print(f"{square(x)}")
def add(x,y):
    return x +y 
def division(x,y):
    return x /y 
def square(n):
    return pow(n, 2)

main()