#Using the rule above and starting with 13, we generate the following sequence:

#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

import time

def is_even(n):
    return n//2

def is_odd(n):
    return 3*n+1

def Collatz(start):
    chain_length = 1
    while start != 1:
        if start%2==0:
            start = is_even(start)
        elif start%2!=0:
            start = is_odd(start)
        chain_length+=1
    return chain_length


answer = 0
greatestchain = 0
for i in range(1,1000000):
    if i%50000==0:
        print("i: ", i)
    a = Collatz(i)

    if a > greatestchain:
        answer = i
        greatestchain = a

print(answer)
print(greatestchain)


