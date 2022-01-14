fullname = str(input("Nhập tên và mã số sinh viên "))
print(fullname)

import re
data = input("Nhập vào các giá trị: ")

l = re.findall(r'\d+', data)
t = tuple(l)

print(data)

print(l)
print(t)