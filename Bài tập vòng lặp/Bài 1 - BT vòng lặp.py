# Cho dãy số vô hạn 12, 15, 18, 21,...
# Viết chương trình in ra số hạng thứ 2023

#Có công thức tìm số của vị trí số hạng:
#Số hạng thứ n = (n-1)*Khoảng cách + Số đầu

#Ta thấy dãy số vô hạn 12, 15, 18, 21,.. có khoảng cách là 3 
#Suy ra số hạng thứ 2023 là = (2023-1)*3+12

soHang2023 = (2023-1)*3+12

print("Số hạng thứ 2023 của dãy số vô hạn 12, 15, 18, 21,... là:",soHang2023)

#Cách 2:
# Dãy số này có quy luật là mỗi số hạng bằng số hạng trước đó cộng với 3
# Ta có thể sử dụng vòng lặp vô hạn while

# Khởi tạo số hạng đầu tiên
a = 12
# Khởi tạo biến đếm
count = 2
# Sử dụng vòng lặp while để tạo dãy số vô hạn
while True:
    # Lấy số hạng trước cộng thêm 3
    b = a + 3
    #Test:
    print(b)
    # Tăng biến đếm lên một đơn vị
    count += 1
    # Kiểm tra nếu biến đếm bằng 2023 thì in ra giá trị của c và thoát khỏi vòng lặp
    if count == 2023:
        print(b)
        break
