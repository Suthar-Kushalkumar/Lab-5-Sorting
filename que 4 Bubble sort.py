#Best case for bubble sort
def BubbleSort(array): 
  l=len(array)

  for i in range(l-1) :
    for j in range(l-1-i) :
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

import time
print("Best case in bubble sort are when it counts swaps and ends when swaps=0 or when array is in ascending order.")
print("Example of best case for bubble sort for ascending ordered array: [1 2 3 4] ")
begin=time.time()
BubbleSort([1,2,3,4])
end=time.time()
print("Array after performing bubblesort: [1 2 3 4] ")
print("Time taken by this example: ",end-begin)

print("\nExample of best case for bubble sort for when it count swaps: [2 1 3 4] ")
begin1=time.time()
BubbleSort([2,1,3,4])
end1=time.time()
print("Array after performing bubblesort: [1 2 3 4] ")
print("Time taken by this example: ",end1-begin1)

#Worst case for bubble sort
def BubbleSortWs(array): 
  l=len(array)

  for i in range(l-1) :
    for j in range(l-1-i) :
      print("Comparing",array[j],array[j+1])
      if array[j] > array[j + 1] :
          print("Swapping",array[j],array[j+1])
          temp = array[j]
          array[j] = array[j + 1]
          array[j + 1] = temp
    print("End of pass:",i+1)
    print("\n")

  return(array)
print("\nWorst case in bubble sort are when it doesn't count swaps and campare everytime or when array is in descending order.")
print("Example of worst case for bubble sort for descending order array: [4 3 2 1] ")
begin2=time.time()
BubbleSortWs([4,3,2,1])
end2=time.time()
print("Array after performing bubblesort: [1 2 3 4] ")
print("Time taken by this example: ",end2-begin2)

print("\nExample of worst case for bubble sort for when it doesn't count swaps: [2 1 3 4] ")
begin3=time.time()
BubbleSortWs([2,1,3,4])
end3=time.time()
print("Array after performing bubblesort: [1 2 3 4] ")
print("Time taken by this example: ",end3-begin3)

