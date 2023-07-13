# Vergel, Chean Bernard V.
# Covid 19 Contact Tracing App

# Import libraries
import tkinter as tk
from PIL import ImageTk, Image

# Create a class for add 
class SafeCaseWind(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        # Set the background image
        self.add_safe_case_wind_path = r"C:\Users\Chean vergel\Pictures\Contact Tracing Images\4.png"
        self.add_safe_case_wind = Image.open(self.add_safe_case_wind_path)
        self.add_safe_case_wind = self.add_safe_case_wind.resize((900, 500), Image.NEAREST)
        self.add_photo = ImageTk.PhotoImage(self.add_safe_case_wind)

        self.background_label = tk.Label(self, image=self.add_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create an exit button
        ok_button = tk.Button(self.master, text="OK", command=self.close_window, bg='#8D60FF', font=('new times roman', 12))
        ok_button.place(x=430, y=380)

    # Define the exit window. This home window will exit the program
    def close_window(self):
        self.master.destroy()