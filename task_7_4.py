# Урок 7_4
# for number in range (5, 10 + 1):
#     print(number ** 2)


# Возведение в квадрат чисел из диапазона
# beginNumber = int(input('Введите начальное число:'))  # Начало диапазона
# endNumber = int(input('Введите конечное число:'))  # Конец диапазона чисел
# for number in range (beginNumber, endNumber + 1):     # к последнему числу диапазона прибовляем единицу
#     print(number ** 2)
    
# Расчет калорий и времени сна

# wake_up = int(input('Время подьема:')) # wake up - проснуться
# awake_hours = 0  # awake hours - часы бодровствования
# calories_sum = 0 # сумма калорий за день
# for hour in range (wake_up, 23 ):
#     print('Сейчас' , hour , 'часов')
#     calories = int(input('Калорий потреблено за час:'))
#     calories_sum += calories
#     if calories_sum > 2000:
#         print('Максимальное количество калорий, пора спать')
#         break
#     awake_hours +=1
#     print('Часов бодровствования' , awake_hours)
#     print('Потреблено за это время колорий' , calories_sum)    

# вычисление суммы чисел от первого до второго

# first = int(input("Первое число: "))
# second = int(input("Второе число: "))
# numbers_sum = 0
# for i in range(first, second + 1):  # +1 чтобы захватить второе число включительно
#     numbers_sum += i
# print('Сумма чисел от', first, 'до', second, 'равна', numbers_sum)    

# Задача 3
wordUp = int(input('Рабочий день начался в :'))  # начало рабочего дня
wordTime = 0  # Рабочее время
sportTime = 0
for word in range(wordUp, 20):
    print('Сейчас ', word , 'часов')
    sports = int(input('Сколько минут разминка в час?'))
    sportTime +=sports
    if sportTime > 45:
        print('Достигнуто максимальное количество активности')
        break
    wordTime +=1
    print('Рабочее время ', wordTime)
    print('Cпортивное время' , sportTime)
