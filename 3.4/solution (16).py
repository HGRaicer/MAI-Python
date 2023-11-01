import itertools

name_suits = ["буби", "пики", "трефы", "черви"]
suits = ["бубен", "пик", "треф", "червей"]
suit = input()
values = [
    "10",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "валет",
    "дама",
    "король",
    "туз",
]
val = input()
new_suit = suits[name_suits.index(suit)]
values.remove(val)
line = input().replace(",", "").split(" ")
line = " ".join(line)
prod = itertools.permutations(itertools.product(values, suits), 3)
line_prod = sorted(set([", ".join(" ".join(j) for j in sorted(i)) for i in prod]))
new_prod = (idx.replace(",", "") for idx in line_prod if new_suit in idx)
flag_ans = False
for ans in new_prod:
    if ans == line:
        ans_line = next(new_prod)
        ans_line = ans_line.replace("пик", "пик,")
        ans_line = ans_line.replace("треф", "треф,")
        ans_line = ans_line.replace("червей", "червей,")
        ans_line = ans_line.replace("бубен", "бубен,")
        print(ans_line[:-1])
        break
