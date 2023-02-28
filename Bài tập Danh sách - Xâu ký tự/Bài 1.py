import random
import math

# Nhập vào 1 danh sách A gồm N phân tử

# Nhập N:
N = int(input("Nhập số phân tử N cho A: "))
# Tạo danh sách A có N phân tử gồm những số nguyên ngẫu nhiên từ khoảng -999 đến 999
A = [random.randint(-999, 999) for i in range(N)]
# Xuất danh sách A:
print("Danh sách A hiện tại gồm:",A)

# 1. Sắp xếp A theo thứ tự tăng dần
A_tangDan = sorted(A)
print("Danh sách A theo thứ tự tăng dần là:",A_tangDan)

# 2. Loại bỏ bớt các phần tử giống nhau sao cho mỗi giá trị chỉ xuất hiện 1 lần duy nhất
A_loc1 = dict.fromkeys(A) #dict.fromkeys() sẽ là 1 danh sách từ điển nơi mà các keys là các phần từ duy nhất trong danh sách
A_loc = sorted(A_loc1) #Sắp xếp lại thứ tự từ điển
# Xuất kết quả
print("Danh sách A đã lược bớt giá trị lặp là:",A_loc)

# 3. Tìm số lớn nhất, nhỏ nhất trong A
A_max = max(A) #Số lớn nhất
A_min = min(A) #Số bé nhất
# Xuất kết quả:
print("Số lớn nhất trong A là:",A_max) 
print("Số bé nhất trong A là:",A_min)

# 4. Tìm số chẵn dương lớn nhất
A_chanDuong = [] #Khởi tạo danh sách số chẵn dương
chanDuong = False #1 biến lôgic kích hoạt điều kiện
for x in A_loc: #Xét các giá trị trong danh sách đã lọc số lặp
    if x % 2 == 0 and x > 0: #Điều kiện số chẵn dương
        A_chanDuong += x #Thêm x vào danh sách
        chanDuong = True
if chanDuong == True: #điều kiện khi có số chẵn dương
    maxChanduong = max(A_chanDuong) #Số chẵn dương lớn nhất
    print("Số chẵn dương lớn nhất trong A là:",maxChanduong) #Xuất kết quả
if chanDuong == False: #điều kiện khi không có số chẵn dương
    print("A không có số chẵn dương.") 

# 5. Tìm số âm lẻ nhỏ nhất trong A
A_amLe = [] #Khởi tạo danh sách số âm lẻ
leAm = False #Biến logic
for x in A_loc:
    if x % 2 != 0 and x < 0: #Điều kiện số lẻ âm
        A_amLe += x #Thêm x vào danh sách
        leAm = True
if leAm == True:
    minLeAm = min(A_amLe) #Số lẻ âm nhỏ nhất
    print("Số âm lẻ nhỏ nhất trong A là:",minLeAm) #Xuất kết quả
if leAm == False:
    print("A không có số lẻ âm.")

# 6. Tìm các số chính phương trong A
# Số chính phương là các cố có căn bậc 2 là số nguyên
A_chinhPhuong = [] #Khởi tạo danh sách số chính phương
chinhPhuong = False #Biến logic
for x in A_loc:
    if math.sqrt(x) == int(math.sqrt(x)): #Kết quả căn bậc 2 của x liệu có bằng số nguyên kết quả căn bậc 2 của x
        A_chinhPhuong += x
        chinhPhuong = True
if chinhPhuong == True:
    print("Các số chính phương trong A là:",A_chinhPhuong)
if chinhPhuong == False:
    print("A không có số chính phương")

# 7. Tìm các số nguyên tố trong A
# Số nguyên tố là các số chỉ chia hết cho 1 và chính nó
A_nguyenTo = [] #Khởi tạo danh sách số nguyên tố
for x in A_loc:
    soNguyenTo = True #Giả sử x là số nguyên tố
    if x < 1: #Nếu x nhỏ hơn 1 thì không phải số nguyên tố
        soNguyenTo = False
    else: #Nếu x đã qua được điều kiện lớn hơn 1, tiếp tục xét x
        for i in range(2,int(math.sqrt(x))): #Duyệt các số từ 2 đến căn bậc 2 của x
            if x % i == 0: #Nếu x chia hết cho 1 số bất kỳ trong khoảng 2 đến căn 2 x
                soNguyenTo = False
                break #Kết thúc vòng lặp
    #Nếu x là số nguyên tố thì thêm vào danh sách
    if soNguyenTo == True:
        A_nguyenTo += x
if soNguyenTo == False:
    print("A không có số nguyên tố")
else:
    print("A có các số nguyên tố là:",A_nguyenTo)

# 8. 
