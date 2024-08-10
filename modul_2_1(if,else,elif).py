# Ввод трех целыйх чисел
first = int(input('Put the first number: '))
second = int(input('Put the sencond number: '))
third = int(input('Put the third number: '))

# Проверкат на равенство
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
