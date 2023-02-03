f = open("C:/Users/Abdullah/Desktop/test/Compiler Construction/file_handle/src.txt", "rt")
a= []
for each_item in f:
   
    temp = [int(x) for x in each_item.split(" ")]
    a.append(temp)
print(a)