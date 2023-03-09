N = int(input("Nhập số N: "))
prime_numbers = []
for num in range(2, N + 1):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        prime_numbers.append(num)
print(prime_numbers)

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