import itertools

suits = ["пик", "треф", "бубен", "червей"]
suit = input()
suits.remove(suit)

values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

for idx, val in itertools.product(values, suits):
    print(idx, val)
