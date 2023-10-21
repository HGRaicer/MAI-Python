count_dict = {}

while True:
    line = input()
    if line == "":
        break
    words = line.split()
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

for key, value in count_dict.items():
    print(f"{key} {value}")
