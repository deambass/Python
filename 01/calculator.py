while True:
    a = float(input("Введіть перше число: "))
    operation = input("Введіть дію (+, -, *, /): ")
    b = float(input("Введіть друге число: "))

    if operation == "+":
        print("Результат:", a + b)

    elif operation == "-":
        print("Результат:", a - b)

    elif operation == "*":
        print("Результат:", a * b)

    elif operation == "/":
        if b == 0:
            print("Помилка: ділити на 0 не можна!")
        else:
            print("Результат:", a / b)

    else:
        print("Помилка: невідома дія")

    # ---- Запит на продовження ----
    again = input("Бажаєте продовжити? (y/yes): ")

    if again == "y" or again == "yes":
        continue
    else:
        print("Некоректно введена відповідь. Роботу калькулятора завершено.")
        break

#cycle = "y"

#while cycle == "y" or cycle == "yes":

    a = float(input("Введіть перше число: "))
    operation = input("Введіть дію (+, -, *, /): ")
    b = float(input("Введіть друге число: "))

    if operation == "+":
        print("Результат:", a + b)

    elif operation == "-":
        print("Результат:", a - b)

    elif operation == "*":
        print("Результат:", a * b)

    elif operation == "/":
        if b == 0:
            print("Помилка: ділити на 0 не можна!")
        else:
            print("Результат:", a / b)

    else:
        print("Помилка: невідома дія")

    cycle = input("Продовжити? (y/yes): ").lower()

    if cycle not in ["y", "yes"]:
        print("Некоректно введена відповідь. Роботу калькулятора завершено.")
        break
