
# i =0
# while i <3:
#     print("meow")
#     i+=1
# print("=====================")
# for i in range(3):
#     print("meow")
# print("=====================")

# print("mewo\n"*3,end="")

def main():
    num =get_num()
    meow(num)



def get_num():
    while True:
        n = int(input("What's numbers? "))
        try:
            if n > 0:
                return n
        except Exception as e:
            print("InValid Value...Please enter +VE number",e)
    
def meow(n):
    for _ in range(n):
        print("meow")
main()