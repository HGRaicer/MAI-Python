chislo = int(input())
prime = []
for i in range(2, chislo):
    if chislo % i == 0:
        while chislo % i == 0:
            prime.append(i)
            chislo //= i
strr = ""
for i in prime:
    strr += str(i) + " * "
print(strr[:-3])
