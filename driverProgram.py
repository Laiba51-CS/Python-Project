import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import time
import csv
import pandas as pd
import SongsDL 
import SongBL
import Searching
import sortFuncs
# from update import Ui_UpdateWindow
# from view import Ui_ViewWindow
# from add import Ui_AddWindow


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen,self).__init__()
        loadUi("splash.ui",self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        pixmap = QPixmap("pt1.png")
        self.setPixmap(pixmap)
    def progress(self):
        for i in range(100):
            time.sleep(0.01)
            self.progressBar.setValue(i)
            self.progressBar.setTextVisible(False)


class addWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        loadUi("add.ui",self)
        self.setWindowTitle("ALA Music")
        self.setWindowIcon(QtGui.QIcon('alaI.ico'))
        self.logoLabel.setPixmap(QtGui.QPixmap("ala2.png"))
        self.addButton.setIcon(QtGui.QIcon('add1.ico'))

        self.addButton.clicked.connect(self.addSong) 

    def addSong(self):
        name = self.NameLine.text()
        album = self.AlbumLine.text()
        genre = self.GenreLine.text()
        artists = self.ArtistLine.text()
        Likes = self.LikesLine.text()
        TimesPlayed = self.ViewsLine.text()
        duration = self.DurationLine.text()
        Comments = self.CommentsLine.text()
        year = self.YearLine.text()
        s = SongBL.songs(name, album, genre, artists, Likes, TimesPlayed, duration, Comments, year)
        SongsDL.songsList.append(s)
        QMessageBox.question(self, 'Message', "Record Added Successfully.", QMessageBox.Ok)


class viewWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        loadUi("view.ui",self)
        self.setWindowTitle("ALA Music")
        self.setWindowIcon(QtGui.QIcon('alaI.ico'))
        self.logoLabel.setPixmap(QtGui.QPixmap("ala2.png"))
        self.previousButton.setIcon(QtGui.QIcon('previous.ico'))
        self.nextButton.setIcon(QtGui.QIcon('next.ico'))
        self.nameLine.setReadOnly = True
        self.albumLine.setReadOnly = True
        self.artistLine.setReadOnly = True
        self.genreLine.setReadOnly = True
        self.likesLine.setReadOnly = True
        self.viewsLine.setReadOnly = True
        self.durationLine.setReadOnly = True
        self.commentsLine.setReadOnly = True
        self.yearLine.setReadOnly = True
        record = 500
        #self.songInfo(record)
        # if(self.previousButton.clicked):
        #     record = record - 1
        #     self.previousButton.clicked.connect(self.songInfo(record))
        # elif(self.nextButton.clicked):
        #     record = record + 1
        #     #self.songInfo(record)
        #     self.nextButton.clicked.connect(self.songInfo(record))

        self.previousButton.clicked.connect(self.songInfo(record))
        self.nextButton.clicked.connect(self.songInfo(record))

        #self.songInfo

    def songInfo(self,record):
        o = input("Check: ")
        # record = 500
        # if(self.previousButton.clicked == True):
        #     record = record - 1
        # elif(self.nextButton.clicked == True):
        #     record = record + 1
        print(SongsDL.songsList[record].name)
        
        self.nameLine.setText = SongsDL.songsList[record].name
        self.albumLine.setText = SongsDL.songsList[record].album
        self.artistLine.setText = SongsDL.songsList[record].artists
        self.genreLine.setText = SongsDL.songsList[record].genre
        self.likesLine.setText = SongsDL.songsList[record].Likes
        self.viewsLine.setText = SongsDL.songsList[record].TimesPlayed
        self.durationLine.setText = SongsDL.songsList[record].duration
        self.commentsLine.setText = SongsDL.songsList[record].Comments
        self.yearLine.setText = SongsDL.songsList[record].year


        # self.nameLine.setText(SongsDL.songsList[record].name)
        # self.albumLine.setText(SongsDL.songsList[record].album)
        # self.artistLine.setText(SongsDL.songsList[record].artists)
        # self.genreLine.setText(SongsDL.songsList[record].genre)
        # self.likesLine.setText(SongsDL.songsList[record].Likes)
        # self.viewsLine.setText(SongsDL.songsList[record].TimesPlayed)
        # self.durationLine.setText(SongsDL.songsList[record].duration)
        # self.commentsLine.setText(SongsDL.songsList[record].Comments)
        # self.yearLine.setText(SongsDL.songsList[record].year)


class updateWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        loadUi("update.ui",self)
        self.setWindowTitle("ALA Music")
        self.setWindowIcon(QtGui.QIcon('alaI.ico'))
        self.logoLabel.setPixmap(QtGui.QPixmap("ala2.png"))
        self.updateButton.setIcon(QtGui.QIcon('update.ico'))


class mainWindow(QMainWindow):
    def __init__(self):
        SongsDL.Loaddata()
        super(QMainWindow,self).__init__()
        loadUi("mwCOPY.ui",self)
        self.setWindowTitle("ALA Music")
        self.setWindowIcon(QtGui.QIcon('alaI.ico'))
        self.loadDataInTable(SongsDL.songsList)
        self.logoLabel.setPixmap(QtGui.QPixmap("ala2.png"))
        self.songsTable.setHorizontalHeaderLabels(['Name','Album','Genre','Artists','Likes','Views','Duration','Comment','Year'])
        self.addButton.setIcon(QtGui.QIcon('add1.ico'))
        self.deleteButton.setIcon(QtGui.QIcon('del.ico'))
        self.updateButton.setIcon(QtGui.QIcon('update.ico'))
        self.viewButton.setIcon(QtGui.QIcon('view.ico'))
        
        self.sortMethod.setReadOnly = True
        self.sortAttribute.setReadOnly = True
        self.sortMode.setReadOnly = True
        self.searchMethod.setReadOnly = True
        
        self.sortMethod.setCurrentText('Select Method')
        self.sortAttribute.setCurrentText('Select Attribute')
        self.sortMode.setCurrentText('Select Mode')
        self.searchMethod.setCurrentText('Select Method')

        self.updateButton.clicked.connect(self.update)   
        self.viewButton.clicked.connect(self.view)   
        self.addButton.clicked.connect(self.add)
        self.deleteButton.clicked.connect(self.deleteSong)    

        # self.updateButton.clicked.connect(self.updateWin)   
        # self.viewButton.clicked.connect(self.viewWin)   
        # self.addButton.clicked.connect(self.addWin)   

        self.searchButton.clicked.connect(self.searchingWith)
        self.reloadButton.clicked.connect(self.back)

        self.sortButton.clicked.connect(self.sortedTable)
        self.reloadButton.clicked.connect(self.back)

        ####---------------------------------------------####

    def sortedTable(self):
        Arr = []
        Name, Album, Genre, Artists, Likes, playedtime, Duration, Comments, Year = SongsDL.sepratelists()
        Sort_BY = self.sortAttribute.currentText()
        if Sort_BY=="Name":
                Arr= Name
        if Sort_BY=="Album":
                Arr= Album
        if Sort_BY=="Genre":
                Arr=  Genre
        if Sort_BY=="Artists":
                Arr= Artists
        if Sort_BY=="Likes":
                Arr= Likes
        if Sort_BY=="Views":
                Arr=  playedtime
        if Sort_BY=="Duration":
                Arr=  Duration
        if Sort_BY=="Comments":
                Arr=  Comments
        if Sort_BY=="Year":
                Arr=  Year
        Sorting_Method=self.sortMethod.currentText()
        Sort_Order=self.sortMode.currentText()
        if Sorting_Method=="Bubble Sort":
            if Sort_Order=="Ascending":
                sortFuncs.BubbleSort("Ascending",Arr)
            else:
                sortFuncs.BubbleSort("Descending",Arr)
        elif Sorting_Method=="Selection Sort":
            if Sort_Order=="Ascending":
                sortFuncs.SelectionSort("Ascending",Arr)
            else:
                sortFuncs.SelectionSort("Descending",Arr)
        elif Sorting_Method=="Gnome Sort":
            if Sort_Order=="Ascending":
                sortFuncs.gnomeSort("Ascending",Arr)
            else:
                sortFuncs.gnomeSort("Descending",Arr)
        elif Sorting_Method=="Shell Sort":
            if Sort_Order=="Ascending":
                sortFuncs.shellSort("Ascending",Arr)
            else:
                sortFuncs.shellSort("Descending",Arr)
        elif Sorting_Method=="Insertion Sort":
            if Sort_Order=="Ascending":
                sortFuncs.InsertionSort("Ascending",Arr)
            else:
                sortFuncs.InsertionSort("Descending",Arr)
        elif Sorting_Method=="Radix Sort":
            if Sort_Order=="Ascending":
                sortFuncs.radixSort("Ascending",Arr)
            else:
                sortFuncs.radixSort("Descending",Arr)
        elif Sorting_Method=="Merge Sort":
            if Sort_Order=="Ascending":
                sortFuncs.MergeSort("Ascending",Arr)
            else:
                sortFuncs.MergeSort("Descending",Arr)
        elif Sorting_Method=="Hybrid Sort":
            if Sort_Order=="Ascending":
                sortFuncs.HybridMergeSort("Ascending",Arr)
            else:
                sortFuncs.HybridMergeSort("Descending",Arr)
        elif Sorting_Method=="Quick Sort":
            if Sort_Order=="Ascending":
                sortFuncs.quickSort("Ascending",Arr)
            else:
                sortFuncs.quickSort("Descending",Arr)
        elif Sorting_Method=="Counting Sort":
            if Sort_Order=="Ascending":
                sortFuncs.countingSort("Ascending",Arr)
            else:
                sortFuncs.countingSort("Descending",Arr)
        elif Sorting_Method=="Bucket Sort":
            if Sort_Order=="Ascending":
                sortFuncs.shellSort("Ascending",Arr)
            else:
                sortFuncs.shellSort("Descending",Arr)
        elif Sorting_Method=="Heap Sort":
            if Sort_Order=="Ascending":
                sortFuncs.combSort("Ascending",Arr)
            else:
                sortFuncs.combSort("Descending",Arr)
        elif Sorting_Method=="Comb Sort":
            if Sort_Order=="Ascending":
                sortFuncs.combSort("Ascending",Arr)
            else:
                sortFuncs.combSort("Descending",Arr)
        self.loadDataInTable(SongsDL.songsList)
       ####---------------------------------------------####


    def back(self):
        self.loadDataInTable(SongsDL.songsList)

    def searchingWith(self):
        Ar = []
        search = self.textToSearch.text()
        allLists = SongsDL.sepratelists()
        fun = self.searchMethod.currentText()
        att = self.searchAttribute.currentText()
        if (att == "Name"):
            Ar = allLists[0]
        elif (att == "Album"):
            Ar = allLists[1]
        elif (att == "Genre"):
            Ar = allLists[2]
        elif (att == "Artists"):
            Ar = allLists[3]
        elif (att == "Likes"):
            Ar = allLists[4]
        elif (att == "Views"):
            Ar = allLists[5]
        elif (att == "Duration"):
            Ar = allLists[6]
        elif (att == "Comments"):
            Ar = allLists[7]
        elif (att == "Year"):
            Ar = allLists[8]

        if fun == "Linear Serach":
            arr = Searching.linearSearch(Ar, search)
            self.loadDataInTable(arr)
        elif fun == "Binary Search":
            arr = Searching.linearSearch(Ar, search)
            self.loadDataInTable(arr)
        elif fun == "Jump Search":
            arr = Searching.linearSearch(Ar, search)
            self.loadDataInTable(arr)

    def loadDataInTable(self, array):
        row = 0
        self.songsTable.setRowCount(len(array))
        for song in array:
            self.songsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(str(song.name)))
            self.songsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(song.album)))
            self.songsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(song.genre)))
            self.songsTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(song.artists)))
            self.songsTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(song.Likes)))
            self.songsTable.setItem(row, 5, QtWidgets.QTableWidgetItem(str(song.TimesPlayed)))
            self.songsTable.setItem(row, 6, QtWidgets.QTableWidgetItem(str(song.duration)))
            self.songsTable.setItem(row, 7, QtWidgets.QTableWidgetItem(str(song.Comments)))
            self.songsTable.setItem(row, 8, QtWidgets.QTableWidgetItem(str(song.year)))
            row += 1

    def deleteSong(self):
        i = self.songsTable.currentRow()
        SongsDL.deleteSong(SongsDL.songsList[i-1])
        self.songsTable.removeRow(i)
        QMessageBox.question(self, 'Message', "Record Deleted Successfully.", QMessageBox.Ok)

    def update(self):
        self.Window = updateWindow()
        self.Window.show()

    def view(self):
        self.Window = viewWindow()
        self.Window.show()

    def add(self):
        self.Window = addWindow()
        self.Window.show()

    # def updateWin(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_UpdateWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()

    # def viewWin(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_ViewWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
  
    # def addWin(self):
    #         self.window = QtWidgets.QMainWindow()
    #         self.ui = Ui_AddWindow()
    #         self.ui.setupUi(self.window)
    #         self.window.show()




if __name__ == '__main__':
    # to make mainWindow size bigger
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    splash.progress()
    window = mainWindow()
    splash.finish(window)
    window.loadDataInTable(SongsDL.songsList)
    window.show()
    SongsDL.AddListintofile()
    sys.exit(app.exec_())

