set_ = set()
N = int(input())

for _ in range(N):
    l1 = input().split(" ")
    for elem in l1:
        set_.add(elem)
for elem in set_:
    print(elem)
