def main():
    post = input("Input:")
    print(shorten(post))
def shorten(word):
    
        
    
    vowel="aeiouAEIOU"
    # translation_table = str.maketrans(' ', ' ', letters_to_remove)
    # for p in letters_to_remove:
        # post = post.replace(p,"")
        # output = post.translate(translation_table)
        
    return"".join([p for p in word if p not in vowel])
     
    
if __name__ =="__main__":       
    main()