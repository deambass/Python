#Number = float(input("Введіть число:" ))
#square = Number ** 2
#print("Квадрат числa",square)

#a = float(input("Введіть перше число: "))
#b = float(input("Введіть друге число: "))
#average = (a + b + c) / 3
#print("Середнє:", average)

#minutes = int(input("Введіть кількість хвилин: "))
#hours = minutes // 60
#remaining_minutes = minutes % 60
#print(hours, "години", remaining_minutes, "хвилин")

#minutes = int(input("Введіть кількість хвилин: "))
#hours = minutes // 60
#rest = minutes % 60
#print(hours, "години", rest, "хвилин")

#price = float(input("Ввудіть ціну"))
#discount = float(input("Введіть знижку (%):"))
#discount_value = price * discount / 100
#final_price = price - discount_value
#print("Ціна зі знишкою", final_price)

#number = int(input("Введіть число: "))
#last_digit = number % 10
#print("Остання цифра:", last_digit)

#length = float(input("Введіть довжину: "))
#width = float(input("Введіть ширину: "))
#perimeter = (length + width) * 2
#print("Периметр:", perimeter)

number = int(input("Введіть 4-х значне число: "))
digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10
print(digit1)
print(digit2)
print(digit3)
print(digit4)