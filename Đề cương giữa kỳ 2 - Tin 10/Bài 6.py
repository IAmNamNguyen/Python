# Viết chương trình nhập vào N số nguyên, 
# in ra các số lớn hơn 3 và nhỏ hơn 6.

#Nhập N số nguyên trong dãy
N = int(input("Nhập số phần tử N số nguyên mà bạn muốn sẽ có trong dãy số: "))
#Tạo 1 danh sách rỗng
daySo = []
#Tạo vòng lặp với x lần tương ứng với số phần từ muốn có trong dãy:
for x in range(N):
    So = int(input("Nhập 1 số bất kỳ thứ " + str(x+1)+": "))
    daySo.append(So)

thoaManDeBai = []
for x in daySo:
    if 3 < x < 6:
        thoaManDeBai.append(x)

print("Các số lớn hơn 3 và bé hơn 6 là:",thoaManDeBai)
