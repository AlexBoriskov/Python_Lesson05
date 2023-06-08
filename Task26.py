# Задача 26. Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def tryTipy (num):
    while type(num) != int:
        try:
            num = int(num)
        except ValueError:
            print ("Ошибка!")
            num = input ("Введите число повторно: ")
    return num

def exponentiation (a, b, i, result):
    if i < b and b>=0:
        result *= a
        i += 1
        result = exponentiation(a,b,i,result)
    elif i>b and b<0:
        result /= a
        i -=1
        result = exponentiation(a,b,i,result)
    return result

number = input("Введите число: ")
number = tryTipy(number)

degree = input("Введите степерь возведения: ")
degree = tryTipy(degree)

count = 0
result = 1

result = exponentiation(number, degree, count, result)
print ("{0}^{1} = {2}" .format(number, degree,result))


