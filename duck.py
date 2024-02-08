import tkinter as tk
import tkinter.font as font  # Import the font module
import base64
import random

# Assuming you have the image_data variable defined in another file
from image_data import image_data

class MessageWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Hello There")

        # Convert the embedded image data back to bytes
        image_bytes = base64.b64decode(image_data)

        # Create a PhotoImage object from the embedded image data
        self.image = tk.PhotoImage(data=image_bytes)

        # Set the size of the window
        self.root.geometry('550x200')

        # Apply the same attributes to the main window
        self.setup_window_attributes(self.root)

        # Bind the on_close function to the window closing event
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)


    def close_windows(self, windows):
        for window in windows:
            window.destroy()

    def on_close(self):
        # Create two new windows with random positions and configure attributes
        new_window1 = tk.Toplevel(self.root)
        new_window1.geometry(f'550x200+{random.randint(0, 800)}+{random.randint(0, 600)}')
        self.setup_window_attributes(new_window1)

        new_window2 = tk.Toplevel(self.root)
        new_window2.geometry(f'550x200+{random.randint(0, 800)}+{random.randint(0, 600)}')
        self.setup_window_attributes(new_window2)

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
        text_message = tk.Message(window, text="This is Ominous Duck. \nHe's harmless, I think.\nHe also doesn't go away! :O", width=350, font=bold_font, bg='black', fg='red')
        text_message.pack(side='right', padx=10, pady=10)

        # Bind the on_close function to the window closing event for Toplevel windows
        window.protocol("WM_DELETE_WINDOW", self.on_close)

if __name__ == "__main__":
    root = tk.Tk()
    app = MessageWindow(root)
    root.mainloop()
