import itertools

N = int(input())
values = [val * val2 for val, val2 in itertools.product(range(1, N + 1), repeat=2)]
for idx in range(N ** 2):
    if (idx + 1) % N == 0 and idx != 0:
        print(values[idx])
    else:
        print(values[idx], end=' ')
