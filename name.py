import sys



# if len(sys.argv) < 2:
#     print("to few arguments")
# elif len(sys.argv) > 2 :
#     print("to many arguments")
# else:
#     print("hello, my name is",sys.argv[1])

# if len(sys.argv) < 2:
#     sys.exit("to few arguments")
# elif len(sys.argv) > 2 :
#     sys.exit("to many arguments")

# print("hello, my name is",sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("to few arguments")
for arg in sys.argv[1:]:
    print("hello, my name is",arg)

