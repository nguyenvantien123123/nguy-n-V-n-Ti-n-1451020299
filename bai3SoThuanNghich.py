# Nhập và in ra màn hình tên của mình
ten = input("Nhập tên đầy đủ của bạn  : ")
print("Tên đầy đủ của bạn là: ", ten)


# chạy chương trình bằng cách nhập n từ bàn phím bằng cách tạo n như sau lấy số lượng họ , tên đệm, tên 
def isThuanNghich(n):
    str1 = str(n);     # ep kieu so n thanh chuoi
    str2 = str1[::-1]; # dao nguoc chuoi str1
    if (str1 == str2):
        return True;
    else:
        return False;

n = int(input("Nhập số lượng họ , tên đệm, tên  = "));
print("Tổng các chữ số của", n , "là", isThuanNghich(n));

