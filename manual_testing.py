from functions import salary, hello_who

# 1 способ. Написать программу и проверять. Долгий вариант
# 2способ. Отдельно проверить функцию ВРУЧНУЮ. Нам нужно подумать правильно ответила программа
#print(hello_who('Max'))

# salary(2, 10) == 20
# print(salary(2, 10))

# С помощью if
if salary(2, 10) != 20:
    print('Failed')
if hello_who('Max') != 'Hello, Max':
    print('Failed')
if hello_who('Leo') != 'Hello, Leo':
    print('Failed')

print('Ok')