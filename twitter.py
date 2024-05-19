import re

url = input("url: ")

# username = re.sub(r"(https?://)?(www\.)?twitter\.(com|in)/","",url)
if matches := re.search(r"^https?://(?:www\.)?twitter\.(.+)/(.+)$",url):
    if matches.group(1) == "com":
        print(matches.group(2))
