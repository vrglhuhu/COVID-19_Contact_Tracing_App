# Vergel, Chean Bernard V.
# Covid 19 Contact Tracing App

# Import libraries
import tkinter as tk
from PIL import ImageTk, Image

# Create a class for last frame
class LastFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.label = tk.Label(self, text="CONTACT TRACING CASE")
        self.label.pack(pady=20)

        # Set the background image
        self.add_responded_path = r"C:\Users\Chean vergel\Pictures\Contact Tracing Images\last frame.png"
        self.add_responded = Image.open(self.add_responded_path)
        self.add_responded = self.add_responded.resize((900, 500), Image.NEAREST)
        self.add_photo = ImageTk.PhotoImage(self.add_responded)

        self.background_label = tk.Label(self, image=self.add_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create an exit button
        ok_button = tk.Button(self.master, text="OK", command=self.close_window, bg='#8D60FF', font=('new times roman', 12))
        ok_button.place(x=430, y=380)

        # create back button
        back_button = tk.Button(self, text='Back', command=self.go_to_main_window, bg='yellow', font=('new times roman', 12))
        back_button.place(x=20, y=20)

    # Define the exit window. This home window will exit the program
    def close_window(self):
        self.master.destroy()

    def go_to_main_window(self):
        self.master.destroy()
        self.after(0, self.open_main_window)
    
    def open_main_window(self):
        app = self.FirstPage()
        app.main_window()