# Сумма трехзначного числа
num = int(input("Введите трехзначное число: "))
a = num // 100
b = (num % 100) // 10
c = num % 10

print(a+b+c)

#журавлики
S = int(input("Введите общее количество журавликов: "))
if not S % 6:
     x = S // 6
     print(f'Катя {x * 4} ')
     print(f'Сережа {x} ')
     print(f'Петя {x}')

#общественный транспорт
while True:
    number = input('Введите шестизначный номер Вашего билета: ')
    if number.isdigit() and len(number) == 6:
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            print('Ваш билет счастливый!')
        else:
            print('Ваш билет не счастливый(')
        break
    else:
        print('Введен некорректный номер билета, попробуйте еще раз)')

#шоколадки
n = int(input("Введите один размер шоколадки в дольках: "))
m = int(input("Введите другой размер шоколадки в дольках: "))

k = int(input("Введите количество долек, которое хотите отломить: "))

if k < m * n and (k % m == 0 or k % n == 0):
    print('Да')
else:
    print('Нет')
