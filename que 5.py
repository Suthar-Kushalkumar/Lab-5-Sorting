def mergeSortedSubseq( theSeq, left, right, end, tmpArray ):
  a=left
  b=right
  m=0

  while a < right and b < end:
    if theSeq[a] < theSeq[b] :
      tmpArray[m] = theSeq[a]
      a += 1
    else :
      tmpArray[m] = theSeq[b]
      b += 1
    m += 1
  while a < right :
    tmpArray[m] = theSeq[a]
    a += 1
    m += 1
  while b < end:
    tmpArray[m] = theSeq[b]
    b += 1
    m += 1
  for i in range(end-left):
    theSeq[i+left] = tmpArray[i]

def recMergeSort( theSeq, first, last, tmpArray ):
  if first == last :
    return;
  else :
    mid = (first + last) // 2
    print("mid:",mid,theSeq[mid])
  recMergeSort( theSeq, first, mid, tmpArray )
  recMergeSort( theSeq, mid+1, last, tmpArray )
  print("merging",first,mid,"and",mid+1,last)
  mergeSortedSubseq( theSeq, first, mid+1, last+1, tmpArray )

def mergeSort( theSeq ): 
    n = len( theSeq )
    tmpArray = [-1]*n
    recMergeSort( theSeq, 0, n-1, tmpArray )
    return(tmpArray)

arr=[]
n=int(input("Number of element in array: "))
for i in range(0,n):
    print("Enter", i,"th element")
    x=int(input())
    arr=arr+[x]
print(arr)
print("Performing merge sort on array: ")
mergeSort(arr)
print("Array after performing merge sort: ",arr)
