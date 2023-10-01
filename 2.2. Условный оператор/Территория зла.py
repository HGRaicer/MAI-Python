a = int(input())
b = int(input())
c = int(input())

k = [a, b, c]
k.sort()
if ((k[-3] ** 2) + (k[-2] ** 2)) > (k[-1] ** 2):
    print("крайне мала")
elif ((k[-3] ** 2) + (k[-2] ** 2)) < (k[-1] ** 2):
    print("велика")
else:
    print("100%")
