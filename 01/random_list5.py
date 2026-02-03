import random


n = random.randint(2, 25)

lst = []
i = 0
while i < n:
    lst.append(random.randint(1, 10))
    i = i + 1

print("Початковий список:", lst)

# новий список: перший, третій і другий з кінця
result = [lst[0], lst[2], lst[-2]]

print("Новий список:", result)