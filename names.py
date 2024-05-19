# name = input("whats your name? ")

# # file = open ("names.txt","a")
# # file.write(f"{name}\n")
# # file.close()

# with open("names.txt","a") as f:
#     f.write(f"{name}\n")

# with open("names.txt","r")as f:
#     lines = f.readlines()
# for line in lines:
#     print("hello,",line.rstrip())

# names = []

# with open ("names.txt")as f:
#     for line in f:
#         names.append(line.rstrip().title())
        
# for name in sorted(names):
#     print(f"hello, {name}")

with open ("names.txt")as f:
    for line in sorted(f r,reverse= True):
        print(f"hello,",line.rstrip().title())

        