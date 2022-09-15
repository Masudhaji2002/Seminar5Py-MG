#1.Напишите программу, которая принимает 
# на вход вещественное число и показывает сумму его цифр.
number_str = input('Введите число')
summa = 0
for i in number_str:
    if i != ',':
        summa += int(i)
print(summa)
#2.Напишите программу, которая принимает на вход 
# число N и выдает набор произведений чисел от 1 до N.
number = int(input('input N: '))
factorial = 1
some_list = []
for i in range(1, number+1):
    some_list.append(factorial*i)
    factorial *= i
print(some_list)
#3.Задайте список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
n = int(input('Input n:' ))
summa = 0
for i in range(1, n+1):
    summa += (1 + 1 / i) ** i
print(summa)
#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции 
# хранятся в файле file.txt в одной строке одно число
from random import *
some_list = [randint(-10,10) for _ in range(randint(5,10))]
print(some_list)
shuffle(some_list)
print(some_list)

#5.Реализуйте алгоритм перемешивания списка.
import random
def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = random.randint(0, list_length - 1)
        
        temp = list[i]
        list[index_aleatory] = temp
    return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(list)
print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)