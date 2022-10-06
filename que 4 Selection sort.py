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

import time
#Best case for selection sort
print("\nBest case in selection sort is when array is in ascending order.") 
print("Example of best case for selection sort: [1 2 3 4] ")
begin=time.time()
SelectionSort([1,2,3,4])
end=time.time()
print("Array after performing selection sort: [1 2 3 4] ")
print("Time taken by best case: ",end-begin)

#Worst case for selection sort
print("\nWorst case in selection sort is when array [a1,a2...an] is in [a2,a3...an,a1] order.")
print("Example of worst case for selection sort: [2 3 4 1] ")
begin1=time.time()
SelectionSort([2,3,4,1])
end1=time.time()
print("Array after performing selection sort: [1 2 3 4] ")
print("Time taken by worst case: ",end1-begin1)
