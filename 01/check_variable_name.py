import string
import keyword

name = input("Введіть ім'я змінної: ")

#  цифри
if name and name[0].isdigit():
    print(False)
    exit()

# 2.  великі літери
if any(ch.isupper() for ch in name):
    print(False)
    exit()

# 3.  пробіли
if " " in name:
    print(False)
    exit()

# 4.  пунктуацію ТІЛЬКИ "_"
for ch in name:
    if ch in string.punctuation and ch != "_":
        print(False)
        exit()

# 5.  НЕ БІЛЬШЕ одного "_"
if name.count("_") > 1:
    print(False)
    exit()

# 6. Не може бути зареєстрованим словом
if name in keyword.kwlist:
    print(False)
    exit()


print(True)
