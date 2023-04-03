integer = int(input("Nhập 1 số nguyên: "))
#floatnum = float(input("Nhập 1 số thực: "))
#string = str("Nhập 1 chuỗi: ")
#characters = input("Nhập 1 thứ bất kỳ: ")
    
def isprime(N):
    if N<2:
        return str("No")
    elif N == 2:
        return str("Yes")
    elif N > 2:
        for x in range(2,N):
            if N%x == 0:
                break
        else:
            return str("Yes")

print(isprime(integer))