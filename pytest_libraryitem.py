import pytest
from library_item import LibraryItem

# --- Constructor & Attribute Tests ---
def test_create_valid_item():
    item = LibraryItem("Song A", "Artist A", 5)
    assert item.name == "Song A"
    assert item.artist == "Artist A"
    assert item.rating == 5
    assert item.play_count == 0

def test_default_rating():
    item = LibraryItem("Song B", "Artist B")
    assert item.rating == 0  # Mặc định là 0 sao
    assert item.stars() == ""

def test_invalid_rating_string():
    with pytest.raises(ValueError):
        LibraryItem("Song C", "Artist C", "five")

def test_invalid_rating_too_high():
    with pytest.raises(ValueError):
        LibraryItem("Song D", "Artist D", 6)

def test_invalid_rating_too_low():
    with pytest.raises(ValueError):
        LibraryItem("Song E", "Artist E", -1)

def test_invalid_rating_float():
    with pytest.raises(ValueError):
        LibraryItem("Song F", "Artist F", 3.5)

# --- stars() Method Test ---
def test_stars_method():
    item = LibraryItem("Song G", "Artist G", 4)
    assert item.stars() == "****"

def test_stars_zero():
    item = LibraryItem("Song H", "Artist H", 0)
    assert item.stars() == ""

# --- info() Method Test ---
def test_info_format():
    item = LibraryItem("Song I", "Artist I", 3)
    assert item.info() == "Song I - Artist I ***"

def test_info_no_stars():
    item = LibraryItem("Song J", "Artist J", 0)
    assert item.info() == "Song J - Artist J "

# --- Play Count Test ---
def test_play_count_initial():
    item = LibraryItem("Song K", "Artist K", 1)
    assert item.play_count == 0
