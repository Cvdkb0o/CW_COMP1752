class LibraryItem:
    """
    Represents a music track with attributes like name, artist, rating, and play count.
    """

    def __init__(self, name, artist, rating=0):
        self.name = name                  # Track name
        self.artist = artist              # Artist name

        # Validate that rating is an integer between 0 and 5
        if not isinstance(rating, int) or not (0 <= rating <= 5):
            raise ValueError("Rating must be an integer between 0 and 5.")
        self.rating = rating              # Track rating (0 to 5)
        self.play_count = 0              # Number of times the track has been played

    def info(self):
        """
        Returns a formatted string with track name, artist, and star rating.
        """
        return f"{self.name} - {self.artist} {self.stars()}"

    def stars(self):
        """
        Returns a string of asterisks representing the track's rating.
        For example, rating 3 returns "***"
        """
        return "*" * self.rating
