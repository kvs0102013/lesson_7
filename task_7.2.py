# for meters in 100,90,95,87,102:
#  if meters % 3 == 0:
#    print(meters, 'Подходит')
#  else:
#    print(meters, 'Не подходит')

# Задание 7.2

# for degree in 3, 7, 5, 6, 4:
#     print(degree ** 2, degree ** 3, degree ** 4)

# Задание 7.2.3

winners = 0
for ticket in 345, 19, 87, 1020, 421:
    if ticket % 5 == 0:
        print(ticket, '- Счастливый билет')
        winners += 1
print('Счастливых билетов ', winners)        
     