name1 = int(input())
name2 = int(input())
name3 = int(input())
sum = name1 * 60 + name2 + name3
h = (sum // 60) % 24
t = sum % 60

print(f"{h:02d}:{t:02d}")
