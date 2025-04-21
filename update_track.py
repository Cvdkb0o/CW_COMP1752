import tkinter as tk
from tkinter import messagebox
import track_library as lib  # Import custom library for track management

# Load the track data from file
lib.load_library()

class UpdateTrack:
    """Class to build and manage the Update Track GUI window."""

    def __init__(self, window):
        # === Configure the main window ===
        window.title("Update Track")         # Set the title of the window
        window.geometry("")                  # Use default size (auto-resize)
        window.configure(bg="gray")          # Set the background color

        # === INPUT SECTION ===

        # Label and entry for track number input
        tk.Label(window, text="Enter Track Number:", bg="lightgray").grid(
            row=0, column=0, padx=20, pady=(20, 5), sticky="w"
        )
        self.track_number_entry = tk.Entry(window, width=30)
        self.track_number_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Label and entry for new rating input
        tk.Label(window, text="Enter New Rating (1–5):", bg="lightgray").grid(
            row=1, column=0, padx=20, pady=5, sticky="w"
        )
        self.rating_entry = tk.Entry(window, width=30)
        self.rating_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # === ACTION BUTTON ===

        # Button to trigger the update action
        self.update_button = tk.Button(
            window,
            text="Update Track",
            command=self.update_track,
            bg="lightgreen",
            width=20
        )
        self.update_button.grid(row=2, column=1, padx=10, pady=20)

    def update_track(self):
        """
        Validates inputs and updates the rating for a track in the library.
        Provides user feedback via message boxes.
        """
        track_number = self.track_number_entry.get().strip()
        new_rating = self.rating_entry.get().strip()

        # Validate that the track number is provided
        if not track_number:
            messagebox.showerror("Error", "Empty track number input.")
            return

        # Validate that the rating is provided
        if not new_rating:
            messagebox.showerror("Error", "Empty rating input.")
            return

        # Check if track number is a valid positive integer
        if not track_number.isdigit() or int(track_number) <= 0:
            messagebox.showerror("Error", "Track number must be a positive integer.")
            return

        # Format track number to 2-digit string
        track_number = track_number.zfill(2)

        # Validate and convert rating to integer (must be between 1 and 5)
        try:
            new_rating = int(new_rating)
            if not 1 <= new_rating <= 5:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Rating must be an integer between 1 and 5.")
            return

        # Check if the track exists in the library
        if track_number in lib.library:
            track = lib.library[track_number]
            success = lib.update_track_details(track_number, new_rating=new_rating)

            if success:
                play_count = lib.get_play_count(track_number)
                messagebox.showinfo(
                    "Success",
                    f"Track: {track.info()}\nNew Rating: {new_rating}\nPlay Count: {play_count}"
                )
            else:
                messagebox.showerror("Error", "Failed to update the track.")
        else:
            messagebox.showerror("Error", "Track not found.")

        # Clear the input fields after action
        self.clear_entries()

    def clear_entries(self):
        """Clears both input fields."""
        self.track_number_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)


# Run this window as a standalone application (for testing/debugging)
if __name__ == "__main__":
    window = tk.Tk()
    UpdateTrack(window)
    window.mainloop()
