
def main():
    
    user = get_str()
    display_list(user)
def get_str():
    
    grocery_items ={}
    
    try:
        
        while True:
            x = input("")
            grocery_items[x]=grocery_items.get(x,0)+1
    
    except (EOFError,KeyError)as e:
        print(f"\n {e}")
    return grocery_items

def display_list(grocery_list):
    print("Grocery List:")
    print("-------------")

    for item, count in sorted(grocery_list.items(), key=lambda x: x[0].lower()):
        print(f"{count} {item.upper()}")
main()