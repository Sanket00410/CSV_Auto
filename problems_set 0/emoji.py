def main():
    x =input().strip()
    Y = convert(x)
    print(f"{Y}")

def convert(input_str):
    input_str = input_str.replace(":)", "🙂")
    input_str = input_str.replace(":(", "🙁")
    return input_str

main()

