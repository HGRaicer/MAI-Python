numbers = [int(num) for num in input().split()]

ans = []

for num in numbers:
    binum = bin(num)[2:]
    lnum = len(binum)
    znum = str(binum).count("0")
    onum = str(binum).count("1")
    dinum = {
        "digits": lnum,
        "zeros": znum,
        "units": onum,
    }
    ans.append(dinum)
print("[")
ma = len(ans)
count = 0
for elem in ans:
    count += 1
    print(f"{'{':>4}")
    for key, val in elem.items():
        print(f"{'':>8}'{key}': {val},")
    if count == ma:
        print(f"{'}':>4}")
    else:
        print(f"{'}':>4},")
print("]")
