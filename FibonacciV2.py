# Fibonacci Series using Dynamic Programming  
FibArray=None
def call_Fibonacci(n):
 global FibArray
 FibArray = [0] * (n+1)
 return fibonacci(n)

def fibonacci(n):
    if n==0 or n==1:
     FibArray[n]=n
     return n

    else:
     FibArray[n]=fibonacci(n-1)+fibonacci(n-2)

    return FibArray[n]  

print("number is : ",call_Fibonacci(7))  
print("array : ",FibArray)

# find number n 
def findN(maxValue,index=0):
    while (call_Fibonacci(index))<=maxValue:
        # if call_Fibonacci(index)!=maxValue:
        #  index=index
        # else:
        index=index+1
         
    return index

#get array for fibonacci 
input=int(input("please enter a number: "))
numberN=findN(input)
print("the index is :",FibArray[0:numberN])
arr=FibArray[0:numberN]

#calcualt the sum of odd number
def sumOdd(array,number=0):
    for x in array:
        if(x%2!=0):
         number=x+number
    return number

print("the sum is : ",sumOdd(arr))
            