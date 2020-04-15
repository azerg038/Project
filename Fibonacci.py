# Fibonacci Series using Dynamic Programming  
FibArray = [0, 1]
def fibonacci(n): 
    while len(FibArray)<n+1:  
        FibArray.append(0)  
    if n <= 1:  
        return n  
    else:  
        if FibArray[n - 1] == 0:  
            FibArray[n - 1] = fibonacci(n - 1)  
  
        if FibArray[n - 2] == 0:  
            FibArray[n - 2] = fibonacci(n - 2)  
              
    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]  
    return FibArray[n]  
# print(fibonacci(9))  
# print(FibArray)


def findN(maxValue,index=0):
    while (fibonacci(index))<=maxValue:
        if fibonacci(index)==maxValue:
         index=index
        else:
         index=index+1
         
    return index

numberN=findN(22)
print("the index is :",FibArray[0:numberN])

arr=FibArray[0:numberN]

def sumOdd(array,number=0):
    for x in array:
        if(x%2!=0):
         number=x+number
    return number

print("the sum is : ",sumOdd(arr))
            