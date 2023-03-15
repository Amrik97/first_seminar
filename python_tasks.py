"Задание 1"
user_name = input("Введите ваше имя: ")
print(f"Привет, {user_name}")
user_second_name = input("Введите вашу фамилию: ")
print(f"Хмм, супер, {user_second_name}. Теперь вам нужно придумать пароль ")
user_password = input("Введите новый пароль: ")
print(f"Отлично, теперь не забудьте свои данные, ваш пароль для авторищации: {user_password}")
password = input('Введите пароль: ')
access = False
if password == user_password:
    print('Пароль принят, вы успешно авторизовались')
    access = True
if password != user_password:
    print('Пароль непринят, введите снова')


"Задание 2"
second_time = int(input("Пожалуйста, введите время в секундах: "))
hour_time = second_time / 3600
minute_time = second_time / 60
print(f"Вами указанные секунды в часах будут:, {hour_time}, в минутах будут:, {minute_time}, и в секундах: {second_time}")


"Задание 3"
number = int(input("Пожалуйста, введите целое положительное цисло: "))
print(number,(number+number),(number+number+number))


"Задание 4"
corp_income = int(input("Введите выручку фирмы: "))
corp_expenditure = int(input("Введите издержки фирмы: "))
result_corp = corp_income - corp_expenditure
print(f"Доходность фирмы составляет: {result_corp}")



"""ДОПОЛНИТЕЛЬНЫЕ:
Задача 2: Найдите сумму цифр трехзначного числа."""

sum_number = int(input("Введите первое число: "))
sum_number_two = int(input("Введите второе число: "))
sum_number_three = int(input("Введите второе число: "))
sum_result = sum_number + sum_number_two + sum_number_three
print(f"Сумма цифр трехзначного числа: {sum_result} ({sum_number}, {sum_number_two},  {sum_number_three}) ")


"""Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал
каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза
больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10"""

peter = int(input("Подскажите, сколько журавликов сделал Петя? "))
sergey = int(input("А теперь, подскажите, сколько журавликов сделал Сережа? "))
kate_result = (peter + sergey) * 2
full_result = (peter + sergey+kate_result)
print(f" Катя сделала: {kate_result} журавликов, Петя сделал: {peter} журавликов, Сережа сделал:{sergey}")
print(f"{full_result},->({kate_result} {peter} {sergey})")



"""Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с
номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна
сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no"""

ticket_number = int(input("Введите номер вашего билета: "))
if ticket_number == 385916:
    print('У вас счастливый билет =)')
    access = True
if ticket_number != 385916:
    print('У вас обычный билет =(')