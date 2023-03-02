#Nhập vào B 1 chuỗi ký tự
B = str(input("Nhập 1 chuỗi ký tự B: "))

#Xuất ra màn hình chuỗi B
print("Chuỗi ký tự B là: ",B)

# 1. Kiểm tra B có ký tự số hay không?
chuSo = any(x.isnumeric() for x in B)
if chuSo == True:
  print("B có chứa ký tự số")
else:
  print("B không chứa ký tự số")
   
# 2. Kiểm tra B có ký tự in hoa không?
# Sử dụng hàm any() để duyệt ký tự
# Sau đó dùng .isupper() để check in hoa
inHoa = any(x.isupper() for x in B)
if inHoa == True:
  print("B có ký tự in hoa")
else:
  print("B không có ký tự in hoa")