import SongBL
from SongsDL import Loaddata
import SongsDL

# selection sort algorithm


def SelectionSort(mode, array):
    for z in range(0, 9):
        if mode == "Ascending":
            for i in range(0, len(array)):
                min_index = i
                j = i+1
                for j in range(i+1, len(array)):
                    if array[j] < array[min_index]:
                        min_index = j
                (array[i], array[min_index]) = (array[min_index], array[i])
                (SongsDL.songsList[i], SongsDL.songsList[min_index]) = (
                    SongsDL.songsList[min_index], SongsDL.songsList[i])
            return array
        if mode == "Descending":
            for i in range(0, len(array)):
                min_index = i
                j = i+1
                for j in range(i+1, len(array)):
                    if array[j] > array[min_index]:
                        min_index = j
                (array[i], array[min_index]) = (array[min_index], array[i])
                (SongsDL.songsList[i], SongsDL.songsList[min_index]) = (
                    SongsDL.songsList[min_index], SongsDL.songsList[i])
            return array

# bubble sort algorithm


def BubbleSort(mode, array):
    if mode == "Ascending":
        for i in range(0, len(array)):
            j = i+1
            for j in range(0, len(array)):
                if (array[i] < array[j]):
                    tempo = array[i]
                    array[i] = array[j]
                    array[j] = tempo
                    temp = SongsDL.songsList[i]
                    SongsDL.songsList[i] = SongsDL.songsList[j]
                    SongsDL.songsList[j] = temp
        return array
    if mode == "Descending":
        for i in range(0, len(array)):
            j = i+1
            for j in range(0, len(array)):
                if (array[i] > array[j]):
                    tempo = array[i]
                    array[i] = array[j]
                    array[j] = tempo
                    temp = SongsDL.songsList[i]
                    SongsDL.songsList[i] = SongsDL.songsList[j]
                    SongsDL.songsList[j] = temp
        return array

# Gnome sort algorithm


def gnomeSort(mode, arr):
    if mode == "Ascending":
        index = 0
        while index < len(arr):
            if index == 0:
                index = index + 1
            if arr[index] >= arr[index - 1]:
                index = index + 1
            else:
                arr[index], arr[index-1] = arr[index-1], arr[index]
                SongsDL.songsList[index], SongsDL.songsList[index -
                                                                1] = SongsDL.songsList[index-1], SongsDL.songsList[index]
                index = index - 1

        return arr
    if mode == "Descending":
        index = 0
        while index < len(arr):
            if index == 0:
                index = index + 1
            if arr[index] <= arr[index - 1]:
                index = index + 1
            else:
                arr[index], arr[index-1] = arr[index-1], arr[index]
                SongsDL.songsList[index], SongsDL.songsList[index -
                                                                1] = SongsDL.songsList[index-1], SongsDL.songsList[index]
                index = index - 1

        return arr


# shell sort algorithm
def shellSort(mode, arr):
    if mode == "Ascending":
        n = len(arr)
        gap = n//2
        while gap > 0:
            j = gap
            while j < n:
                i = j-gap
                while i >= 0:
                    if arr[i+gap] > arr[i]:
                        break
                    else:
                        arr[i+gap], arr[i] = arr[i], arr[i+gap]
                        SongsDL.songsList[i +
                                            gap], SongsDL.songsList[i] = SongsDL.songsList[i], SongsDL.songsList[i+gap]
                    i = i-gap
                j += 1
            gap = gap//2
    if mode == "Descending":
        n = len(arr)
        gap = n//2
        while gap > 0:
            j = gap
            while j < n:
                i = j-gap
                while i >= 0:
                    if arr[i+gap] < arr[i]:
                        break
                    else:
                        arr[i+gap], arr[i] = arr[i], arr[i+gap]
                        SongsDL.songsList[i +
                                            gap], SongsDL.songsList[i] = SongsDL.songsList[i], SongsDL.songsList[i+gap]
                    i = i-gap
                j += 1
            gap = gap//2

# bucket sort algorithm


