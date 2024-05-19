# name = input("what's your name? ").strip().title()
# #name = name.strip().title() # remove any spaces and capatilize that user gave in input
# #first, last = name.split(" ") # splits user input into first and last
# print (f"hello, {name}")
def main():
    hello()
    name =input("what's your name? ").strip().title()
    hello(name)


def hello(to="world"):
    print ("hello", to)

main()