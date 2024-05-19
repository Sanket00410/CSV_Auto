def main():
    speed = input()
    print(f"{playback(speed)}")

def playback(to):
    return to.replace(" ","...")
main()