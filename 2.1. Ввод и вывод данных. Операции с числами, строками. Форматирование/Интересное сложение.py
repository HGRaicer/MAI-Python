name1 = int(input())
name2 = int(input())

d = 1
sum = 0
while name1 != 0:
    k1 = name1 % 10
    k2 = name2 % 10
    sum += (k1 + k2) % 10 * d
    name1 //= 10
    name2 //= 10
    d *= 10
print(sum)
