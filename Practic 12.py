per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму Вашего вклада:")
tkb = per_cent['ТКБ'] * (int(money)/100)
skb = per_cent['СКБ'] * (int(money)/100)
vtb = per_cent['ВТБ'] * (int(money)/100)
sber = per_cent['СБЕР'] * (int(money)/100)
deposit = [tkb, skb, vtb, sber]
print(deposit)
deposit_i = max(deposit)
print("Максимальная сумма, которую вы можете заработать —", deposit_i)
