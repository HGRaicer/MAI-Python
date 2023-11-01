import itertools

N = int(input())
foods = []
for _ in range(N):
    foods.extend(input().split(", "))
foods = sorted(foods)

for idx, food in enumerate(foods, 1):
    print(idx, food, sep=". ")
