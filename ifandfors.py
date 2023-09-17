def compute_values(n):
    values = []
    for i in range(n):
        if i == 0:
            values.append(3)
        elif i % 2 == 0:
            values.append(2 * i)
        else:
            values.append(i * i)
    return values
T = int(input())
for _ in range(T):
    n=int(input())
    result =compute_values(n)
    print(*result)
