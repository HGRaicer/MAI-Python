name = input()
amount = int(input())
wt = int(input())
count = int(input())
print(
    f"Чек\n{name} - {wt}кг - {amount}руб/кг\nИтого: {amount*wt}руб\nВнесено: {count}руб\nСдача: {count-amount*wt}руб"
)
