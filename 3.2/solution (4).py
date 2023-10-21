set_ = set()
N = int(input())
M = int(input())
count = 0
for _ in range(N + M):
    strr = input()
    if strr in set_:
        count += 1
    set_.add(strr)

if count == N and N == M:
    print("Таких нет")
else:
    print(len(set_) - count)
