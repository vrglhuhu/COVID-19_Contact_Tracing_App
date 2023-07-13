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

    def perform_search(self):
            # Get the entered name for search
            search_name = self.search_entry.get()

            # Search the name in the CSV file
            with open('entry.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 0 and row[0] == search_name:
                        # Display the corresponding data for the name
                        # You can customize the output based on your requirements
                        print("Name:", row[0])
                        print("Age:", row[1])
                        print("Birthday:", row[2])
                        # Display other corresponding data as needed

                        # You can create labels or update existing labels to display the data in the GUI
                        # Example:
                        # self.name_label.config(text="Name: " + row[0])
                        # self.age_label.config(text="Age: " + row[1])
                        # ...

                        # Exit the loop once the name is found
                        break


    def perform_search(self):
        # Search logic goes here
        pass
