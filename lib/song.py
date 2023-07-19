class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genre_count(cls):
        for genre in cls.genres:
            cls.genre_count[genre] = cls.genres.count(genre)

    @classmethod
    def add_to_artist_count(cls):
        for artist in cls.artists:
            cls.artist_count[artist] = cls.artists.count(artist)



    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count()
        Song.add_to_artist_count()
        