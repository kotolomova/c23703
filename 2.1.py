# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)


# TODO здесь ваш код

if month == 2:
    print("в нем ", 28, " дней")
elif month%2 == 1 and month > 0 and month < 8 or month%2 == 0 and month > 7 and month < 13:
    print ("в нем ", 31, " день")
elif month%2 == 0 and month > 1 and month < 7 or month%2 == 1 and month > 8 and month < 12:
    print("в нем ", 30, " дней")
else:
    print('номер некорректен')