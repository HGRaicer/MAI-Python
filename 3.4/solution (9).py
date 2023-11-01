import itertools

N = int(input())
print("А Б В")
for f1, s2, t3 in itertools.product(range(1, N - 1), range(1, N - 1), range(1, N - 1)):
    if f1 + s2 + t3 == N:
        print(f1, s2, t3)
