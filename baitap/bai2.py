#bài 2
inport math
# nhập giá trị biểu thức
x= float(input("nhập giá trị biểu thức x:"))
# điều kiện của biểu thức 
if x>=0 and x!=0:
    print("giá trị không được â hoặc bằng 0")
else:
    print("giá trị không thỏa mãn")
# tính giá trị biểu thức 
f_x = -x+math.sqrt(x**2 + 4)/math.pow(x**4 + 1,1/7)
#in ra kết quả 
print("giá trị biểu thức:{f_x:.2f}")
print("kết thúc chương trình")