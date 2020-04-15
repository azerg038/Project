#open the file
file=open("address.csv")
data=[]

#search for ontario
for x in file:
 value=x.find("Ontario")
 if value!=-1:
     data.append(x)

     #close the file
file.close()

#print data
print("residents of Ontario: ")
print(data)
