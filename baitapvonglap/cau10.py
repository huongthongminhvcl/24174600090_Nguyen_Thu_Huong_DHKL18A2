#Nhập hai số bất kỳ
a = int(input("nhập số thứ nhất:"))
b = int(input("nhập số thứ hai :"))
# xác định giá trị nhỏ nhất giữa hai số để tối ưu vòng lặp
nho_nhat = min(abs(a),abs(b))
#lấy giá trị tuyệt đối để tránh số âm
#tìm ước chung lớn nhất (UCLN) bằng cách duyệt ngược từ giá trị nhỏ nhất về 1
ucln = 1
for i in range(nho_nhat, 0 , -1):
    if a % i == 0 and b % i == 0:
        ucln = i 
        break 
    #in ra kết quả UCLN
    print(f"Ước chung lớn nhất của{a} và {b} là:{ucln}")
