# Viết chương trình nhập vào 1 dãy số ngẫu nhiên từ bàn phím, 
# in ra các số chẵn dương và vị trí của chúng.

#Đầu tiền ta nhập muốn bao nhiêu phần tử trong dãy
phanTu = int(input("Nhập số phần tử mà bạn muốn sẽ có trong dãy số: "))
#Tạo 1 danh sách rỗng
daySo = []
#Tạo vòng lặp với x lần tương ứng với số phần từ muốn có trong dãy:
for x in range(phanTu):
    So = float(input("Nhập 1 số bất kỳ thứ " + str(x+1)+": "))
    daySo.append(So)
#Tìm số chẵn dương:
soChanDuong = [] #Tạo danh sách rỗng sẽ chứa số chẵn dương
ViTri = []  #1 danh sách rỗng sẽ chứa số thứ tự vị trí của
            # số chẵn dương có trong danh sách 'daySo'
for x in range(len(daySo)):
    #len(TênDãy) chỉ số lượng phần tử trong dãy
    #Hoặc nói cách khác là các vị trí của phần tử
    #trong dãy từ 0 đến hết phần tử
    #Có trong sgk
    #Ví dụ:
    #dãyA = [14, 22, 332, 14, 12]
    #Số 12 ở vị trí cuối cùng là 4
    #=> len(dãyA) = 4
    #=> range(4)
    #Vì dãy số ko cố định đc số phần tử nên dùng cách này
    if daySo[x] > 0 and daySo[x] % 2 == 0:
        #daySo[x] với x là vị trí phân tử trong dãy
        #daySo[x] sẽ trả về giá trị là dữ liệu của phần tử đó
        #Ví dụ:
        #dãyA = [14, 22, 332, 14, 12]
        # Có số 14 ở vị trí 0, 22 ở vị trí 1, 332 ở vị trí 2
        #dãyA[0] = 14
        #dãyA[1] = 22
        #dãyA[2] = 332
        soChanDuong.append(daySo[x])
        ViTri.append(x) #Vị trí của x trong dãy số mình tạo
        # Ví dụ:
        # dãyA = [14, 22, 332, 14, 12]
        # Có số 14 ở vị trí 0, 22 ở vị trí 1, 332 ở vị trí 2
        # trong dãy
print("Các số chẵn dương trong dãy là:",soChanDuong,", tương ứng với các vị trí trong dãy là:",ViTri)
