import sys

def main():
    try:
        file_name = sys.argv[1]
        if not file_name.endswith(".py"):
            sys.exit("Not a python file")
        print(f"{file(file_name)}")
    except IndexError:
        sys.exit("To few arguments")

def file(name):
    try:
        with open(name)as f:
            lines = f.readlines() 
        count = 0
        for line in lines:
            if line.startswith("#"):
                continue
            if line.strip():
                count += 1
        return count
    except FileNotFoundError:
        sys.exit("file not present")
        
if __name__ == "__main__":
    main()