def bucket_sort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
    buckets = [[] for _ in range(length)]
    buckets1 = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
            buckets1[j].append(SongsDL.songsList[i])
        else:
            buckets[length - 1].append(alist[i])
            buckets1[length - 1].append(SongsDL.songsList[i])
    for i in range(length):
        InsertionSort(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]
    return result


##################################### comb Sort################################
def getNextGap(gap):
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap
def combSort(arr,mode):
    n = len(arr)
    gap = n
   

    swapped = True
    if mode =="Ascending":
      while gap !=1 or swapped == 1:
        gap = getNextGap(gap)
        swapped = False
        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                (SongsDL.songsList[i],SongsDL.songsList[i+gap]) = (SongsDL.songsList[i+gap], SongsDL.songsList[i])

    else:
         while gap !=1 or swapped == 1:
            gap = getNextGap(gap)
            swapped = False
            for i in range(0, n-gap):
                if arr[i] <arr[i + gap]:
                    arr[i], arr[i + gap]=arr[i + gap], arr[i]
                    SongsDL.songsList[i],SongsDL.songsList[i+gap]=SongsDL.songsList[i+gap],SongsDL.songsList[i]
                    swapped = True
    



################################## INSERTION SORT######################################
def InsertionSort(Array,mode):
     def InsertionSort(Array,mode):
        for i in range(0, len(Array)):
            key=Array[i]
            k = SongsDL.songsList[i]

            j=i-1
            if mode=="Ascending":
              while (key< Array[j] and j>=0):
                  Array[j+1]=Array[j]
                  SongsDL.songsList[j+1] = SongsDL.songsList[j]
                  j=j-1
              Array[j+1]=key
              SongsDL.songsList[j+1] = k
            if mode=="Descending":
                while (key> Array[j] and j>=0):
                  Array[j+1]=Array[j]
                
                  SongsDL.songsList[j+1] = SongsDL.songsList[j]
                  j=j-1
                Array[j+1]=key
                SongsDL.songsList[j+1] = SongsDL.songsList[k]



################################  QUICK SORT ######################################################
def quickSort(array, low, high, mode):
    if low < high:
        pi = partition(array, low, high, mode)
        quickSort(array, low, pi - 1, mode)
        quickSort(array, pi + 1, high, mode)

