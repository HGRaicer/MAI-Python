import itertools

f_name = input().replace(",", "").split()
s_name = input().replace(",", "").split()
for first, second in zip(f_name, s_name):
    print(f"{first} - {second}")
