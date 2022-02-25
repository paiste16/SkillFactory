per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму Вашего вклада:")
values = list(per_cent.values())
deposit = list(map(lambda x: x*(int(money)/100), values))
print(deposit)
deposit_i = max(deposit)
print("Максимальная сумма, которую вы можете заработать —", deposit_i)