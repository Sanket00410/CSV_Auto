import sys
import random
from pyfiglet import Figlet

def main():
    if len(sys.argv) == 1 or (len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']):
        font_name = None

        if len(sys.argv) == 3:
            font_name = sys.argv[2]

        text = input("Enter text: ")
        print_output(text, font_name)
    else:
        print("Invalid command-line arguments. Usage: figlet.py [-f/--font FONT_NAME]")

def print_output(text, font_name):
    figlet = Figlet(font=font_name) if font_name else Figlet(font=random.choice(Figlet().getFonts()))
    output_text = figlet.renderText(text)
    print(output_text)

if __name__ == "__main__":
    main()
