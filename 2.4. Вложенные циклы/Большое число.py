n = int(input())
s = ''
for _ in range(n):
    amount = input()
    ma = "0"
    for i in range(len(amount)):
        if amount[i] > ma:
            ma = amount[i]
    s += ma
print(s)
