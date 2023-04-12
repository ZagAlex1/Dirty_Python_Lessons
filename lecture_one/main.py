# var = input('Введите переменную: ')
#
# print(var, end="\n")
# print(var, end=" ")
# print(var, end=" ")
# print(var, end=" ")
# print(var, end=" ")

# int
# float
# str
# bool

# var_1 = 1
# var_2 = '1'
# var_3 = 0.1
# var_4 = True

# type возвращает тип данных

# print(type(var_1))
# print(type(var_2))
# print(type(var_3))
# print(type(var_4))

# number_1 = 10
# number_2 = 5
#
# print(number_1 + number_2)
# print(number_1 - number_2)
# print(number_1 / number_2)
# print(number_1 * number_2)
# print(number_1 // number_2) # целочисленное деление
# print(number_1 % number_2)  # деление с остатком
# print(number_1 ** number_2) # возведение в степень
# print(number_1 == number_2)

# from decimal import Decimal
#
# a = Decimal('0.56')
# print(a)
# print(a * 100)

# text = "khj'l'jljk"
#
# letters = '''kjhkjhkjh
# kklklklk
# jhkjhkjhkjhkjh''' # многострочный комментарий
#
# print(letters)

# text = "sd344fsd fa5645sdf asd4564asd asd9687asd asd345asd"
# new_text = text.split()
#
# print(text.split(' ')) # разбить на список по нужному символу
#                        # по умолчанию, по пробелу
# print(text.replace(' ', "***")) # заменить одно на другое
# print(text.isdigit()) # проверяет записано ли в строке число
# print(text.isalpha()) # проверяет записан ли в строке символ
# print(text.lower()) # перевод в нижний регистр
# print(text.upper()) # перевод в верхний регистр
# print(text.index('f')) # индекс вхождения искомого элемента, ошибка
# print(text.find('f')) # индекс вхождения искомого элемента, -1
# print(text.rfind('f')) # индекс вхождения искомого элемента, -1,
#                        # поиск с права
# print(text.count()) # подсчет элементов

# Срезы у строк

text = "sd344fsd fa5645sdf asd4564asd asd9687asd asd345asd"
# print(text[start:finish:step])

print(text[9:])
print(text[:-10])
print(text[: : -1]) # получить строку задом на перед
print(text[text.index('f'):text.rindex('3')])