N = int(input())
all_numbs = []
for _ in range(N):
    numb = int(input())
    all_numbs.append(numb)

poww = int(input())

for numb in all_numbs:
    print(pow(numb, poww))
