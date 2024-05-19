def main():
    custmer = input("Greeting:").strip().lower()
    bank(custmer)
        
def bank(greet):
    if greet.startswith("hello"):
        print("$0")
    elif greet.startswith("h") or greet.startswith("hey"):
        print("$20")
    
    else:
        print("$100")

if __name__  == "__main__":
    main()
