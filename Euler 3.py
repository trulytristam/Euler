n = 600851475143

a = [2]
greatest = 0

for i in range(2, 7000):
    check = 0

    for prim in a:
        if i % prim != 0:
            check = 1
        else:
            check = 0
            break

    if check == 1:
        if n % i == 0:
            greatest = i


