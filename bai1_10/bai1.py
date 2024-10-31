#bai1
#Nhập năm
year = int(input("nhập năm :"))
#điều kiện năm nhuận chia hết cho 4,nhưng không chia hết 100 hoặc chia cho 400
if year %4 ==0 and year %100 !=0 or year %400 ==0:
    print("là năm nhuận")
else: 
    print("không phải là năm nhuận,vui lòng nhập lại")