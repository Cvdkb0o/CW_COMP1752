import tkinter as tk
from tkinter import messagebox
import track_library as lib  # Đảm bảo đã có hàm increment_play_count

lib.load_library()

class CreateTrackList:
    def __init__(self, window):
        window.title("Create Track List")  # Set the title of the window
        window.geometry("")
        window.configure(bg="gray")

        # Configure grid to center all widgets
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=1)
        window.columnconfigure(2, weight=1)
        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=1)
        window.rowconfigure(2, weight=1)
        window.rowconfigure(3, weight=1)

        # ==== ADD TRACK SECTION ====
        add_track_label = tk.Label(window, text="Enter Track Number:", bg="lightgray")
        add_track_label.grid(row=0, column=0, padx=20, pady=20, sticky="e")

        self.track_number_entry = tk.Entry(window, width=30)
        self.track_number_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.add_button = tk.Button(window, text="Add to Playlist", command=self.add_to_playlist, bg="lightgreen", width=20)
        self.add_button.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        # ==== PLAYLIST DISPLAY ====
        playlist_label = tk.Label(window, text="   Your Playlist:   ", bg="lightgray")
        playlist_label.grid(row=1, column=0, padx=20, pady=20, sticky="e")

        self.playlist_box = tk.Listbox(window, width=60, height=15, bg="white", selectmode=tk.SINGLE)
        self.playlist_box.grid(row=2, column=0, columnspan=3, padx=20, pady=5, sticky="nsew")

        # ==== PLAY & RESET BUTTONS ====
        self.play_button = tk.Button(window, text="Play Playlist", command=self.play_all, bg="lightblue", width=20)
        self.play_button.grid(row=3, column=1, padx=20, pady=10, sticky="e")

        self.reset_button = tk.Button(window, text="Reset Playlist", command=self.reset_playlist, bg="lightsalmon", width=20)
        self.reset_button.grid(row=3, column=2, padx=20, pady=10, sticky="w")

        # Playlist storage
        self.playlist = []

    def add_to_playlist(self):
        """Add a track to the playlist by track number."""
        raw_input = self.track_number_entry.get().strip()

        if not raw_input:
            messagebox.showerror("Error", "Empty input")
            return

        if not raw_input.isdigit() or int(raw_input) < 0:
            messagebox.showerror("Error", "Must be integer")
            return

        # Convert to two-digit format
        track_number = raw_input.zfill(2)

        # Check existence in library
        if track_number not in lib.library:
            messagebox.showerror("Error", "Not found")
            return

        track = lib.library[track_number]
        track_info = f"{track_number} - {track.info()} (Plays: {track.play_count})"

        if track_info in self.playlist:
            messagebox.showerror("Error", "This track is already in the playlist.")
            return

        self.playlist.append(track_info)
        self.update_playlist_display()


    def update_playlist_display(self):
        """Update the playlist display in the listbox."""
        self.playlist_box.delete(0, tk.END)
        for track in self.playlist:
            self.playlist_box.insert(tk.END, track)

    def play_all(self):
        """Simulate playing all tracks in the playlist."""
        if not self.playlist:
            messagebox.showerror("Error", "The playlist is empty. Add tracks before playing.")
            return

        for track in self.playlist:
            track_id = track.split(" - ")[0].strip()
            lib.increment_play_count(track_id)

        messagebox.showinfo("Success", "All tracks in the playlist have been played!")
        self.update_playlist_display()

    def reset_playlist(self):
        """Clear the playlist and reset the display."""
        self.playlist = []
        self.update_playlist_display()



if __name__ == "__main__":
    window = tk.Tk()
    CreateTrackList(window)
    window.mainloop()