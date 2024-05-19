def main():
    user_input = get_user()
    
   
def get_user():
    show_menu()
    print("=================\n",end="")
    total = 0.00
    try:
        
        while True:
            
            x = input("Item: ").title()
            
            if x not in menu:
                print("Invalid item Please enrter item in listed menu")
                continue
            
            R =get_menu(x)
            total += R
            
            print(f"Total: {total:.2f}$")
    
    except EOFError:
        print("\n Order Placed")
    
    else:
        return x
menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
def show_menu():
    
    print("Menu")
    print("-------")
    for item , price in menu.items():
        print(f"{item}: {price:.2f}$")

def get_menu(item):
    
    if item in menu:
        capitalized_item = ' '.join(word.capitalize() for word in item.split())
        return menu.get(capitalized_item, None)
    else:
        return None
    
main()
