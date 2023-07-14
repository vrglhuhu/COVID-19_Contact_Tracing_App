# Vergel, Chean Bernard V.
# Covid 19 Contact Tracing App

# Import tkinter
import tkinter as tk
from PIL import ImageTk, Image
from add_action import AddFrame
from search_action import SearchFrame

# Create the main window
class FirstPage():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("COVID-19 CONTACT TRACING APP")

        # Set the window size and position it in the center of the screen
        self.window.geometry("900x500")
        self.window.resizable(False, False)

        # Set the background image
        image_path = r"C:\Users\Chean vergel\Pictures\Contact Tracing Images\covid- 19.png"
        image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(image)
        
        self.background_label = tk.Label(self.window, image=self.photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create buttons for adding and searching
        add_button = tk.Button(self.window, text="Add", command=FirstPage.add_action)
        add_button.place(x=640, y=230, width=100, height=30)

        search_button = tk.Button(self.window, text="Search", command=FirstPage.search_action)
        search_button.place(x=640, y=265, width=100, height=30)
        
        # Start the main loop
        self.window.mainloop()

    # Create add action
    def add_action():
        # Add action logic goes here
        info_frame = AddFrame()
        info_frame.place(x=0, y=0, relwidth=1, relheight=1)

    # Create search action
    def search_action():
        # Search action logic goes here
        search_frame = SearchFrame()
        search_frame.place(x=0, y=0, relwidth=1, relheight=1)
    
    def close_window(self):
        self.window.destroy()
    
    def run(self):
        self.window.mainloop()
        
if __name__ == "__main__":
    app = FirstPage()
    app.run()