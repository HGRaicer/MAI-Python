import itertools

f_swords = input().split(", ")
s_swords = input().split(", ")
t_swords = input().split(", ")

values = itertools.chain(f_swords, s_swords, t_swords)

for index, swrd in enumerate(sorted(values), 1):
    print(f"{index}. {swrd}")
