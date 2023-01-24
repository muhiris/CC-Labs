for itm in f:
 for each in itm:
     if ((ord(each)>65 and ord(each)<127) or each in check):
      print(temp)
      temp+=each
     else:
         print('yayy')

s= temp.split(' ')
print(s)
