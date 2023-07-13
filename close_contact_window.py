# Vergel, Chean Bernard V.
# Covid 19 Contact Tracing App

# Import libraries
import tkinter as tk
from PIL import ImageTk, Image

# Create a class for add 
class CloseContactWind(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        # Set the background image
        self.add_close_contact_wind_path = r"C:\Users\Chean vergel\Pictures\Contact Tracing Images\1.png"
        self.add_close_contact_wind = Image.open(self.add_close_contact_wind_path)
        self.add_close_contact_wind = self.add_close_contact_wind.resize((900, 500), Image.NEAREST)
        self.add_photo = ImageTk.PhotoImage(self.add_close_contact_wind)

        self.background_label = tk.Label(self, image=self.add_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)


