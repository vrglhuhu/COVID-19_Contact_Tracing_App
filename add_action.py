# Vergel, Chean Bernard V.
# Covid 19 Contact Tracing App

# Import libraries
import tkinter as tk
from PIL import ImageTk, Image

class InfoFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        # Set the background image
        image_path = r"C:\Users\Chean vergel\Pictures\PUP BACKGROUND\Pylon Maroon with trees.jpg"
        image = Image.open(image_path)
        image = image.resize((900, 500), Image.NEAREST)
        photo = ImageTk.PhotoImage(image)
        
        self.background_label = tk.Label(self, image=photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

 

        