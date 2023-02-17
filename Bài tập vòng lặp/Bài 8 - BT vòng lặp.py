# Viết chương trình in ra tất cả các số nguyên tố
# trong khoảng từ 2 đến N với N được nhập từ bàn phím

from math import sqrt

# Nhập N:
N = int(input("Nhập số N: "))
while N<2:
    N = int(input("N phải lớn hơn 1, xin nhập lại: "))

num = []

for i in range(2,N+1):
    for s in range(2,int(sqrt(i)+1)):
        if i%s == 0:
            num += (i,)



print("Các số nguyên tố từ 2 đến N (",N,") là:",num)
     