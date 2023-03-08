n = int(input("N: "))

primenum = []
isprime = False
for x in range(2, n+1):
    for i in range(2, x):
        if x%i == 0:
            isprime = False
            break
        else:
            isprime = True
            break
    if isprime == True:
        primenum.append(x)

print(primenum)