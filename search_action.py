# Vergel, Chean Bernard V.
# Covid 19 Contact Tracing App

# Import libraries
import tkinter as tk
from PIL import ImageTk, Image
import csv

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
        self.search_label = tk.Label(self, text="Enter Registered Name:", font=("Arial", 8))
        self.search_label.place(x=50, y=50)
        
        self.search_entry = tk.Entry(self, width=30)
        self.search_entry.place(x=190, y=50)

        # Create a button to perform the search
        search_button = tk.Button(self, text="SEARCH", command=self.perform_search)
        search_button.place(x=50, y=90) 

        self.result_canvas = tk.Canvas(self, width=700, height=220, bg="white", highlightthickness=1, highlightbackground="black")
        self.result_canvas.place(x=70, y=210)

    def perform_search(self):
            # Get the entered name for search
            search_name = self.search_entry.get()
            found = False

            # Search the name in the CSV file
            with open('entry.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == search_name:
                        found = True
                        # You can create labels or update existing labels to display the data in the GUI
                        result = f"Name: {row[0]}\nAge: {row[1]}\nBirthday: {row[2]}"

                        # Output other data fields as needed
                        self.result_canvas.create_text(10, 10, anchor="nw", text=result, font=("Arial", 11), fill="black")

                        # Exit the loop once the name is found
                        break


            if not found:
                self.result_label.config(text="Name not found.")




