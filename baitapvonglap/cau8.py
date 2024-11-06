n = int( input("Nhập vào một số nguyên dương n:"))
print(f"các số hoàn hảo nhỏ hơn{n} là:",end=" ")
#Duyệt qua từng số từ 2 đến n - 1
for n in range(2,n):
    s = 0 
    #Biến lưu tổng các ước số thực sự
# tìm các ước số thực sự của num 
for i in range(1,n):
    if n % i == 0:
        # kiểm tra nếu i là ước số của num 
        s = s + i 
        # cộng i vào tổng các ước số
#kiểm tra nếu tổng các ước số bằng chính num 
if s == n:
    print(n,end=" ")
