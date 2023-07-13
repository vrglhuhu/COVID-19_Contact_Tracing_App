# Vergel, Chean Bernard V.
# Covid 19 Contact Tracing App

# Import libraries
import tkinter as tk
from PIL import ImageTk, Image

class SearchFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        # Set the background image
        self.search_image_path = r"C:\Users\Chean vergel\Pictures\Contact Tracing Images\search.png"
        self.search_image = Image.open(self.search_image_path)
        self.search_image = self.search_image.resize((900, 500), Image.NEAREST)
        self.search_photo = ImageTk.PhotoImage(self.search_image)

        self.background_label = tk.Label(self, image=self.search_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create search components here
        # ...

        # Create a button to perform the search
        search_button = tk.Button(self, text="SEARCH", command=self.perform_search)
        search_button.place(x=50, y=90) 

    def perform_search(self):
        # Search logic goes here
        pass
