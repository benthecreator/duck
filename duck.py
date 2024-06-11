import os
import sys
import tkinter as tk
import tkinter.font as font
import base64
import random
import pygame
import winshell
from win32com.client import Dispatch

window_dimensions = '700x325'
startup_folder_shortcut_name = 'windows32.lnk'

# Determine if running in a PyInstaller bundle
if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.abspath(os.path.dirname(__file__))

# Path to your image file
image_path = os.path.join(bundle_dir, "hugeDuck.png")

# Read the image file and encode it to base64
with open(image_path, 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    image_data = encoded_string

# Use the below code (and comment out lines 16 and 19-21) if you're fetching the image base64 from the image_data.txt file (who's data is written by using the function in convert_base64.py)
# # Path to the image_data.txt file
# image_data_path = os.path.join(bundle_dir, 'image_data.txt')

# # Read the image data from image_data.txt
# with open(image_data_path, "r") as f:
#     image_data = f.read()

# Path to the sound file
sound_file_path = os.path.join(bundle_dir, 'sound_file.mp3')

# Path to the icon file
icon_path = os.path.join(bundle_dir, 'duckIcon.ico')

def add_startup():
    global startup_folder_shortcut_name
    try:
        # Get the user's Startup folder
        startup_folder = winshell.startup()

        # Get the script's current directory
        script_dir = os.path.dirname(os.path.realpath(__file__))

        # Create the full path to the script
        script_path = os.path.join(script_dir, sys.argv[0])

        # Create the full path to the shortcut
        shortcut_path = os.path.join(startup_folder, startup_folder_shortcut_name)

        # Check if the script is already in the startup folder
        if os.path.exists(shortcut_path):
            msg = "Script is already in the user's Startup folder."
            print(msg)
        else:
            # Create the shortcut
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.TargetPath = script_path
            shortcut.WorkingDirectory = script_dir
            shortcut.IconLocation = icon_path
            shortcut.save()

            msg = f"Shortcut '{startup_folder_shortcut_name}' added to user's Startup folder. Full path: '{shortcut_path}'"
            print(msg)
    except Exception as e:
        error_msg = f"Error adding shortcut to user's Startup folder: {str(e)}"
        print(error_msg)

class MessageWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello There")

        # Set the window icon
        self.root.iconbitmap(icon_path)

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Load the sound file
        pygame.mixer.music.load(sound_file_path)

        # Convert the embedded image data back to bytes
        image_bytes = base64.b64decode(image_data)

        # Create a PhotoImage object from the embedded image data
        self.image = tk.PhotoImage(data=image_bytes)

        # Set the size of the window
        self.root.geometry(window_dimensions)

        # Apply the same attributes to the main window
        self.setup_window_attributes(self.root)

        # Bind the on_close function to the window closing event
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def close_windows(self, windows):
        for window in windows:
            window.destroy()

    def play_sound(self):
        # Play the sound file
        pygame.mixer.music.play()

    def on_close(self):
        # Play the sound when the window is closed
        self.play_sound()

        # Create two new windows with random positions and configure attributes
        new_window1 = tk.Toplevel(self.root)
        new_window1.geometry(f'{window_dimensions}+{random.randint(0, 800)}+{random.randint(0, 600)}')
        self.setup_window_attributes(new_window1)
        new_window1.iconbitmap(icon_path)

        new_window2 = tk.Toplevel(self.root)
        new_window2.geometry(f'{window_dimensions}+{random.randint(0, 800)}+{random.randint(0, 600)}')
        self.setup_window_attributes(new_window2)
        new_window2.iconbitmap(icon_path)

        # Schedule the close_windows function for the new windows after 10 seconds
        self.root.after(10000, lambda: self.close_windows([new_window1]))
        self.root.after(11000, lambda: self.close_windows([new_window2]))

        # Don't destroy the original window, comment or remove the following line
        # self.root.destroy()

    def setup_window_attributes(self, window):
        # Set the background color of the window to black
        window.configure(bg='black')

        # Reapply attributes to the new window
        image_label = tk.Label(window, image=self.image)
        image_label.pack(side='left', padx=10, pady=10, anchor='center')

        # Use a bold font for the text and set the text color to white
        bold_font = font.Font(weight='bold')
        text_message = tk.Message(window, text="This is Duckさん. \nHe's harmless...I think.\nHe also doesn't go away.", width=350, font=bold_font, bg='black', fg='red')
        text_message.pack(side='right', padx=10, pady=10)

        # Bind the on_close function to the window closing event for Toplevel windows
        window.protocol("WM_DELETE_WINDOW", self.on_close)

if __name__ == "__main__":
    add_startup()
    root = tk.Tk()
    app = MessageWindow(root)
    root.mainloop()