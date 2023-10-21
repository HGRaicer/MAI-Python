names = dict()
N = int(input())

for i in range(N):
    name = input()
    try:
        names[name] += 1
    except KeyError:
        names[name] = 1

count = 0
for i in names:
    if names[i] > 1:
        count += names[i]

print(count)
