import sqlite3
####### define table name as const
ARTISTS_TABLE = "Music_Artists"
GENRES_TABLE = "Genres"
CITIES_TABLE = "Cities"

####### open connection and set cursor
connection = sqlite3.connect("music_artists.db")
cursor = connection.cursor()

# create database tables
cursor.execute(f"CREATE TABLE {ARTISTS_TABLE} (artist TEXT, genre TEXT, number_recordings INTEGER)")
cursor.execute(f"CREATE TABLE {GENRES_TABLE} (genre TEXT, city TEXT)")
cursor.execute(f"CREATE TABLE {CITIES_TABLE} (city TEXT, state TEXT, zip_code INTEGER, population INTEGER)")

####### load artist data
artist_data = [
    ('Miley', 'Rock', 14),
    ('Dolly', 'Country', 123),
    ('Eminem', 'HipHop', 98),
    ('Brittany', 'Rock', 37)
]
cursor.executemany(f"INSERT INTO {ARTISTS_TABLE} VALUES (?, ?, ?)", artist_data)

# load genre data
genre_data = [
    ('Rock', 'Los Angeles'),
    ('Hippie', 'Eugene'),
    ('Opera', 'Florence')
]
cursor.executemany(f"INSERT INTO {GENRES_TABLE} VALUES (?, ?)", genre_data)

# load city data
city_data = [
    ('Los Angeles', 'CA', '66666', 10000000),
    ('Eugene', 'OR', '55555', 80000),
    ('Nashville', 'TN', '11111', 1500000)
]
cursor.executemany(f"INSERT INTO {CITIES_TABLE} VALUES (?, ?, ?, ?)", city_data)

# commit cursor changes
connection.commit()

####### print out artists and genre data
print("ARTIST DATA: ")
for row in cursor.execute(f"SELECT * FROM {ARTISTS_TABLE}"):
    print(row)

print("GENRE DATA: ")
for row in cursor.execute(f"SELECT * FROM {GENRES_TABLE}"):
    print(row)

####### print out matching artist genres
print("ARTISTS WITH GENRE IN GENRES TABLE:")
# a = artist table, g = genres table
query = f"SELECT a.artist FROM {ARTISTS_TABLE} a INNER JOIN {GENRES_TABLE} g ON a.genre = g.genre"
for row in cursor.execute(query):
    # print out only the name
    print(row[0])

####### take artist input for query
artist_input = input("\nEnter artist name: ")

# query for artist
cursor.execute(f"SELECT * FROM {ARTISTS_TABLE} WHERE artist = ?", (artist_input,))
artist_query_input = cursor.fetchone()

print('\n')

# checks artist query and returns string based on result
def CheckArtistQuery(artist_query):
    # if artist_query is not valid, artist does not exist
    if not artist_query:
        return "Artist not found"

    # set variables equal to artist_query data
    artist_name, genre, recordings = artist_query
    cursor.execute(f"SELECT city FROM {GENRES_TABLE} WHERE genre = ?", (genre,))
    genre_row = cursor.fetchone()

    # if not in genre row, then there is no valid index in the genres table
    if not genre_row:
        return f"{genre} artist {artist_name} has {recordings} recordings and is popular everywhere"

    # get city from genre row, then get city info
    city = genre_row[0]
    cursor.execute(f"SELECT population FROM {CITIES_TABLE} WHERE city = ?", (city,))
    city_info = cursor.fetchone()

    # print full info
    return f"{genre} artist {artist_name} has {recordings} recordings and is most popular in {city} with a population of {city_info[0]}"

print(CheckArtistQuery(artist_query_input))

connection.close()