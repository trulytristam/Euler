trinum = 1
for i in range(2,1000000000000):
    trinum = trinum + i
    div,half = 2,trinum//2
    num = 100
    for d in range(2,half):
        if d>=num:
            break
        if trinum%d ==0:
            num = trinum//d
            div = div + 2
        if d*d == trinum:
            div -=1

    if div > 500:
        print("FOUND:")
        print(trinum)
        break





# for i in range(1,10000000000000000):
#     trinum = trinum + i
#     if (not(trinum%2==0)and not(trinum%3==0)and not(trinum%5==0)):
#         print("hey")
#     print(trinum)





