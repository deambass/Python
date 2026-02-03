lst = [0, 1, 0, 12, 3]

result = []
zero_count = 0

for x in lst:
    if x == 0:
        zero_count = zero_count + 1
    else:
        result.append(x)

i = 0
while i < zero_count:
    result.append(0)
    i = i + 1

print(result)