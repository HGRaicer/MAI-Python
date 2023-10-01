n = int(input())
nama = ''
ma = 0
for _ in range(n):
    name = input()
    amount = input()
    s = 0
    for i in amount:
        s += int(i)
    if s >= ma:
        ma = s
        nama = name
print(nama)
