def main():
    print(get_tweet())
def get_tweet():
    
        try:
            post = input("Input:")
            letters_to_remove="aeiouAEIOU"
            # translation_table = str.maketrans(' ', ' ', letters_to_remove)
            # for p in letters_to_remove:
                # post = post.replace(p,"")
                # output = post.translate(translation_table)
                
            output ="".join([p for p in post if p not in letters_to_remove])
            return f"output:{output}"
        except Exception  as e:
            print("Not Accepted..",e)
if __name__ =="__main__":       
    main()