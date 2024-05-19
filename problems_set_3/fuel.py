def main():
    
    x,y = get_fraction()
    r = cal(x,y)
    conditions(r)
    print(f"{r}%")

def conditions(n):
   
    if n >= 99:
        print("F")
    
    elif n<= 1 :
        print("E")
    
            
def cal(x,y):
    return round((x / y )* 100)

def get_fraction():
    while True:
        try:
            fraction = input("fraction: ")
            x,y = map(int,fraction.split("/"))
            return x,y

            
        except(ValueError,ZeroDivisionError)as e:
            print(f"Error is {e}")

            
        
            
main()