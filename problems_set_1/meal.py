def main():

    reminder= input("what time is it? ")
    T=convert(reminder)
    R=time(T)
    print(R)
    
def convert(C):
    h, m=C.split(":")
    return h,m
    
def time(T):

    b_start=convert("7:00") 
    b_end=convert("8:00") 
    
    l_start=convert("12:00") 
    l_end=convert("13:00") 
    
    d_start=convert("19:00") 
    d_end=convert("20:00") 
    
    if b_start<= T <= b_end :
        return"breakfast time"
    elif l_start<= T <= l_end:
        return"lunch time"
    elif d_start<= T <= d_end:
        return"dinner time"
    else:
        return None
        
        
    
    
main()