def SelectionSort(array):
    l=len(array)
    for i in range(l-1):
        smallNdx= i
        for j in range(i+1,l):
            if array[j] < array[smallNdx] :
                smallNdx=j
        print("Minimum is:",array[smallNdx])
        if smallNdx != i :
            temp = array[i]
            array[i] = array[smallNdx]
            array[smallNdx] = temp
            print("Replace: ",array[smallNdx],"with",array[i],": ",array)
        else:
            print(array[i],"is already in place")

    return(array)

arr=[]
n=int(input("Number of element in array: "))
for i in range(0,n):
    print("Enter", i,"th element")
    x=int(input())
    arr=arr+[x]
print(arr)
print("Performing selection sort on array: ")
SelectionSort(arr)
print("Array after performing selection sort: ",arr)


