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
        self.search_image_path = r"C:\Users\Chean vergel\Pictures\Contact Tracing Images\updated search.png"
        self.search_image = Image.open(self.search_image_path)
        self.search_image = self.search_image.resize((900, 500), Image.NEAREST)
        self.search_photo = ImageTk.PhotoImage(self.search_image)

        self.background_label = tk.Label(self, image=self.search_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create some labels 
        self.search_label = tk.Label(self, text="SEARCH SAVED INFORMATION",  font=("Arial", 11))
        self.search_label.place(x=330, y=10)
        self.search_label.config(bg="#BAF8FA" )

        # Create search components here
        self.search_label = tk.Label(self, text="Enter Registered Name:",bg="#00b89f", font=("Arial", 9))
        self.search_label.place(x=70, y=50)
        
        self.search_entry = tk.Entry(self, width=30)
        self.search_entry.place(x=223, y=50)

        # Create a button to perform the search
        search_button = tk.Button(self, text="SEARCH",bg="#e19c55", command=self.perform_search)
        search_button.place(x=70, y=80) 

        # Create canvass for the result
        self.result1_canvas = tk.Canvas(self, width=390, height=320, bg="#88ffcc", highlightthickness=1, highlightbackground="black")
        self.result1_canvas.place(x=24, y=130)

        # Create another canvass for the result
        self.result2_canvas = tk.Canvas(self, width=435, height=320, bg="#88ffcc", highlightthickness=1, highlightbackground="black")
        self.result2_canvas.place(x=435, y=130)

        # Create an exit button
        ok_button = tk.Button(self.master, text="OK", command=self.close_window, bg='#fddfae', font=('new times roman', 12))
        ok_button.place(x=405, y=455)

     # Define the exit window. This home window will exit the program
    def close_window(self):
        self.master.destroy()

    # Define the perform search
    def perform_search(self):
            
            self.result1_canvas.delete("all")
            self.result2_canvas.delete("all")

            # Get the entered name for search
            search_name = self.search_entry.get()
            found = False

            # Search the name in the CSV file
            with open('entry.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == search_name:
                        found = True
                        # Create value for result
                        result1 = f"BASIC INFORMATION\033\n\nName: {row[0]}\nAge: {row[1]}\nBirthday: {row[2]}\nResponse Date: {row[3]}\nContact Number: {row[4]}\nEmail: {row[5]}\n\n"
                        result1 += f"EMERGENCY INFORMATION\033\n\nContact Person Name: {row[6]}\nEmergency Contact Number: {row[7]}\nEmergency Email: {row[8]}\nRelationship: {row[9]}\n\n"
                        result2 = f"TRAVEL DECLARATION\n\nHave you traveled abroad in the last 7 days? {row[10]}\nAre you near an area with local transmission? {row[11]}\nDo you have a relative who came from another country? {row[12]}\n\n"
                        result2 += f"HEALTH DECLARATION\n\nAre you already vaccinated for Covid-19? {row[13]}\nDo you have any symptoms in the past 7 days? {row[14]}\nDo you have an exposure to a confirmed covid patient\n in the past 7 days? {row[15]}\nHave you been tested for Covid-19 in the past 14 day? {row[15]}"
                        # Output other data fields as needed
                        self.result1_canvas.create_text(10, 10, anchor="nw", text=result1, font=("Arial", 10), fill="black")
                        self.result2_canvas.create_text(10, 10, anchor="nw", text=result2, font=("Arial", 10), fill="black")
                        # Exit the loop once the name is found
                        break


            if not found:
                self.result1_canvas.create_text(10, 10, anchor="nw", text="Unfortunately name not found", font=("Arial", 11), fill="red")
                self.result2_canvas.create_text(10, 10, anchor="nw", text="")