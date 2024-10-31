#bài 3
#nhập hệ số
#nhập ba số người dùng
a = float(input("nhập số thứ nhất:"))
b = float(input("nhập số thứ hai:"))
c = float(input("nhập số thứ ba:"))
#tìm số lớn nhất 
if a >= b and a >= c:
    so_lon_nhat = a
elif b >= a and b >= c:
    so_lon_nhat = b
else :
    so_lon_nhat = c
    print(f"số lớn nhất là:{so_lon_nhat}")
