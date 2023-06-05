import SongBL
import SongsDL
import math


def linearSearch(array, key):
    list1 = []
    for i in range(len(array)):

        if array[i] == key:
            print(i)
            list1.append( SongsDL.songsList[i] )
    return list1

def binarySearch(list_num, first, last, search,self):
        if last >= first:
            
            mid = (first + last) // 2
            mid_element = list_num[mid]

        if mid_element == search:
            return f"{mid_element} occurs in position {mid}"

        elif mid_element > search:
            position = mid - 1
            return binarySearch(list_num, first, position, search)

        elif mid_element < search:
            position = mid + 1
            return binarySearch(list_num, position, last, search)

def jumpSearch(arr,search):
    ListJ = []
    low = 0
    interval = int(math.sqrt(len(arr)))
    for i in range(0,len(arr),interval):
        if arr[i] < search:
            low = i
        elif arr[i] == search:
            ListJ.append(SongsDL.songsList[i])
        else:
            break
    c=low
    for j in range(arr[low]):
        if arr[j]==search:
            ListJ.append(SongsDL.songsList[j])
        c+=1
    return ListJ


#SongsDL.Loaddata()
#allLists = SongsDL.sepratelists()
#arr = linearSearcah(allLists[4])
