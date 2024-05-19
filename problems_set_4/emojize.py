import emoji
import sys


def main():
    # emo = input(("Input:"))
    # face(emo)
    sysargv()

def sysargv():
    if len(sys.argv)>0:
        print(emoji.emojize(sys.argv[1],language="alias"))
    else:
        None

# def face(n):
#     print((f"{emoji.emojize(n, language='alias')}"))

   
if __name__ == "__main__":
    main()

