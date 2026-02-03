lst = [0, 1, 7, 2, 4, 8]   # приклад для перевірки

if len(lst) == 0:
    result = 0
else:
    s = 0
    i = 0

    while i < len(lst):
        s = s + lst[i]
        i = i + 2

    result = s * lst[-1]

print(result)