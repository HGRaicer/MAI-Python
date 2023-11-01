import itertools

start, fin, it = map(float, input().split())
for value in itertools.count(start, it):
    if value > fin:
        break
    print(f"{value:.2f}")
