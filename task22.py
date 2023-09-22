#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все 
#те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
#Затем пользователь вводит сами элементы множеств.

a = int(input())
b = int(input())
a_string = []
b_string = []
res = []
c = 0
for i in range(0, a):
    a_num = input()
    a_string.insert(i, a_num)

for j in range(0, b):
    b_num = input()
    b_string.insert(j, b_num)

for i in range(0, a):
    for j in range(0, b):
        if a_string[i] == b_string[j]:
            if a_string[i] not in res:
                res.insert(c, a_string[i])
                c += 1

for i in range (0, len(res)-1):
    for j in range (i ,len(res)):
        if int(res[i]) > int(res[j]):
            c = res[i]
            res[i] = res[j]
            res[j] = c

print(res)
