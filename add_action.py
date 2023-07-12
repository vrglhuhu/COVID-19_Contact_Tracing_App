# Vergel, Chean Bernard V.
# Covid 19 Contact Tracing App

# Import libraries
import tkinter as tk
from PIL import ImageTk, Image

# Create a class for add 
class AddFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        # Set the background image
        self.add_image_path = r"C:\Users\Chean vergel\Pictures\Contact Tracing Images\covid- 19 second.png"
        self.add_image = Image.open(self.add_image_path)
        self.add_image = self.add_image.resize((900, 500), Image.NEAREST)
        self.add_photo = ImageTk.PhotoImage(self.add_image)

        self.background_label = tk.Label(self, image=self.add_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Information label
        self.info = tk.Label(self, text="BASIC INFORMATION.", height=1, font=("Source Sans Pro", 8))
        self.info.place(x=15, y=10)
        self.info.config(bg="#20c997")

        # Date
        self.date = tk.Label(self, text="Date", height=1, font=("Source Sans Pro", 7))
        self.date.place(x=30, y=40)
        self.date.config(bg="#BAF8FA")




        