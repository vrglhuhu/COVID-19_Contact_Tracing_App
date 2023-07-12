# Vergel, Chean Bernard V.
# Covid 19 Contact Tracing App

# Import libraries
import tkinter as tk
from PIL import ImageTk, Image

# Create a class for add 
class AddFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        # Set the background image
        self.add_image_path = r"C:\Users\Chean vergel\Pictures\Contact Tracing Images\covid- 19 second.png"
        self.add_image = Image.open(self.add_image_path)
        self.add_image = self.add_image.resize((900, 500), Image.NEAREST)
        self.add_photo = ImageTk.PhotoImage(self.add_image)

        self.background_label = tk.Label(self, image=self.add_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # BasicInformation label
        self.info = tk.Label(self, text="BASIC INFORMATION.", height=1, font=("Arial", 8))
        self.info.place(x=15, y=10)
        self.info.config(bg="#20c997")

        # Name
        self.name = tk.Label(self, text="NAME: ", height=1, font=("Arial", 8))
        self.name.place(x=15, y=40)
        self.name.config(bg="#BAF8FA")

        # Name Input
        self.name_entry = tk.Entry(self, width=40)
        self.name_entry.place(x=60, y= 40)
        # Set initial text
        self.name_entry.insert(0, "FIRSTNAME/LASTNAME/SURNAME")  
        self.name_entry.bind("<FocusIn>", self.clear_name_text)
        self.name_entry.config(fg="gray")

        # Age
        self.age = tk.Label(self, text="AGE: ", height=1, font=("Arial", 8))
        self.age.place(x=15, y=70)
        self.age.config(bg="#BAF8FA")

        # Age Input
        self.age_entry = tk.Entry(self, width=40)
        self.age_entry.place(x=58, y= 70)
        # Set initial text
        self.age_entry.insert(0, "YOUR AGE")  
        self.age_entry.bind("<FocusIn>", self.clear_age_text)
        self.age_entry.config(fg="gray")

        # Birthday
        self.bday_entry = tk.Label(self, text="BIRTHDAY: ", height=1, font=("Arial", 8))
        self.bday_entry.place(x=15, y=100)
        self.bday_entry.config(bg="#BAF8FA")

        # Birthday Input
        self.bday_entry = tk.Entry(self, width=36)
        self.bday_entry.place(x=90, y= 100)
        # Set initial text
        self.bday_entry.insert(0, "MM/DD/YYYY")  
        self.bday_entry.bind("<FocusIn>", self.clear_bday_text)
        self.bday_entry.config(fg="gray")

        # Date
        self.date = tk.Label(self, text="DATE ", height=1, font=("Arial", 8))
        self.date.place(x=15, y=130)
        self.date.config(bg="#BAF8FA")

        # Date Input
        self.date_entry = tk.Entry(self, width=40)
        self.date_entry.place(x=58, y= 130)
        # Set initial text
        self.date_entry.insert(0, "MM/DD/YYYY")  
        self.date_entry.bind("<FocusIn>", self.clear_date_text)
        self.date_entry.config(fg="gray")

        # Contact Information label
        self.contact_info = tk.Label(self, text="CONTACT INFORMATION.", height=1, font=("Arial", 8))
        self.contact_info.place(x=410, y=10)
        self.contact_info.config(bg="#20c997")

        # Contact Number
        self.cont_num = tk.Label(self, text="CONTACT NUMBER: ", height=1, font=("Arial", 8))
        self.cont_num.place(x=410, y=40)
        self.cont_num.config(bg="#BAF8FA")

        # Contact Number Input

        # Email Address
        self.age = tk.Label(self, text="EMAIL ADDRESS: ", height=1, font=("Arial", 8))
        self.age.place(x=410, y=70)
        self.age.config(bg="#BAF8FA")

        # Email Address Input












    # Display text will be gone if the user click the entry

    def clear_name_text(self, event):
        self.name_entry.delete(0, tk.END)
        self.name_entry.config(fg="black")
    def clear_age_text(self, event):
        self.age_entry.delete(0, tk.END)
        self.age_entry.config(fg="black")
    def clear_bday_text(self, event):
        self.bday_entry.delete(0, tk.END)
        self.bday_entry.config(fg="black")
    def clear_date_text(self, event):
        self.date_entry.delete(0, tk.END)
        self.date_entry.config(fg="black")
    def clear_cont_num_text(self, event):
        self.date_entry.delete(0, tk.END)
        self.date_entry.config(fg="black")

        

 







        