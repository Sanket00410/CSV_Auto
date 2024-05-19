def main():
    try:
        calory = input("Item:")
        print(f"Calorioes:{get_fruit(calory)}")
    except (TypeError, ValueError) as  e:
        print("Not Allowed",e) 
    
    
def get_fruit(n):

    
    nutrition ={
    "apple":130,
    "banana":110,
    "avocado":50,
    "cantaloupe":60,
    "grapefruit":90,
    "honeydew melon":50,
    "kwifruit":90,
    "lemon":15,
    "lime":20,
    "nectarine":60,
    "orange":80,
    "peach":60,
    "pear":100,
    "pineapple":50
    }
    for i in n:
        if i in n:
            return nutrition.get(n)
        
               
        
        
               
        
        

    

        
main()
