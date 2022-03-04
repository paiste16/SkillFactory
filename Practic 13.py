tickets = int(input("Сколько билетов Вы хотите приобрести?"))
S = 0
n = 1
while n <= tickets:
    age = int(input(f"Введите возраст {n} гостя"))
    if age < 18:
        S += 0
    elif 18 <= age < 25:
        S += 990
    else:
        S += 1390
    n += 1
if tickets > 3:
    print("Сумма к оплате с учетом скидки 10%:", S * 0.9, "руб.")
else:
    print("Сумма к оплате:", S, "руб.")

