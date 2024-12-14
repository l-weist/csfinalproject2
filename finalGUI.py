from tkinter import *
import csv
import sys

class Gui:
    def __init__(self, window):
        self.window = window
        self.showingData = False
        self.isSaving = False
        self.frame_one = Frame(self.window)
        self.label_askName = Label(self.frame_one, text='Name*')
        self.input_name = Entry(self.frame_one)
        self.input_name.pack(side='right')
        self.label_askName.pack()
        self.frame_one.pack()
        
        self.frame_two = Frame(self.window)
        self.label_askMajor = Label(self.frame_two, text='Major')
        self.input_major = Entry(self.frame_two)
        self.input_major.pack(side='right')
        self.label_askMajor.pack()
        self.frame_two.pack()
        
        self.frame_three = Frame(self.window)
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.radio_2025 = Radiobutton(self.frame_three, text='2025', variable=self.radio_answer, value=1)
        self.radio_2026 = Radiobutton(self.frame_three, text='2026', variable=self.radio_answer, value=2)
        self.radio_2027 = Radiobutton(self.frame_three, text='2027', variable=self.radio_answer, value=3)
        self.radio_2028 = Radiobutton(self.frame_three, text='2028', variable=self.radio_answer, value=4)
        self.label_graduationYear = Label(self.frame_three, text = "Graduation Year*")
        self.label_graduationYear.pack(side='left')
        self.radio_2025.pack(side='left')
        self.radio_2026.pack(side='left')
        self.radio_2027.pack(side='left')
        self.radio_2028.pack(side='left')
        self.frame_three.pack()
        
        self.window = window
        self.frame_four = Frame(self.window)
        self.label_email = Label(self.frame_four, text='School Email*')
        self.input_email = Entry(self.frame_four)
        self.input_email.pack(side='right')
        self.label_email.pack()
        self.frame_four.pack()

        self.frame_five = Frame(self.window)
        self.radio_option = IntVar()
        self.radio_option.set(0)
        self.radio_coffee = Radiobutton(self.frame_five, text='Coffee date', variable=self.radio_option, value=1)
        self.radio_openHouse = Radiobutton(self.frame_five, text='Open House', variable=self.radio_option, value=2)
        self.radio_both = Radiobutton(self.frame_five, text='Both', variable=self.radio_option, value=3)
        self.label_meeting = Label(self.frame_five, text='Meeting Type*')
        self.label_meeting.pack(side='left')
        self.radio_coffee.pack(side='left')
        self.radio_openHouse.pack(side='left')
        self.radio_both.pack(side='left')
        self.frame_five.pack()

        self.frame_six = Frame(self.window)
        self.button_save = Button(self.frame_six, text='SAVE', command=self.submit)
        self.button_save.pack(side='left')
        self.frame_six.pack()
        self.frame_six = Frame(self.window)
                
        self.frame_options = Frame(self.window)
        self.button_show = Button(self.frame_options, text='Show Data', command=self.show)
        self.button_show.pack(side='left')
        
        self.button_Filter = Button(self.frame_options, text='Filter By Year', command=self.year)
        self.button_Filter.pack(side='left')
        
        self.button_pref = Button(self.frame_options, text='Filter By Preference', command=self.pref)
        self.button_pref.pack(side='left')
        
        self.frame_options.pack()
        
        self.window = window
        self.frame_info = Frame(self.window)
        self.label_info = Label(self.frame_info, text='')
        self.label_info.pack()
        self.frame_info.pack()

    def submit(self):
        print(f"submit button, getting show... {self.showingData}")
        name = self.input_name.get().strip()
        major = self.input_major.get()
        gradYear = self.radio_answer.get()
        email = self.input_email.get().strip()
        option = self.radio_option.get()
        print(f"info submitted, waiting to update... {self.showingData}")
        
        if major == '':
            major = "Undecided"
        
        if gradYear == 0:
            gradYear = "NA"
        elif gradYear == 1:
            gradYear = 2025
        elif gradYear == 2:
            gradYear = 2026
        elif gradYear == 3:
            gradYear = 2027
        elif gradYear == 4:
            gradYear = 2028
            
        if option == 0:
            option = "NA"
        elif option == 1:
            option = "Coffee date"
        elif option == 2:
            option = "Open house"
        elif option == 3:
            option = "Both"
        
        try:
            
            if name == '':
                raise ValueError("Please fill out all * fields")
            elif email == '':
                raise ValueError("Please fill out all * fields")
            elif "@unomaha.edu" not in email:
                raise NameError("Please enter a valid email")
            elif option == 'NA':
                raise ValueError("Please fill out all * fields")
            elif gradYear == 'NA':
                raise ValueError("Please fill out all * fields")
            elif option == 'NA':
                raise ValueError("Please fill out all * fields")
            
            else:
                with open("recruitment.csv", mode = "a", newline="\n") as output:
                    writer = csv.writer(output)
                    writer.writerow([name, major, gradYear, email, option])
                    print("info is written")
                self.button_save.config(text = "SAVE")
            
                print("checking for real-time update...")
                if self.showingData == False:
                    self.label_info.config(text = '')
                    self.button_show.config(text = 'Show Data')
                    print("not updating in real time")
                else:
                    print("updating in real time")
                    self.isSaving = True
                    self.show()
               
        except ValueError:
            self.button_save.config(text = "Please fill out all * fields")
        except NameError:
            self.button_save.config(text = "Please enter a valid email")

        self.input_name.delete(0, END)
        self.input_major.delete(0, END)
        self.input_email.delete(0,END)
        self.radio_answer.set(0)
        self.radio_option.set(0)
        self.input_name.focus_set()
        self.button_pref.config(text = "Filter By Preference")
        self.button_Filter.config(text = "Filter By Year")
        self.button_show.config(text = "Show Data")
        
    def year(self):
        print(f"sorting year, getting show...{self.showingData}")
        self.showingData = False
        self.isSaving = False
        
        self.label_info.config(text = '')
        self.button_show.config(text = 'Show Data')
        print(f"year sorting. hiding data (show = {self.showingData})")
        gradYear = self.radio_answer.get()
        found = []
        
        if gradYear == 0:
            gradYear = "NA"
        elif gradYear == 1:
            gradYear = '2025'
        elif gradYear == 2:
            gradYear = '2026'
        elif gradYear == 3:
            gradYear = '2027'
        elif gradYear == 4:
            gradYear = '2028'
        
        try:
            with open("recruitment.csv", "r") as output:
                reader = csv.reader(output)
                for row in reader:
                    info = row
                    
                    if gradYear == "NA":
                        self.button_Filter.config(text = "Select a year")
                        
                    elif row[2] == gradYear:
                        self.button_Filter.config(text = "Filter By Year")
                        self.button_pref.config(text = "Filter By Preference")
                        self.button_show.config(text = "Show Data")
                        found.append(row)
                        
            displayList = []
            
            for person in found:
                person = " | ".join(person)
                displayList.append(person)
                
            displayList = "\n".join(displayList)
            self.label_info.config(text = displayList)
        
        except FileNotFoundError:
            self.button_Filter.config(text = "File not found, enter information")
        
        self.input_name.delete(0, END)
        self.input_major.delete(0, END)
        self.input_email.delete(0,END)
        self.radio_answer.set(0)
        self.radio_option.set(0)
        self.input_name.focus_set()
        
    def show(self):
        print(f"displaying, checking show...{self.showingData}")
        
        if self.button_show['text'] == "Show Data" and self.showingData == False:
            print(f"button says {self.button_show['text']}")
            self.showingData = True
            try:
                with open("recruitment.csv", "r") as output:
                    reader = csv.reader(output)
                    displayList = []
                    for person in reader:
                        info = " | ".join(person)
                        displayList.append(info)
                    
                displayList = "\n".join(displayList)
                print("displaying data")
                self.label_info.config(text = displayList)
                self.button_show.config(text = 'Hide Data')
            
            except FileNotFoundError:
                self.button_show.config(text = "File not found, enter information")
                
            print(f"show = {self.showingData}")
            self.button_show.config(text = 'Hide Data')
        
        elif self.button_show['text'] == "Hide Data" and self.showingData == True and self.isSaving == False:
            print(f"button says {self.button_show['text']}")
            self.button_show.config(text = 'Show Data')
            print(f"hiding data")
            self.label_info.config(text = '')
            self.showingData = False
        
        elif self.isSaving == True and self.showingData == True:
            print("info is displayed, saving new info")
            print(f"button says {self.button_show['text']}")
            self.showingData = True
            try:
                with open("recruitment.csv", "r") as output:
                    reader = csv.reader(output)
                    displayList = []
                    for person in reader:
                        info = " | ".join(person)
                        displayList.append(info)
                    
                displayList = "\n".join(displayList)
                print("displaying data")
                self.label_info.config(text = displayList)
                self.button_show.config(text = 'Hide Data')
            except FileNotFoundError:
                self.button_show.config(text = "File not found, enter information")
                
            print(f"show = {self.showingData}")
            self.button_show.config(text = 'Hide Data')
        
        
        self.input_name.delete(0, END)
        self.input_major.delete(0, END)
        self.input_email.delete(0,END)
        self.radio_answer.set(0)
        self.radio_option.set(0)
        self.input_name.focus_set()
        print(f"display, checking show...{self.showingData}")
        
    def pref(self):
        self.showingData = False
        self.isSaving = False
        self.label_info.config(text = '')
        self.button_show.config(text = 'Show Data')
        
        print(f"preference, hiding data (show = {self.showingData})")
        option = self.radio_option.get()
        found = []
        
        if option == 0:
            option = "NA"
        elif option == 1:
            option = "Coffee date"
        elif option == 2:
            option = "Open house"
        elif option == 3:
            option = "Both"
        
        try:
            with open("recruitment.csv", "r") as output:
                reader = csv.reader(output)
                for row in reader:
                    info = row
                    
                    if option == "NA":
                        self.button_pref.config(text = "Select a preference")
                        
                    elif row[4] == option:
                        self.button_pref.config(text = "Filter By Preference")
                        self.button_Filter.config(text = "Filter By Year")
                        self.button_show.config(text = "Show Data")
                        found.append(row)
                        
            displayList = []
            
            for person in found:
                person = " | ".join(person)
                displayList.append(person)
                
            displayList = "\n".join(displayList)
            self.label_info.config(text = displayList)
        
        except FileNotFoundError:
            self.button_pref.config(text = "File not found, enter information")
        
        self.input_name.delete(0, END)
        self.input_major.delete(0, END)
        self.input_email.delete(0,END)
        self.radio_answer.set(0)
        self.radio_option.set(0)
        self.input_name.focus_set()