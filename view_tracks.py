import tkinter as tk  # Standard Tkinter module for GUI development
import tkinter.scrolledtext as tkst  # ScrolledText widget for multi-line text areas with scrollbars
import track_library as lib  # Custom module containing track-related functions
import font_manager as fonts  # Custom module for managing font configurations
from tkinter import messagebox  # Message box utility for displaying alerts and dialogs
import os  # Operating system module for file and path handling
from PIL import Image, ImageTk  # Python Imaging Library for image handling in Tkinter

# Load track data into memory when the program starts
lib.load_library()

# Utility function to update the content of a text area
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear existing text
    text_area.insert("1.0", content)  # Insert new content

# Class representing the main GUI window for viewing tracks
class TrackViewer:

    # Constructor to initialize the GUI components
    def __init__(self, window):
        window.geometry("800x300")  # Set the window dimensions
        window.title("View Tracks")  # Set the window title
        window.configure(bg="gray")  # Set background color

        # Button to list all tracks
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # Label prompting the user to enter a track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Entry field for entering the track number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Button to view details of a specific track
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # Scrolled text area to display the list of tracks
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text area to display detailed information about a selected track
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Label to display the current status (e.g., button clicked)
        self.status_lbl = tk.Label(window, background="gray")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Label to display the album image
        self.image_lable = tk.Label(window, bg="lightgray")
        self.image_lable.grid(row=1, column=4, columnspan=4, sticky="W", padx=0, pady=0)

        # Display all tracks by default when the GUI starts
        self.list_tracks_clicked()

    # Function executed when "View Track" button is clicked
    def view_tracks_clicked(self):
        key = self.input_txt.get()  # Get user input (track number)

        # Validate: track number cannot be empty
        if not key:
            messagebox.showerror("Error", "Track number cannot be empty!")
            return

        # Validate: track number must be an integer
        if not key.isdigit():
            messagebox.showerror("Error", "Track number must be an integer")
            return

        # Format the key to always be 2 digits (e.g., 1 -> 01)
        if len(key) == 1:
            key = key.zfill(2)

        # Retrieve track details
        name = lib.get_name(key)

        if name is not None:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)  # Display track details in the text area
        else:
            # Handle invalid track ID
            set_text(self.track_txt, f"Track {key} not found")
            messagebox.showerror("Error", f"Track {key} not found")

        self.status_lbl.configure(text="View Track button was clicked!")

        # === DISPLAY ALBUM IMAGE ===
        image_path = os.path.join("img/", f"{key}.jpeg")  # Construct path to image file
        if os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((200, 200))  # Resize image to fit display area
            photo = ImageTk.PhotoImage(image)
            self.image_lable.configure(image=photo)  # Display the image
            self.image_lable.image = photo  # Keep a reference to avoid garbage collection
        else:
            # If image does not exist, clear the label and show a message
            self.image_lable.configure(image='', text="No image available")

    # Function executed when "List All Tracks" button is clicked
    def list_tracks_clicked(self):
        track_list = lib.list_all()  # Fetch list of all tracks
        set_text(self.list_txt, track_list)  # Display in the text area
        self.status_lbl.configure(text="List Tracks button was clicked!")  # Update status

# Run the application if this script is executed directly
if __name__ == "__main__":
    window = tk.Tk()         # Create the main window
    fonts.configure()        # Apply custom font settings
    TrackViewer(window)      # Instantiate the TrackViewer class
    window.mainloop()        # Start the Tkinter event loop
