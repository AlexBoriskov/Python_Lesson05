# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def summa (a, b, res,i):
    if i!=b and b>0:
        res +=1
        i+=1
        res = summa (a,b,res,i)
    elif i!=b and b<0:
        res -=1
        i -=1
        res = summa (a,b,res,i)
    return res

number01 = int(input ("Введите первое число: "))
number02 = int(input("Введите второе число: "))

result = number01
count = 0

result = summa (number01, number02, result, count)
print (result)