def partition(array, low, high, mode):
    pivot = array[high]

    i = low - 1
    if mode == "Asc":
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1

                (array[i], array[j]) = (array[j], array[i])
                (SongsDL.songsList[i],SongsDL.songsList[j]) = (SongsDL.songsList[j], SongsDL.songsList[i])

    if mode == "Des":
        for j in range(low, high):
            if array[j] >= pivot:
                i = i + 1

                (array[i], array[j]) = (array[j], array[i])
                (SongsDL.songsList[i], SongsDL.songsList[j]) = (SongsDL.songsList[j], SongsDL.songsList[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    (SongsDL.songsList[i + 1], SongsDL.songsList[high]) = (SongsDL.songsList[high], SongsDL.songsList[i + 1])

    return i + 1

#####################   Merge Sort  ################################################

def Merge(arr, p, q, r,mode):
  if mode=="Ascending": 
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1)
    tempL=[0]*(n1)
    R = [0] * (n2)
    tempR=[0]*(n1)
    
    for i in range(0, n1):
        L[i] = arr[p + i]
        tempL[i]=SongsDL.songsList[p+i]
    for j in range(0, n2):
        R[j] = arr[q + 1 + j]
        tempR[j]=SongsDL.songsList[q+1+j]
    i = 0   
    j = 0     
    k = p    
   
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            SongsDL.songsList[k]=tempL[i]
            i += 1
        else:
            arr[k] = R[j]
            SongsDL.songsList[k]=tempR[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        SongsDL.songsList[k]=tempL[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        SongsDL.songsList[k]=tempR[j]
        j += 1
        k += 1
  else:
    n1 = q - p + 1
    n2 = r - q
    L = [0] * (n1)
    tempL=[0]*(n1)
    R = [0] * (n2)
    tempR=[0]*(n1)
    
    for i in range(0, n1):
        L[i] = arr[p + i]
        tempL[i]=SongsDL.songsList[p+i]
    for j in range(0, n2):
        R[j] = arr[q + 1 + j]
        tempR[j]=SongsDL.songsList[q+1+j]
    i = 0   
    j = 0     
    k = p  
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = R[j]
            SongsDL.songsList[k]=tempR[j]
            j += 1
        else:
            arr[k] = L[i]
            SongsDL.songsList[k]=tempL[i]
            i += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        SongsDL.songsList[k]=tempL[i]
        i+=1
        k += 1
    while j < n2:
        arr[k] = R[j]
        SongsDL.songsList[k]=tempR[j]
        j += 1
        k += 1
    if p < q:
        m = p+(q-p)//2
        MergeSort(arr, p, m,mode)
        MergeSort(arr, m+1, q,mode)
        Merge(arr, p, m, q,mode)
def MergeSort(arr, p, q,mode):
    if p < q:
        m = p+(q-p)//2
        MergeSort(arr, p, m,mode)
        MergeSort(arr, m+1, q,mode)
        Merge(arr, p, m, q,mode)
        
   # return arr
    return arr




def HybridMergeSort(A, p, r, mode):
    dif = r - p
    if (p < r and dif > 43):
        q = (p + r)//2
        HybridMergeSort(A, p, r, mode)
        HybridMergeSort(A, p, r, mode)
        Merge(A, p, q, r)
    else:
        InsertionSort(A, mode)


 
################################  Heap Sort ###################################################

def heapify(arr, N, i,mode):
    largest = i  
    largest2=SongsDL.songsList[i]
    l = 2 * i + 1    
    l2=SongsDL.songsList[2 * i + 1]
    r = 2 * i + 2  
    r2=SongsDL.songsList[2 * i + 2]
    if mode=="Ascending":
 
  
      if l < N and arr[largest] < arr[l]:
        largest = l
       
 
      if r < N and arr[largest] < arr[r]:
        largest = r
       
 
      if largest != i:
        #direct swap
        arr[i], arr[largest] = arr[largest], arr[i] 
        SongsDL.songsList[i],SongsDL.songsList[largest2],SongsDL.songsList[i]
        heapify(arr, N, largest,mode)
    else:
         if l < N and arr[largest] > arr[l]:
             largest = l
             
      
         if r < N and arr[largest] > arr[r]:
             largest = r
             
      
         if largest != i:
             #direct swap
             arr[i], arr[largest] = arr[largest], arr[i]
             SongsDL.songsList[i],SongsDL.songsList[largest2],SongsDL.songsList[i]
     
    
def buildmaxheapify(arr,mode):
    N = len(arr)
    for i in range(int(N/2)- 1, -1, -1):
        heapify(arr, N, i,mode)

 
 
def heapSort(arr,mode):
    buildmaxheapify(arr,mode)
    for i in range(len(arr)-1, 0, -1):
        temp=arr[i]
        temp2= SongsDL.songsList[i]
        arr[i]= arr[0] 
        SongsDL.songsList[i]= SongsDL.songsList[0]
        arr[0]=temp  
        SongsDL.songsList[0]=temp2
        heapify(arr, i, 0,mode)


##################################  Radix Sort  ####################################################33
def countingSort(arr, buckets1,mode):
  if mode=="Ascending":
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = int(arr[i] / buckets1)
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = int(arr[i] / buckets1)
        output[count[index % 10] - 1] = arr[i]
        
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
  if mode=="descen ding":
       n = len(arr)
       output = [0] * (n)
       count = [0] * (10)
       for i in range(0, n):
           index = int(arr[i] / buckets1)
           count[index % 10] += 1
       for i in range(1, 10):
           count[i] += count[i - 1]
       i = n - 1
       while i >= 0:
           index = int(arr[i] / buckets1)
           output[count[index % 10] - 1] = arr[i]
           
           count[index % 10] -= 1
           i -= 1
       i = 0
       for i in range(0,len(arr)):
           arr[i] = output[i]
  arr.reverse()
  return arr
         
  
       
def radixSort(arr,mode):
    max1 = max(arr)
    buckets = 1
    while max1 / buckets >= 1:
        countingSort(arr, buckets,mode)
        buckets *= 10
        
