import tkinter as tk  # Tkinter module for building the GUI
import font_manager as fonts  # Custom module to manage fonts and styles
from view_tracks import TrackViewer  # GUI class for viewing track details
from update_track import UpdateTrack  # GUI class for updating track information
from create_track_list import CreateTrackList  # GUI class for creating a new track list

# === Button callback functions ===

# Open the TrackViewer window
def view_tracks_clicked():
    status_lbl.configure(text="View Tracks button was clicked!")
    TrackViewer(tk.Toplevel(window))  # Open a new top-level window for viewing tracks

# Open the CreateTrackList window
def create_track_clicked():
    status_lbl.configure(text="Create Track button was clicked!")
    CreateTrackList(tk.Toplevel(window))  # Open a new top-level window for creating tracks

# Open the UpdateTrack window
def update_tracks_clicked():
    status_lbl.configure(text="Update Tracks button was clicked!")
    UpdateTrack(tk.Toplevel(window))  # Open a new top-level window for updating tracks


# === Main GUI Setup ===

window = tk.Tk()  # Create the main application window
window.geometry("")  # Optional: Leave empty to auto-size or specify e.g. "600x400"
window.title("JukeBox")  # Set the window title
window.configure(bg="gray")  # Set the background color

fonts.configure()  # Apply custom font settings (assumes font_manager handles this)

# Create a header label with user instructions
header_lbl = tk.Label(
    window,
    text="Select an option by clicking one of the buttons below"
)
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# === Main menu buttons ===

# Button to view tracks
view_tracks_btn = tk.Button(window, text="View Tracks", command=view_tracks_clicked)
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

# Button to create a new track list
create_track_list_btn = tk.Button(window, text="Create Track List", command=create_track_clicked)
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

# Button to update existing tracks
update_tracks_btn = tk.Button(window, text="Update Tracks", command=update_tracks_clicked)
update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

# Status label to show feedback messages
status_lbl = tk.Label(window, bg='gray')
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Run the application event loop
window.mainloop()
