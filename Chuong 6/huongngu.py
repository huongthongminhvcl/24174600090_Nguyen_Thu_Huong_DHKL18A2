import math

n_kinh = float(input("Nhập bán kính khối trụ: "))
chieu_cao = float(input("Nhập chiều cao khối trụ: "))

# công thức Sxq Stp
pi = 3.14
dien_tich_xung_quanh = 2 * pi * ban_kinh * chieu_cao
dien_tich_toan_phan = 2 * pi * ban_kinh * (ban_kinh + chieu_cao)
the_tich = pi * ban_kinh ** 2 * chieu_cao

# Làm tròn kết quả đến hai chữ số thập phân
dien_tich_xung_quanh = round(dien_tich_xung_quanh, 2)
dien_tich_toan_phan = round(dien_tich_toan_phan, 2)
the_tich = round(the_tich, 2)

# in ra kết quả
print(f"Diện tích xung quanh: {dien_tich_xung_# Nhậ bán kính và chiều cao từ bàn phím
baquanh}")
print(f"Diện tích toàn phần: {dien_tich_toan_phan}")
print(f"Thể tích: {the_tich}")




#bai2
#tu so = -x + (x**2 + 4)**(1/2)
#mau so = (x**4 + 1)**(1/7)
#f_x = (-x + (x**2 +4)**(1/2)/(x**4 + 1)**(1/7))
print(f"Gia tri cua f(x) = {f_x:.2f}")
       grade1 = 80
grade2 = 90
average = (grade1 + grade2) / 2
print(average