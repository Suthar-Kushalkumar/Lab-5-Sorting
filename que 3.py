def InsertionSort(array):
  n=len(array)
  for i in range(1,n) :
    value=array[i]
    print("deciding for position",i,"incoming value:",value)
    pos=i
    while pos > 0 and value < array[pos-1] :
      print(value," < ", array[pos-1])
      array[pos] = array[pos-1]
      print('moving',array[pos-1],"to position",pos)
      pos-=1

    array[pos] = value
    print("found pos:",pos,"for value:",value)
    print("sorted subseq:",array[0:i+1],"\nremaining:",array[i+1:n],"\n")
    
  return(array)


arr=[]
n=int(input("Number of element in array: "))
for i in range(0,n):
    print("Enter", i,"th element")
    x=int(input())
    arr=arr+[x]
print(arr)
print("Performing insertion sort on array: ")
InsertionSort(arr)
print("Array after performing insertion sort: ",arr)



 


