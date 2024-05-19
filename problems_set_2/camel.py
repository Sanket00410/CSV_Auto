def main():
    name= input("Camelcase: ")
    print(case_letter(name))

def case_letter(n):
    snake_case = [n[0].lower()]
    for c in n[1:]:
        if c.isupper():
            snake_case.extend(["_",c.lower()])
        else:
            snake_case.append(c)
    return "".join(snake_case)
            
        
main()
