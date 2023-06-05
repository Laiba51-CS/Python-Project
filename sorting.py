import SongBL
import SongsDL

def SelectionSort(mode,array):
    if mode=="Ascending":
        for i in range(0,len(array)):
            min_index = i
            j=i+1
            for j in range(i+1,len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            (SongsDL.songsList[i], SongsDL.songsList[min_index]) = (SongsDL.songsList[min_index], SongsDL.songsList[i])
        return array 
    if mode=="Descending":
        for i in range(0,len(array)):
            min_index = i
            j=i+1
            for j in range(i+1,len(array)):
                if array[j] > array[min_index]:
                    min_index = j
            (SongsDL.songsList[i], SongsDL.songsList[min_index]) = (SongsDL.songsList[min_index], SongsDL.songsList[i])
        return array 


SongsDL.Loaddata()
allLists = SongsDL.sepratelists()
SelectionSort("Ascending",allLists[4])
print("--------------------------------------")

for s in SongsDL.songsList:
    print(s.name,s.album,s.genre,s.Likes, s.duration, s.Comments, s.year)
