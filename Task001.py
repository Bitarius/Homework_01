'''
Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
'''

number = int(input('Ведите трехзначное число: '))
print(number)

if number < 100 or number > 999:
    print('Это не трехзначное число, но я всё равно посчитаю')

sum = 0

for i in range(number):
    number_1 = number % 10
    sum = sum + number_1
    number = number // 10

print(f'Сумма цифр этого числа равна {sum}')
