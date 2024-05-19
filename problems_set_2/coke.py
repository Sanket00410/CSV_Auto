def main():
    amount =0
    get_amount(amount)
    
    def get_amount(amount):
    while amount < 50:
        try:
            n = int(input("Insert Coin:"))
            if n in [1,2,5,10,25]:
                amount +=n
                print(f"Amount Due:{50-amount}")
            else:
                print("Only 1,2,5,10,25 coins are accepted..")
        except ValueError:
            print("Invalid Amount..Please enter right amount")
    change_owe = amount -50
    print(f"Change owed:{change_owe}")
       
 
main() 
