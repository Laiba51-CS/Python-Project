import csv 
import SongBL
import pandas as pd


@staticmethod
def Loaddata():
    df = pd.read_csv('Songs1.csv')
    #df = df.astype({"Comments": 'str', "year": 'str', "name": 'str', "album": 'str', "genre": 'str', "artists": 'str', "Likes": 'str', "Times Played": 'str'})
    #print(df.dtypes)
    Name = df['name'].values.tolist()
    Album = df['album'].values.tolist()
    Genre = df[' genre'].values.tolist()
    Artists = df['artists'].values.tolist()
    Likes = df['Likes'].values.tolist()
    PlayedTime = df['Times Played'].values.tolist()
    Comments = df['Comments'].values.tolist()
    Duration = df['duration'].values.tolist()
    Year = df['year'].values.tolist()
    
    for i in range(len(Name)):
        s = SongBL.songs(Name[i], Album[i], Genre[i], Artists[i], Likes[i], PlayedTime[i], Duration[i], Comments[i], Year[i])
        #print(s.name, s.album, s.genre, s.artists, s.Likes, s.TimesPlayed, s.duration, s.Comments, s.year)
        songsList.append(s)

    #songsList[0:50]

def addSong(name, album, genre, artists, Likes, TimesPlayed, duration, Comments, year):
    s = SongBL.songs(name, album, genre, artists, Likes, TimesPlayed, duration, Comments, year)
    songsList.append(s)


def deleteSong(s):
    songsList.remove(s)


def AddListintofile():
    with open('Songs1.csv', 'w') as f:
        csv_writer = csv.writer(f)
        for song in songsList:
            data= [song.name, song.album, song.genre, song.artists, song.Likes, song.TimesPlayed, song.duration, song.Comments, song.year]
            #csv_writer.writerow(data)

# def Addintofile(song):
#     with open('Songs1.csv', 'w') as f:
#         csv_writer = csv.writer(f)
#         data= [song.name, song.album, song.genre, song.artists, song.Likes, song.TimesPlayed, song.duration, song.Comments, song.year]
#         csv_writer.writerow(data)

def sepratelists():
    df = pd.read_csv('songsData.csv')
    Name = df['name'].values.tolist()
    Album = df['album'].values.tolist()
    Genre = df['genre'].values.tolist()
    Artists = df['artists'].values.tolist()
    Likes = df['Likes'].values.tolist()
    PlayedTime = df['Times Played'].values.tolist()
    Comments = df['Comments'].values.tolist()
    Duration = df['duration'].values.tolist()
    Year = df['year'].values.tolist()
    # Name[0:50]
    # Album[0:50]
    # Genre[0:50]
    # Artists[0:50]
    # Likes[0:50]
    # PlayedTime[0:50]
    # Duration[0:50]
    # Comments[0:50]
    # Year[0:50]
    return [Name, Album, Genre, Artists, Likes, PlayedTime, Duration, Comments, Year]


songsList = []



