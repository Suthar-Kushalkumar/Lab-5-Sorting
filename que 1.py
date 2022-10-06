def BubbleSort(array): 
  n=len(array)

  for i in range(n-1) :
    for j in range(n-1-i) :
      print("Comparing",array[j],array[j+1])
      swap=0
      if array[j] > array[j+1] :
        print("Swapping",array[j],array[j+1])
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        swap=swap+1
    print("End of pass:",i+1)
    print("\n")
    if swap==0:
      print("All elements are sorted so no need to compare further.")
      return

  return(array)

arr=[]
n=int(input("Number of element in array: "))
for i in range(0,n):
    print("Enter", i,"th element")
    x=int(input())
    arr=arr+[x]
print(arr)
print("Performing bubblesort on array: ")
BubbleSort(arr)
print("Array after performing bubblesort: ",arr)

