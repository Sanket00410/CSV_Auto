import re

name = input("Name: ").strip()

if match := re.search(r"^(.+) (.+) (.+)$",name.title()):
    name = match.group(2) + " " + match.group(3) + " " + match.group(1)
print(f"hello, {name}")