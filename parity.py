def main():
    x = int(input("X ?"))
    if is_even(x):
        print(f"{x}is even")
    else:
        print(f"{x}is odd")

def is_even(n):
    #return True if n % 2 == 0 else False
    return n % 2 ==0
    

main()

