set_ = set()
N = int(input())
M = int(input())

for _ in range(N + M):
    set_.add(input())
if len(set_) == N + M:
    print("Таких нет")
else:
    print(N + M - len(set_))
