a = [(1, 2), (2, 3), (3, 7), (4, 16)]

for i in a:
    result = 1
    for j in i:
        result *= j
    print(result)