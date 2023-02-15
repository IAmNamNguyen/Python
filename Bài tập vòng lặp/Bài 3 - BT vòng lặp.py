# Nhập vào 1 số N
# Kiểm tra xem N có phải số nguyên tố hay không?
# Số nguyên tố là số chỉ có 2 ước duy nhất là 1 và chính nó

#Nhập N:
N = float(input("Nhập số N: "))

#Đặt biến điều kiện:
dieuKien1 = N%N == 0
dieuKien2 = N%1 == 0
dieuKien = [dieuKien1, dieuKien2]

#Thuật toán:
if False in dieuKien:
  print("N không phải số nguyên tố")
else:
  print("N là số nguyên tố")