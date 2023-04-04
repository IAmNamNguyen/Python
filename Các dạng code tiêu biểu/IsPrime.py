N = int(input("Nhập số N: "))

def listprimes(N):
    prime_numbers = []
    for num in range(2, N + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)
    return prime_numbers

'''
Trong đoạn code trên, else không cùng hàng với if mà cùng hàng với for. 
Đây là một cấu trúc điều khiển đặc biệt trong Python được gọi là for-else.
Cấu trúc for-else cho phép chúng ta thực hiện một khối lệnh khi vòng lặp for kết thúc mà không gặp lệnh break. 
Trong trường hợp này, nếu số num không chia hết cho bất kỳ số nào từ 2 đến num - 1, 
thì vòng lặp sẽ kết thúc mà không gặp lệnh break, 
và khối lệnh trong else sẽ được thực hiện (tức là thêm số nguyên tố vào danh sách).
Nếu có lệnh break, tức là số num chia hết cho một số từ 2 đến num - 1, 
thì vòng lặp sẽ thoát ra và khối lệnh trong else sẽ không được thực hiện.
'''

def isprime(N):
    if N<2:
        return str("Không phải số nguyên tố")
    uoc = 1
    dem = 2
    while dem < N//2:
        if N%dem == 0:
            uoc = uoc + 1
        dem = dem + 1
    if uoc == 1:
        return str("Là số nguyên tố")
    else:
        return str("Không phải số nguyên tố")

def prime(N):
    if N<2:
        return "No"
    elif N == 2:
        return "Yes"
    elif N > 2:
        for x in range(2,N):
            if N%x == 0:
                break
        else:
            return "Yes"
    
print(isprime(N))
print("Các số nguyên tố từ 1 đến N:",listprimes(N))
print("Số nguyên tố? -",prime(N))