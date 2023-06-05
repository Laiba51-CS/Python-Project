class songs:
    name = ""
    album = ""
    genre = ""
    artists = ""
    Likes = 0
    TimesPlayed = 0
    duration = 0
    Comments = 0
    year = 0.0

    def __init__(self, name, album, genre, artists, Likes, TimesPlayed, duration, Comments, year):
        self.name = name
        self.album = album
        self.genre = genre
        self.artists = artists
        self.Likes = Likes
        self.TimesPlayed = TimesPlayed
        self.duration = duration
        self.Comments = Comments
        self.year = year

    def init(self, name):
        self.name = name

    def init(self, album):
        self.album = album

    def init(self, genre):
        self.genre = genre

    def init(self, artists):
        self.artists = artists

    def init(self, likes):
        self.likes = likes

    def init(self, TimesPlayed):
        self.TimesPlayed = TimesPlayed

    def init(self, duration):
        self.duration = duration

    def init(self, Comments):
        self.Comments = Comments

    def init(self, year):
        self.year = year
