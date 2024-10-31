#bài 2
#nhập tọa độ 
x = float(input("nhập tọa độ x của điểm M:"))
y = float(input("nhập tọa độ y của điểm M:"))
a = float(input("nhập tọa độ a của điểm I:"))
b = float(input("nhập tọa độ b của điểm I:"))
r = float(input("nhập bán kính R:"))
m_i = (x-a)**2+(y-b)**2
ban_kinh = r**2
#xét điêu kiện nằm trong đường tròn khi khoảng cách <=R
if m_i <= ban_kinh:
    print("nằm trong đường tròn")
    print("đúng")
else:
    print("không nằm trong đường tròn")
    print("sai")