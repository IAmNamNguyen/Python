# Viết chương trình  tìm  các số nguyên a, b, c, d khác nhau 
# trong khoảng 0 tới 10 thỏa mãn điều kiện:
# a*d*d= b*c*c*c

import random

#Ta đặt random cho b, c, d
#a ở đây sẽ là số cần tìm tùy biến theo thuật toán 
# để thỏa mãn a*d*d= b*c*c*c
b = random.randint(0, 11)
c = random.randint(0, 11)
d = random.randint(0, 11)
while b == c or b == d or d == c: #Check trùng random b, c, d và random lại
    b = random.randint(0, 11)
    c = random.randint(0, 11)
    d = random.randint(0, 11)

for a in range (0,11):
    if a != b and a != c and a != d: #Đảm bảo a không trùng b, c, d
        check = a*d*d == b*c*c*c
        if check == True:
            break

print("Các số nguyên a, b, c, d khác nhau trong khoảng 0 - 10 thỏa mãn điều kiện a*d*d= b*c*c*c là:",a, b, c, d)
# Thuật toán random này sẽ không có kết quả giá trị cụ thể
# Mà ta phải check điều kiện của đề bài cho so với giá trị trả về
