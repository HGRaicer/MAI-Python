N = int(input())
porridge = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

for i in range(N):
    print(porridge[i % 5])
