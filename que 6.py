def partitionSeq(a,low,high):
    if(low >= high):
        return
    p = a[(low + high) // 2] #// is for floor division
    print(p)
    i = low - 1
    j = high + 1
    l=len(a)
    while(l):
        while(l):            
            i += 1
            if(a[i] >= p):
                break
        while(l):            
            j -= 1
            if(a[j] <= p):
                break
        if(i >= j):
            break
        a[i],a[j] = a[j],a[i]
    partitionSeq(a, low, j)
    partitionSeq(a, j+1, high)

def quickSort(theSeq):
    m = len( theSeq ) 
    partitionSeq( theSeq, 0, m-1 )
    
arr=[]
n=int(input("Number of element in array: "))
for i in range(0,n):
    print("Enter", i,"th element")
    x=int(input())
    arr=arr+[x]
print(arr)
print("Performing quick sort on array: ")
quickSort(arr)
print("Array after performing quick sort: ",arr) 

