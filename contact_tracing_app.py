# Vergel, Chean Bernard V.
# Covid 19 Contact Tracing App

# Import tkinter
import tkinter as tk
from PIL import ImageTk, Image
from add_action import InfoFrame

# Create the main window
def main_window():
    window = tk.Tk()
    window.title("COVID-19 CONTACT TRACING APP")

    # Set the window size and position it in the center of the screen
    window.geometry("900x500")
    window.resizable(False, False)
    window.eval('tk::PlaceWindow . center')

    # Set the background image
    image_path = r"C:\Users\Chean vergel\Pictures\Contact Tracing Images\covid- 19.png"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    
    background_label = tk.Label(window, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create buttons for adding and searching
    add_button = tk.Button(window, text="Add", command=add_action)
    add_button.place(x=640, y=230, width=100, height=30)

    search_button = tk.Button(window, text="Search", command=search_action)
    search_button.place(x=640, y=265, width=100, height=30)
    
    # Start the main loop
    window.mainloop()

# Create add action
def add_action():
    # Add action logic goes here
    info_frame = InfoFrame()
    info_frame.place(x=0, y=0, relwidth=1, relheight=1)

# Create search action
def search_action():
    # Search action logic goes here
    pass    
    
# Call the main_window function to run the application
main_window()