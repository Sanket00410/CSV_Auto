import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: bitcoin.py <number_of_bitcoins>")
        sys.exit(1)

    try:
        bitcoins_to_buy = float(sys.argv[1])
    except ValueError:
        print("Invalid input. Please provide a valid number of Bitcoins.")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    total_cost = bitcoins_to_buy * bitcoin_price

    # formatted_total_cost = "{:,.4f}".format(total_cost)  # Format the total cost with comma as a thousands separator

    print(f"The current cost of {bitcoins_to_buy:,.4f} Bitcoins is ${total_cost:,.4f} USD.")

if __name__ == "__main__":
    main()
