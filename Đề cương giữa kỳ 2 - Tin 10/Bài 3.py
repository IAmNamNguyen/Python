# Nhập vào 1 số nguyên N, viết chương trình in ra các số chẵn 
# từ 1 đến N và tính tổng các số đó.

#Nhập N:
N = int(input("Nhập 1 số nguyên N: "))
tong = 0 # Tổng dãy số chẵn
soChan = [] #Tạo danh sách rỗng
# Dùng vòng lặp for để xét các số từ 1 đến N
# for x in range là gán giá trị cho biến x với
# các số trong khoảng range() mình đặt lần lượt
# từ điểm đầu đến điểm cuối
# Ví dụ cho range(1,N+1) nghĩa là đặt lần lượt x với
# 1, 2, 3,... N; range(N) thì nghĩa là xét từ 0 đến N-1
# Lý do muốn xét N phải cần N+1 vì nó sẽ bắt đầu đếm từ 0 là
# 1 giá trị nên nếu để N nó sẽ thành N-1
# Ví dụ: N = 10
# for sẽ đếm 10 giá trị bắt đầu từ 0
# => 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# Vì vậy muốn xét cả N (10) thì cần +1
# Việc đếm giá trị ko liên quan gì đến giới hạn giá trị
# của range(), vì giới hạn giá trị là để gán cho x
for x in range(1,N+1): #Vòng lặp for 
    # for là 1 vòng lặp vì khi gán giá trị trong khoảng
    # với x, thì bắt đầu tính toán với code bên trong nó,
    # tính toán xong lại bắt đầu lại với 1 x khác trong
    # khoảng range()
    if x%2 == 0:
        #Công thức của append:
        #(TênDanhSách).append(GiáTrị/TênBiến)
        soChan.append(x) #.append() là thêm phần từ vào danh sách
        tong = tong + x 

#Xuất kết quả:
print("Các số chẵn từ 1 đến N gồm:",soChan)
print("Tổng của các số đó là:",tong)

         
