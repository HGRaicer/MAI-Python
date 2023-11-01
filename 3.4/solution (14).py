import itertools

N = int(input())
foods = []
for _ in range(N):
    foods.extend(input().split(", "))
for perm in itertools.permutations(sorted(foods), 3):
    print(" ".join(perm))
