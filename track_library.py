from library_item import LibraryItem  # Import the LibraryItem class that represents individual track data
import csv  # Module for reading and writing CSV files

CSV_FILE = "data.csv"  # Path to the CSV file storing the track data
library = {}  # Dictionary to store track items with track_number as keys

# Load track data from the CSV file into the library dictionary
def load_library():
    with open(CSV_FILE, mode="r", newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            track_number = row["track_number"]
            name = row["name"]
            artist = row["artist"]
            rating = int(row["rating"])
            play_count = int(row["play_count"])

            # Create a LibraryItem object and add it to the dictionary
            item = LibraryItem(name, artist, rating)
            item.play_count = play_count
            library[track_number] = item

# Save the current state of the library dictionary to the CSV file
def save_library():
    with open(CSV_FILE, mode="w", newline='', encoding="utf-8") as file:
        fieldnames = ["track_number", "name", "artist", "rating", "play_count"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for track_number, item in library.items():
            writer.writerow({
                "track_number": track_number,
                "name": item.name,
                "artist": item.artist,
                "rating": item.rating,
                "play_count": item.play_count
            })

# Return a formatted string of all track entries in the library
def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()} (Plays: {item.play_count})\n"
    return output

# Retrieve the name of a track by its track number
def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None  # Return None if the key does not exist

# Retrieve the artist of a track by its track number
def get_artist(key):
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None

# Retrieve the rating of a track by its track number
def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1  # Return -1 to indicate that the key does not exist

# Update the rating of a specific track
def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return  # Do nothing if the key does not exist

# Retrieve the play count of a track by its track number
def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

# Increment the play count of a specific track and save changes to the CSV
def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
        save_library()  # Persist the update
    except KeyError:
        return

# Update details of a track, such as its rating
def update_track_details(track_number, new_rating=None):
    if track_number in library:
        if new_rating is not None:
            # Validate that rating is an integer between 0 and 5
            if not isinstance(new_rating, int) or not (0 <= new_rating <= 5):
                return False
            library[track_number].rating = new_rating
        save_library()  # Save updates after modification
        return True
    return False  # Return False if the track does not exist
