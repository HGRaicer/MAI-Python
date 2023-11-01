import itertools

N = int(input())
people = [input() for _ in range(N)]
for perm in itertools.permutations(sorted(people), 3):
    print(", ".join(perm))
