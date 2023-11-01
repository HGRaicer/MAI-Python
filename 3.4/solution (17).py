import itertools

line = input()
print("a b c f")
bin_list = itertools.product([0, 1], repeat=3)
for ans in bin_list:
    a, b, c = ans
    if eval(line) == 0:
        f = 0
    else:
        f = 1
    print(a, b, c, f)
