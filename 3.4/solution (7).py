import itertools

N = int(input())
names = [input() for _ in range(N)]
mcount = int(input())

for idx in range(mcount):
    print(names[idx % N])
