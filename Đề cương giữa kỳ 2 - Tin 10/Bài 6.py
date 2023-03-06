# Viết chương trình nhập vào N số nguyên, 
# in ra các số lớn hơn 3 và nhỏ hơn 6.

#Nhập N số nguyên trong dãy
N = int(input("Nhập số phần tử muốn có trong dãy số: "))
#Tạo 1 danh sách rỗng
daySo = []
#Tạo vòng lặp với N lần tương ứng với số phần tử muốn có trong dãy:
for x in range(N):
    daySo.append(int(input("Nhập 1 số bất kỳ thứ " + str(x+1)+": ")))

lonHonBa = []
beHonSau = []
for x in daySo:
    if x>3:
        lonHonBa.append(x)
    if x<6:
        beHonSau.append(x)

if lonHonBa == []:
    print("Không có số lớn hơn 3.")
else:
    print("Các số lớn hơn 3 là:",lonHonBa)
if beHonSau == []:
    print("Không có số bé hơn 6.")
else:
    print("Các số bé hơn 6 là:",beHonSau)

