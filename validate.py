import re
email = input("email: ")

# if re.search(r"^.+@.+\.edu$", email):
#     print("valid")
# else:
#     print("invalid")

match = re.search("^[\w. -]+@[\w. -]+$",email,re.IGNORECASE)  #"^[\w. -]+@[\w. -]+\.(com|gov|org|net)$"
                                                              #re.IGNORECASE, re.MULTILINE, re.DOTALL  
if match:
    print(match.group())
else:
    print("invalid")    