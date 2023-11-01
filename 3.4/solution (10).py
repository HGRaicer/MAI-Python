import itertools

N = int(input())
M = int(input())

answers = [f1 * s2 for f1, s2 in itertools.product([1], range(1, N * M + 1))]
for idx in range(len(answers)):
    if idx % M == 0 and idx != 0:
        print()
    print(f"{answers[idx]:>{len(str(N * M))}}", end=" ")
