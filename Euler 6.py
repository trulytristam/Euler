a = []
number = 0

while True:
    number += 280
    Alltrue = True

    for i in [19,18,17,16,15,14,13,12,11,7]:
        if number % i != 0:
            Alltrue = False
            break
    if number %1000000:
        print(number)
    if Alltrue:
        print(number)
        break