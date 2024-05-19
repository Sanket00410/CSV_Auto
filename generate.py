import random

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["king", "queen", "jack"]
random.shuffle(cards)
for card in cards:
    print(card)