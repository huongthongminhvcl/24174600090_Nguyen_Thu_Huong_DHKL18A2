#Nhập vào n 
n = int(input("nhập vào một số dương n:"))
#Duyệt qua từng số từ 2 đến n-1
for n in range(2,n):
    is_prime = True
    #Giả sử num là số nguyên tố
#Kiểm tra từ 2 đến num - 1
for n in range(2,n):
    if n % i == 0: 
        #nếu tìm thấy ước thì không phải số nguyên tố
        is_prime = False
        break
# Nếu là số nguyên tố, in ra màn hình 
if is_prime:
    print(n,end=" ")
    print(f"Các số nguyên tố nhỏ hơn {n}là:",end=" ")
