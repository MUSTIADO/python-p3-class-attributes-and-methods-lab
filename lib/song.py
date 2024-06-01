class Song:
    # Class attributes
    count = 0           # Total count of songs
    genres = []         # List to store unique genres
    artists = []        # List to store unique artists
    genre_count = {}    # Dictionary to store count of songs per genre
    artist_count = {}   # Dictionary to store count of songs per artist
    
    # Constructor method
    def __init__(self, name, artist, genre) -> None:
        # Initialize instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update class attributes
        self.add_song_to_count()        # Increment total count of songs
        self.add_to_genres(genre)       # Add genre to the list of genres
        self.add_to_artists(artist)     # Add artist to the list of artists
        self.add_to_genre_count(genre)  # Update count of songs per genre
        self.add_to_artist_count(artist)# Update count of songs per artist

    # Class method to increment total count of songs
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    # Class method to add genre to the list of genres
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    # Class method to add artist to the list of artists
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    # Class method to update count of songs per genre
    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    # Class method to update count of songs per artist
    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
