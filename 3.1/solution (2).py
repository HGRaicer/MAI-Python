L = int(input())
N = int(input())
for _ in range(N):
    strr = input()
    if len(strr) > L:
        print(f"{strr[:L-3]}...")
    else:
        print(strr)
