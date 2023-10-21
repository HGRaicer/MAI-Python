N = int(input())
for _ in range(N):
    strr = input()
    try:
        print(strr.index("зайка") + 1)
    except ValueError:
        print("Заек нет =(")
