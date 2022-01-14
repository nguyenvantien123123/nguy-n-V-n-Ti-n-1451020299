

fullname = str(input("Nhập tên của bạn "))
print(len(fullname))

myDict = {}
for x in range(1, len(fullname) + 1):
    myDict[x] = x * x
    
print("\nDictionary = ", myDict)

# print (d)
number = int(input("nhập n bằng độ dài tên của mình : "))
myDict = {}

for x in range(1, number + 1):
    myDict[x] = x * x
    
print("\nDictionary = ", myDict)

