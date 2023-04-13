from math import comb
a = int(input('Nhập số a: '))
b = int(input('Nhập số b: '))
n = int(input('Nhập số luỹ thừa: '))
k = n
h = 0
A = []
N = []
def superscripts(num):
    numsup = ["\u2070","\u00b9","\u00b2","\u00b3","\u2074","\u2075","\u2076","\u2077","\u2078","\u2079"]
    if 0 <= num < 10:
        for x in range(10):
            if num == x:
                return numsup[x]
    elif num >= 10:
        uni = []
        digits = [int(digit) for digit in str(num)]
        for n in digits:
            for x in range(10):
                if n == x:
                    s = numsup[x]
                    uni.append(s)
        result = str("".join(uni))
        return result
def subscripts(num):
    numsub = ["\u2080","\u2081","\u2082","\u2083","\u2084","\u2085","\u2086","\u2087","\u2088","\u2089"]
    if 0 <= num < 10:
        for x in range(10):
            if num == x:
                return numsub[x]
    elif num >= 10:
        uni = []
        digits = [int(digit) for digit in str(num)]
        for n in digits:
            for x in range(10):
                if n == x:
                    s = numsub[x]
                    uni.append(s)
        result = str("".join(uni))
        return result
print('Đẳng thức là:','('+str(a)+'+'+str(b)+')'+superscripts(n))
for x in range(n+1):
    s = comb(n, k)*(a**(n-h))*(b**(n-k))
    S = 'C'+subscripts(n)+superscripts(h)+str(a)+superscripts(n-h)+str(b)+superscripts(n-k)
    A.append(s)
    N.append(S)
    k = k - 1
    h = h + 1

print(N)
print(A)