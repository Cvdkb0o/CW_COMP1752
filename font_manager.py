import tkinter.font as tkfont

def configure():
    """
    Configures the default font styles used across the Tkinter application
    for a consistent and readable user interface.
    """
    # Define the font family to use throughout the application
    # You can change "Helvetica" to another available font like "Segoe UI"
    family = "Helvetica"

    # Configure the default font used for most widgets
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=15, family=family)

    # Configure the font used for Text widgets
    text_font = tkfont.nametofont("TkTextFont")
    text_font.configure(size=12, family=family)

    # Configure the font used for fixed-width widgets (e.g., code display)
    fixed_font = tkfont.nametofont("TkFixedFont")
    fixed_font.configure(size=12, family=family)
