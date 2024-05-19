# match  usees cases

name = input(" what's your name 1?")

match name:
    case  "dark" | "king" | "world":
        print("Space")
    case "knight":
        print("Earth")
    case _ :
        print("who?")
