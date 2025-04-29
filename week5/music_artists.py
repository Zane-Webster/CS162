import sqlite3

# define table name as const
TABLE_NAME = "Music_Artists"

# open connection and set cursor
connection = sqlite3.connect("week5/music_artists.db")
cursor = connection.cursor()

# create database if it does not exist
cursor.execute(f"CREATE TABLE {TABLE_NAME} (artist TEXT, genre TEXT, number_recordings INTEGER)")

# artist data
artist_data = [
    ('Miley', 'Rock', 14),
    ('Dolly', 'Country', 123),
    ('Eminem', 'HipHop', 98),
    ('Brittany', 'Rock', 37)
]

# insert artist data into database
cursor.executemany(f"INSERT INTO {TABLE_NAME} VALUES (?, ?, ?)", artist_data)

# commit cursor changes
connection.commit()

# print out each row
print("ALL DATA: ")
for row in cursor.execute(f"SELECT * FROM {TABLE_NAME}"):
    print(row)

# print out only the rock artists
cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE genre = 'Rock'")

print("\n ROCK ARTISTS: ")
for row in cursor.fetchall():
    print(row)

connection.close()