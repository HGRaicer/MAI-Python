import itertools

N = int(input())
names = [input() for _ in range(N)]
for f_name, s_name in itertools.combinations(names, 2):
    print(f"{f_name} - {s_name}")
