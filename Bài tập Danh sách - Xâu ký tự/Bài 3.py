#Nhập vào B 1 chuỗi ký tự
B = str(input("Nhập 1 chuỗi ký tự B: "))

#Xuất ra màn hình chuỗi B
print("Chuỗi ký tự B là: ",B)

# 1. Kiểm tra B có ký tự số hay không?
for x in range(10):
    if x in B:
        print("B có chứa ký tự số")
        break
    else:
        print("B không chứa ký tự số")
        break