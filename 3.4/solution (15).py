import itertools

name_suits = ["буби", "пики", "трефы", "черви"]
suits = ["бубен", "пик", "треф", "червей"]
suit = input()
values = ["10", "2", "3", "4", "5", "6", "7", "8", "9", "валет", "дама", "король", "туз"]
val = input()
new_suit = suits[name_suits.index(suit)]
values.remove(val)
count = 0
if new_suit == suits[0] or new_suit == suits[1]:
    for val, suit in (itertools.product(values, suits)):
        if val == values[0] and (suit == suits[0] or suit == suits[1]):
            pass
        else:
            print(f"{values[0]} {suits[0]}, {values[0]} {suits[1]}, {val} {suit}")
            count += 1
        if count == 10:
            break
else:
    for val in range(10):
        print(f"{values[0]} {suits[0]}, {values[0]} {suits[1]}, {values[val]} {new_suit}")
