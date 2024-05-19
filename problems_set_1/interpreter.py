def main():
    number = input("Expression: ").split()
    x,y,z=number
    R=maths(x,y,z)
    if R is not None:
        print(f"{R:.1f}")
    

def maths(x,y,z):
    x=float(x)
    z=float(z)
    if y == "+":
        return x +z
    elif y == "*":
        return x * z
    elif y == "/":
        if z != 0:
            return x / z
        else:
            return None
    else:
        print("InValid Value")



    
    


main()