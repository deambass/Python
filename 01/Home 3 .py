#a = float(input("Введіть перше число: "))
#op = input("Введіть дію (+, -, *, /): ")
#b = float(input("Введіть друге число: "))

#   if op == "+":
#    print("Результат:", a + b)
#   elif op == "-":
#    print("Результат:", a - b)
#   elif op == "*":
#    print("Результат:", a * b)
#   elif op == "/":
#   if b == 0:
#    print("Помилка: ділити на 0 не можна!")
#   else:
#    print("Результат:", a / b)
#   else:
#    print("Помилка: невідома дія")

    #Перемістити елемент у списку

#lst = [10, 20, 30, 40, 50]
#print("Початковий список:", lst)

#old_i = input("Введіть індекс елемента, який перемістити: ")

#if not old_i.isdigit():
#    print("Помилка: потрібно вводити тільки число!")
#else:
#    old_i = int(old_i)

#    if old_i < 0 or old_i >= len(lst):
#        print("Помилка: такого індексу в списку немає!")
#    else:
#        new_i = input("Введіть новий індекс: ")

#        if not new_i.isdigit():
#            print("Помилка: потрібно вводити тільки число!")
#        else:
#            new_i = int(new_i)

#            if new_i < 0 or new_i > len(lst):
#                print("Помилка: некоректний новий індекс!")
#            else:
#                elem = lst.pop(old_i)
#                lst.insert(new_i, elem)
#                print("Новий список:", lst)

    #Розділити один список на два списки

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_list = []
odd_list = []

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        even_list.append(numbers[i])
    else:
        odd_list.append(numbers[i])
    i = i + 1

print("Початковий список:", numbers)
print("Парні:", even_list)
print("Непарні:", odd_list)