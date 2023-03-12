'''
Cho N là số học sinh nhập từ bàn phím.
Các học sinh này mỗi người muốn gửi bài của mình cho nhau.
Hãy tính số lần gửi thư sao cho tất cả học sinh đều nhận được 
tất cả các bài của những học sinh khác.

Ví dụ: Có 3 học sinh. Người 1 gửi cho người 3 bài của người 1, 
người 2 gửi cho người 3 bài của người 2,
người 3 gửi cho người 1 bài của người 3 với bài của người 2,
người 3 gửi cho người 2 bài của người 3 với bài của người 1.
Tổng 4 lần gửi thư.
'''

# Phân tích ta thấy là sẽ có 1 người chuyên nhận của tất cả mọi người khác và
#sau đó chuyển tiếp bài của những người khác cho từng người sau cho mỗi người đều có
#bài của những người khác. Ta coi như người này là 'monitor' (lớp trưởng) và những
# người khác là 'others' đi.

N = int(input("Nhập số học sinh: ")) #Số học sinh tương đương với tổng số bài
#Số học sinh = tổng số bài 
others = N-1 #N-1 đứa khác gửi cho monitor (vì không tính monitor) = tổng số lần gửi 1
monitor = others #monitor gửi lại cho những đứa kia mỗi đứa bài của những đứa còn lại và bài của monitor
# = tổng số lần gửi 2
tongthu = others + monitor

print(tongthu)
