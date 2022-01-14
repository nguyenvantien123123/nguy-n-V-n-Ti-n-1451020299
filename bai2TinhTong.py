# Nhập và in ra màn hình tên của mình
ten = input("Nhập tên đệm của bạn : ")
print("Tên đệm của bạn là:", ten)


def tinhtongdodai(n):
    total = 0;
    while (n > 0):
        total = total +  n % 10;
        n = int(n / 10);
    return total;
 
n = int(input("nhập n bằng độ dài tên của mình và tên đệm = "));
print("Tổng các chữ số của", n , "là", tinhtongdodai(n));
