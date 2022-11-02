


per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

amount = input('Введите сумму')

deposit = []

deposit.append(float(amount) / 100 * float(per_cent['ТКБ']))
deposit.append(float(amount) / 100 * float(per_cent['СКБ']))
deposit.append(float(amount) / 100 * float(per_cent['ВТБ']))
deposit.append(float(amount) / 100 * float(per_cent['СБЕР']))

max_value = max(deposit)

print(deposit)
print('Максимальная сумма, которую вы можете заработать -', max_value)














































