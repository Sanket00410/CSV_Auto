def main():
    Que = input("What's your answer to the Great Question of Life, the Universe and Everything? ")
    deep(Que)
def deep(Que):
    match Que :
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case "forty_two":
            print("Yes")
        case _:
            print("No")
main()