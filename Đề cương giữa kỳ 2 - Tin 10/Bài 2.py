# Nhập vào số điện tiêu thụ của gia đình bạn và viết chương trình tính số tiền phải trả biết:
#- 100 số đầu giá: 2000đ/số.
#- 50 số tiếp theo giá: 2500đ/số
#- 50 số tiếp theo giá: 3000đ/số
#- Các số tiếp theo tính giá: 4000đ/số.

#Nhập vào số điện 
soDien = int(input("Nhập vào số điện: "))

#Với 100 số đầu
if soDien <= 100:
    soTien = soDien*2000
    print("Số tiền cần phải trả cho",soDien,"số điện là:",soTien,"Đồng")
#Với 50 số tiếp theo (150):
if 100 < soDien <= 150:
    soTien = soDien*2500
    print("Số tiền cần phải trả cho",soDien,"số điện là:",soTien,"Đồng")
#Với 50 số tiếp theo nữa (200):
if 150 < soDien <= 200:
    soTien = soDien*3000
    print("Số tiền cần phải trả cho",soDien,"số điện là:",soTien,"Đồng")
#Các số tiếp theo (>200):
if soDien > 200:
    soTien = soDien*4000
    print("Số tiền cần phải trả cho",soDien,"số điện là:",soTien,"Đồng")