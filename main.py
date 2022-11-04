
number_of_tickets = int(input('Сколько билетов вам нужно?'))

age_less_than_18 = int(input('Сколько будет посетителей до 18 лет?'))
age_from_18_to_25 = int(input('Сколько будет посетителей от 18 до 25 лет?'))
age_from_25 = int(input('Сколько будет посетителей от 25 лет?'))

total_amount = 0

if number_of_tickets != age_less_than_18 + age_from_18_to_25 + age_from_25:

    print('Количество билетов не совпадает, введите данные заново')

else:

    if age_from_18_to_25 > 0:
        age_from_18_to_25 *= 990
        total_amount += age_from_18_to_25

    if age_from_25 > 0:
        age_from_25 *= 1390
        total_amount += age_from_25

    if number_of_tickets > 3:
        total_amount = total_amount - total_amount / 100 * 10

    print(total_amount)














































