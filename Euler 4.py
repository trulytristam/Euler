def ispalin(num):
    for i in range(len(str(num)) // 2):
        if str(num)[i] != str(num)[-(i + 1)]:
            return False
    return True

greatest=myi=myj=n= 0
for i in range(0, 1000):
    for j in range(n, 1000):
        if ispalin(i * j):
            if i * j > greatest:
                myi,myj = i,j
                greatest = i * j
    n+=1
print(greatest)