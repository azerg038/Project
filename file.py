file=open("address.csv")
data=[]

for x in file:
 value=x.find("Ontario")
 if value!=-1:
     data.append(x)
file.close()

print("residents of Ontario: ")
print(data)
