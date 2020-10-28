#Game of Cards
import random
picked_card = random.randint(0,51)

if (picked_card % 13 == 0) or (picked_card % 13 == 10) or (picked_card % 13 == 11) or (picked_card % 13 == 12):
    if (picked_card % 13 == 0):
        ace = picked_card % 13

    if (picked_card % 13 == 10):
        jack = picked_card % 13

    if (picked_card % 13 == 11):
        queen = picked_card % 13

    if (picked_card % 13 == 12):
        king = picked_card % 13
else:
    print(f"The card picked is {picked_card % 13}")

if (picked_card // 13 == 0):
    print("The card is Clubs")

if (picked_card // 13 == 0):
    print("The card is Diamonds")

if (picked_card // 13 == 0):
    print("The card is Hearts")

if (picked_card // 13 == 0):
    print("The card is Spades")