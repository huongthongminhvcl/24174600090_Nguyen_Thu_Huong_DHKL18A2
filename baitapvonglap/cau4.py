n = int(input("nhap so duong can tim"))
if n <=1:
    print("so nay khong phai la so nguyen to")
else:
    k = n 
    for i in range(n):
        if n % k ==0 and k !=n and k !=1:
            print("so nay khong phai so nguyen to")
            break
        k = k-1
    else:
        print("so nay la so nguyen to")