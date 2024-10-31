#bài 6 
#menu phim 
print("chào mừng bạn đến rạp phim ABC")
print("vui lòng bạn chọn thể loại phim")
print("phim tình cảm")
print("phim kinh dị")
print("phim hoạt hình")
print("phim khoa học viễn tưởng")
#nhập lựa chọn
lua_chon = float(input("nhập bộ phim bạn muốn lựa chọn(1->4):"))
if lua_chon == 1:
    print("phim tình cảm")
elif lua_chon == 2:
    print("phim kinh dị")
elif lua_chon == 3:
    print("phim hoạt hình")
elif lua_chon == 4:
    print("phim khoa học viễn tưởng")
else:
    print("lựa chọn không hợp lệ vui lòng thử lại")


