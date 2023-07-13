# Vergel, Chean Bernard V.
# Covid 19 Contact Tracing App

# Import libraries
import tkinter as tk
from PIL import ImageTk, Image

# Create a class for add 
class SuspectedContactWind(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        # Set the background image
        self.add_suspected_contact_wind_path = r"C:\Users\Chean vergel\Pictures\Contact Tracing Images\2.png"
        self.add_suspected_contact_wind = Image.open(self.add_suspected_contact_wind_path)
        self.add_suspected_contact_wind = self.add_suspected_contact_wind.resize((900, 500), Image.NEAREST)
        self.add_photo= ImageTk.PhotoImage(self.add_suspected_contact_wind)

        self.background_label = tk.Label(self, image=self.add_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a home button
        ok_button = tk.Button(self.window, text="OK", command=self.home_window, bg='yellow', font=('new times roman', 16))
        ok_button.place(x=750, y=700)

        # Create an exit button
        ok_button = tk.Button(self.window, text="OK", command=self.close_window, bg='yellow', font=('new times roman', 16))
        ok_button.place(x=750, y=700)



        # Define the home window. This home window will get to the home window

        # Define the exit window. This home window will exit the program
         


    