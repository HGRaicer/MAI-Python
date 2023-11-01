import itertools

swords = input().split()
swords = [sword + " " for sword in swords]
for val in itertools.accumulate(swords):
    print(val[:-1])
