lists = ["-",".","a"]


last = 0
current = 1
unit = 0

mynum = []


for i in range(40):
    unit = last + current
    last = current
    current = unit

    if current>= 4000000:
        break

    if current%2==0:
        mynum.append(current)







print(sum(mynum))









