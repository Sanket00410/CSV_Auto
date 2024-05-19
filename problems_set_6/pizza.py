from tabulate import tabulate
import csv
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("To few arguments")
    
    name = sys.argv[1]
    if not name.endswith(".csv"):
        sys.exit("Not a csv file")
    
    filename = pizza_file(name)
    headers = filename[0]
    rows = filename[1:]
    print(tabulate(rows, headers =headers , tablefmt="grid"))

def pizza_file(name):
    try:
        with open (name)as f:
            reader = csv.reader(f)
            return list(reader)
    except FileNotFoundError:
        sys.exit("File not present")
        
if __name__ == "__main__":
    main()