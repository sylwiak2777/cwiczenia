#liczby pierwsze


def primes(limit):
    tab=[]
    for i in range(2,limit):
        for j in tab:
            if i % j == 0: break
        else:
            yield i
            tab.append(i)

for i in primes(100):
    print (i)
