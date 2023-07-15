# Vergel, Chean Bernard V.
# Covid 19 Contact Tracing App

# Import libraries
import csv
import tkinter as tk
from PIL import ImageTk, Image
from last_frame import LastFrame


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
        self.name_entry = tk.Entry(self, width=30)
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
        self.age_entry = tk.Entry(self, width=30)
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
        self.bday_entry = tk.Entry(self, width=26)
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
        self.date_entry = tk.Entry(self, width=30)
        self.date_entry.place(x=58, y= 130)
        # Set initial text
        self.date_entry.insert(0, "MM/DD/YYYY")  
        self.date_entry.bind("<FocusIn>", self.clear_date_text)
        self.date_entry.config(fg="gray")

        # Contact Information label
        self.contact_info = tk.Label(self, text="CONTACT INFORMATION.", height=1, font=("Arial", 8))
        self.contact_info.place(x=325, y=10)
        self.contact_info.config(bg="#20c997")

        # Contact Number
        self.cont_num = tk.Label(self, text="CONTACT NUMBER: ", height=1, font=("Arial", 8))
        self.cont_num.place(x=325, y=40)
        self.cont_num.config(bg="#BAF8FA")

        # Contact Number Input
        self.cont_num_entry = tk.Entry(self, width=15)
        self.cont_num_entry.place(x=458, y= 40)
        # Set initial text
        self.cont_num_entry.insert(0, "09*********")  
        self.cont_num_entry.bind("<FocusIn>", self.clear_cont_num_text)
        self.cont_num_entry.config(fg="gray")

        # Email Address
        self.email = tk.Label(self, text="EMAIL ADDRESS: ", height=1, font=("Arial", 8))
        self.email.place(x=590, y=40)
        self.email.config(bg="#BAF8FA")

        # Email Address Input
        self.email_ad_entry = tk.Entry(self, width=22)
        self.email_ad_entry.place(x=705, y= 40)
        # Set initial text
        self.email_ad_entry.insert(0, "carlomanuel@gmail.com")  
        self.email_ad_entry.bind("<FocusIn>", self.clear_email_ad_text)
        self.email_ad_entry.config(fg="gray")


        # Emergency Information Label
        self.emergency_info = tk.Label(self, text="EMERGENCY INFORMATION.", height=1, font=("Arial", 8))
        self.emergency_info.place(x=325, y=70)
        self.emergency_info.config(bg="#20c997")

        # Name
        self.emer_name_entry = tk.Label(self, text="NAME : ", height=1, font=("Arial", 8))
        self.emer_name_entry.place(x=325, y=100)
        self.emer_name_entry.config(bg="#BAF8FA")

        # Name input
        self.emer_name_entry = tk.Entry(self, width=30)
        self.emer_name_entry.place(x=380, y= 100)
        # Set initial text
        self.emer_name_entry.insert(0, "FIRSTNAME/LASTNAME/SURNAME")  
        self.emer_name_entry.bind("<FocusIn>", self.clear_emer_name_text)
        self.emer_name_entry.config(fg="gray")

        # Contact number
        self.emer_cont_num = tk.Label(self, text="CONTACT NUMBER: ", height=1, font=("Arial", 8))
        self.emer_cont_num.place(x=325, y=130)
        self.emer_cont_num.config(bg="#BAF8FA")

        # Contact Number Input
        self.emer_cont_num_entry = tk.Entry(self, width=15)
        self.emer_cont_num_entry.place(x=458, y= 130)
        # Set initial text
        self.emer_cont_num_entry.insert(0, "09*********")  
        self.emer_cont_num_entry.bind("<FocusIn>", self.clear_emer_cont_num_text)
        self.emer_cont_num_entry.config(fg="gray")

        # Email Address
        self.emer_email_add = tk.Label(self, text="EMAIL ADDRESS: ", height=1, font=("Arial", 8))
        self.emer_email_add.place(x=590, y=130)
        self.emer_email_add.config(bg="#BAF8FA")

        # Email Address Input
        self.emer_email_add_entry = tk.Entry(self, width=22)
        self.emer_email_add_entry.place(x=705, y= 130)
        # Set initial text
        self.emer_email_add_entry.insert(0, "carlomanuel@gmail.com")  
        self.emer_email_add_entry.bind("<FocusIn>", self.clear_emer_email_add_text)
        self.emer_email_add_entry.config(fg="gray")

        # Relationship
        self.relation_entry = tk.Label(self, text="RELATIONSHIP : ", height=1, font=("Arial", 8))
        self.relation_entry.place(x=630, y=100)
        self.relation_entry.config(bg="#BAF8FA")

        # Relationship input
        self.relation_entry = tk.Entry(self, width=19)
        self.relation_entry.place(x=730, y= 100)
        # Set initial text
        self.relation_entry.insert(0, "MOTHER/FATHER etc")  
        self.relation_entry.bind("<FocusIn>", self.clear_relation_ad_text)
        self.relation_entry.config(fg="gray")

        # Create a boundary line
        self.boundary = tk.Label(self,text = "<>" * 72, font=("Arial", 6))
        self.boundary.place(x=15, y=160)
        self.boundary.config(fg="#000000", bg="#659c55")


        # Create Travel Declaration Label
        self.travel_declaration = tk.Label(self, text="TRAVEL DECLARATION ", height=1, font=("Arial", 8))
        self.travel_declaration.place(x=15, y=185)
        self.travel_declaration.config(bg="#20c997")

        # Ask if the user travelled abroad
        self.travel_label = tk.Label(self, text="Have you traveled abroad in the last 7 days?", font=("Arial", 8))
        self.travel_label.place(x=15, y=210)
        self.travel_label.config(bg="#BAF8FA")

        # Create the travel choice variable
        self.travel_choice = tk.StringVar()
        
        # Create Yes Radiobuttons
        self.yes_radio = tk.Radiobutton(self, text="Yes", font=("Arial", 8), variable=self.travel_choice, value="yes")
        self.yes_radio.place(x=35, y=235)
        self.yes_radio.config(bg="#B3FFA8")

        # Create No Radiobuttons
        self.no_radio = tk.Radiobutton(self, text="No", font=("Arial", 8), variable=self.travel_choice, value="no")
        self.no_radio.place(x=100, y=235)
        self.no_radio.config(bg="#B3FFA8")
        
        # Ask if the user is near in a where there is a local tranmission
        self.transmission_label = tk.Label(self, text="Are you near an area with local transmission?", font=("Arial", 8))
        self.transmission_label.place(x=15, y=260)
        self.transmission_label.config(bg="#BAF8FA")

        # Create the local transmission choice variable
        self.transmission_choice = tk.StringVar()

        # Create Yes Radiobutton for local transmission
        self.transmission_yes_radio = tk.Radiobutton(self, text="Yes", font=("Arial", 8), variable=self.transmission_choice, value="yes")
        self.transmission_yes_radio.place(x=35, y=285)
        self.transmission_yes_radio.config(bg="#B3FFA8")

        # Create No Radiobutton for local transmission
        self.transmission_no_radio = tk.Radiobutton(self, text="No", font=("Arial", 8), variable=self.transmission_choice, value="no")
        self.transmission_no_radio.place(x=100, y=285)
        self.transmission_no_radio.config(bg="#B3FFA8")

        # Ask if the user has relative came from other country
        self.relative_label = tk.Label(self, text="Do you have a relative who came from another country?", font=("Arial", 8))
        self.relative_label.place(x=15, y=310)
        self.relative_label.config(bg="#BAF8FA")

        # Create the relative choice variable
        self.relative_choice = tk.StringVar()

        # Create Yes Radiobuttons
        self.relative_yes_radio = tk.Radiobutton(self, text="Yes", font=("Arial", 8), variable=self.relative_choice, value="yes")
        self.relative_yes_radio.place(x=35, y=335)
        self.relative_yes_radio.config(bg="#B3FFA8")

        # Create No Radiobuttons
        self.relative_no_radio = tk.Radiobutton(self, text="No", font=("Arial", 8), variable=self.relative_choice, value="no")
        self.relative_no_radio.place(x=100, y=335)
        self.relative_no_radio.config(bg="#B3FFA8")

        # Create Health Declaration Label
        self.health_declaration = tk.Label(self, text="HEALTH DECLARATION ", height=1, font=("Arial", 8))
        self.health_declaration.place(x=380, y=185)
        self.health_declaration.config(bg="#20c997")

        # Ask if the user have been vaccinated for Covid 19
        self.vaccine_label = tk.Label(self, text="Are you already vaccinated for Covid-19?", font=("Arial", 8))
        self.vaccine_label.place(x=380, y=210)
        self.vaccine_label.config(bg="#BAF8FA")

        # Create the vaccine choice variable
        self.vaccine_choice = tk.StringVar()

        # Create choice 1
        self.vaccine_choice1_radio = tk.Radiobutton(self, text="1st Dose", font=("Arial", 8), variable=self.vaccine_choice, value="1")
        self.vaccine_choice1_radio.place(x=400, y=235)
        self.vaccine_choice1_radio.config(bg="#B3FFA8")

        # Create choice 2
        self.vaccine_choice2_radio = tk.Radiobutton(self, text="2nd Dose", font=("Arial", 8), variable=self.vaccine_choice, value="2")
        self.vaccine_choice2_radio.place(x=490, y=235)
        self.vaccine_choice2_radio.config(bg="#B3FFA8")

        # Create choice 3
        self.vaccine_choice3_radio = tk.Radiobutton(self, text="1st Booster Shot", font=("Arial", 8), variable=self.vaccine_choice, value="3")
        self.vaccine_choice3_radio.place(x=585, y=235)
        self.vaccine_choice3_radio.config(bg="#B3FFA8")

        # Create choice 4
        self.vaccine_choice4_radio = tk.Radiobutton(self, text="2nd Booster Shot", font=("Arial", 8), variable=self.vaccine_choice, value="4")
        self.vaccine_choice4_radio.place(x=725, y=235)
        self.vaccine_choice4_radio.config(bg="#B3FFA8")

        # Create choice 5
        self.vaccine_choice5_radio = tk.Radiobutton(self, text="Not Yet", font=("Arial", 8), variable=self.vaccine_choice, value="5")
        self.vaccine_choice5_radio.place(x=400, y=265)
        self.vaccine_choice5_radio.config(bg="#B3FFA8")

        # Ask if user has symptoms in the past 7 days
        self.symptoms_label = tk.Label(self, text="Do you have any symptoms in the past 7 days?", font=("Arial", 8))
        self.symptoms_label.place(x=380, y=295)
        self.symptoms_label.config(bg="#BAF8FA")

        # Create the symptoms choice variable
        self.symptoms_choice = tk.StringVar()

        # Create Yes Radiobuttons
        self.symptoms_yes_radio = tk.Radiobutton(self, text="Yes", font=("Arial", 8), variable=self.symptoms_choice, value="yes")
        self.symptoms_yes_radio.place(x=400, y=320)
        self.symptoms_yes_radio.config(bg="#B3FFA8")

        # Create No Radiobuttons
        self.symptoms_no_radio = tk.Radiobutton(self, text="No", font=("Arial", 8), variable=self.symptoms_choice, value="no")
        self.symptoms_no_radio.place(x=470, y=320)
        self.symptoms_no_radio.config(bg="#B3FFA8")

        # Ask if the user has an exposure to a confirmed covid patient
        self.exposure_label = tk.Label(self, text="Do you have an exposure to a confirmed covid patient in the past 7 days?", font=("Arial", 8))
        self.exposure_label.place(x=380, y=350)
        self.exposure_label.config(bg="#BAF8FA")

        # Create the exposure choice variable
        self.exposure_choice = tk.StringVar()

        # Create Yes Radiobuttons
        self.exposure_yes_radio = tk.Radiobutton(self, text="Yes", font=("Arial", 8), variable=self.exposure_choice, value="yes")
        self.exposure_yes_radio.place(x=400, y=375)
        self.exposure_yes_radio.config(bg="#B3FFA8")

        # Create No Radiobuttons
        self.exposure_no_radio = tk.Radiobutton(self, text="No", font=("Arial", 8), variable=self.exposure_choice, value="no")
        self.exposure_no_radio.place(x=470, y=375)
        self.exposure_no_radio.config(bg="#B3FFA8")

        # Ask if the user have been tested for Covid-19 in the past 14 day
        self.tested_label = tk.Label(self, text="Have you been tested for Covid-19 in the past 14 day?", font=("Arial", 8))
        self.tested_label.place(x=380, y=405)
        self.tested_label.config(bg="#BAF8FA")

        # Create the tested choice variable
        self.tested_choice = tk.StringVar()

        # Create Yes Radiobuttons
        self.tested_yes_radio = tk.Radiobutton(self, text="Yes", font=("Arial", 8), variable=self.tested_choice, value="yes")
        self.tested_yes_radio.place(x=400, y=430)
        self.tested_yes_radio.config(bg="#B3FFA8")

        # Create No Radiobuttons
        self.tested_No_radio = tk.Radiobutton(self, text="No", font=("Arial", 8), variable=self.tested_choice, value="no")
        self.tested_No_radio.place(x=470, y=430)
        self.tested_No_radio.config(bg="#B3FFA8")

        # Create Submit Button
        submit_button = tk.Button(self, text="SUBMIT", command= self.submit_data, bg="green")
        submit_button.place(x=35, y=400)


    # Define the data for submit
    def submit_data(self):
        # Get the entered data for Basic information
        user_name = self.name_entry.get()
        user_age = self.age_entry.get()
        user_birthday = self.bday_entry.get()
        date = self.date_entry.get()

        # Get the entered data for Contact information
        user_contact_num = self.cont_num_entry.get()
        user_email = self.email_ad_entry.get()

        # Get the entered data for Emergency information
        emergency_name = self.emer_name_entry.get()
        emergency_contact_num = self.emer_cont_num_entry.get()
        emergency_email = self.emer_email_add_entry.get()
        relationship = self.relation_entry.get()

        # Get the entered data for Travel Declaration
        travel = self.travel_choice.get()
        transmission = self.transmission_choice.get()
        relative = self.relative_choice.get()

        # Get the entered data for Health Declaration
        vaccine = self.vaccine_choice.get()
        symptoms = self.symptoms_choice.get()
        exposure = self.exposure_choice.get()
        tested = self.tested_choice.get()

        # Save the file using CVS
        with open('entry.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user_name, user_age, user_birthday, date, user_contact_num, user_email, 
                             emergency_name, emergency_contact_num, emergency_email, relationship,  
                             travel, transmission, relative, vaccine, symptoms, exposure, tested])
           
            # Create notification for user
            if travel == "No" and relative == "No" and symptoms == "No" and transmission == "No" and exposure == "No":
                # Display that you are not a close contact and not a covid positive
                window4 = LastFrame(self.master)
                window4.pack(fill="both", expand=True)
            else:
                # Display that you are not a close contact and not a covid positive
                window4 = LastFrame(self.master)
                window4.pack(fill="both", expand=True)

 
         
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
        self.cont_num_entry.delete(0, tk.END)
        self.cont_num_entry.config(fg="black")
    def clear_email_ad_text(self, event):
        self.email_ad_entry.delete(0, tk.END)
        self.email_ad_entry.config(fg="black")
    def clear_relation_ad_text(self, event):
        self.relation_entry.delete(0, tk.END)
        self.relation_entry.config(fg="black")
    def clear_emer_name_text(self, event):
        self.emer_name_entry.delete(0, tk.END)
        self.emer_name_entry.config(fg="black")
    def clear_emer_cont_num_text(self, event):
        self.emer_cont_num_entry.delete(0, tk.END)
        self.emer_cont_num_entry.config(fg="black")
    def clear_emer_email_add_text(self, event):
        self.emer_email_add_entry.delete(0, tk.END)
        self.emer_email_add_entry.config(fg="black")
