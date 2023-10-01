chislo = input()
nch = ""
for i in chislo:
    if int(i) % 2 != 0:
        nch += i
print(nch)
