def main():
    file_name = input("File: ").lower()
    files(file_name)


def files(period):
        if period.endswith(".gif"):
            print("image/gif")
        elif period.endswith(".zip"):
            print("application/zip") 
        elif period.endswith(".jpg") or (".jpeg"):
            print("image/jpeg")
        else:
            print("application/octet-stream")


main()

# import requests

# link =requests.get("https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types")
# print(link)
