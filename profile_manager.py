#profile_manager.py
#CS314
#Doctor Patient Management System
#This file holds the profile manager class. This class is responsible for managing profiles in the data system.
#Including creating and deleting doctor and manager profiles and changing member's statuses. 

from parent import parent


class profile_manager(parent):
    #this function specifically adds a new doctor profile
    def add_new_doctor_profile(self):
        self.add_new_profile("doctor")
    

    #this function specifically adds a new member profile
    def add_new_member_profile(self):
        self.add_new_member_profile


    #this function adds a new profile to the data system, returns True for success or False for not added
    #pass in "member" or "doctor" for the profile type
    def add_new_profile(self, type):
        name = "" #to store the doctors name
        no_spaces_name = "" #used to store the person's name but replaces the spaces with under scores to be used for the file name
        id_num = "" #to store the doctors ID number
        street = ""
        city = ""
        state = ""
        zip = ""

        print("You select to create a new doctor profile.")
        #store id number entered from manager in id_num
        name = super().get_text(f"\nEnter the {type}'s full name: ")
        id_num = super().get_id_num(type) #makes sure id is not already taken and is valid
        print(f"Enter the following for the {type}'s address.")
        street = super().get_text(f"\nEnter the {type}'s street: ")
        city = super().get_text(f"\nEnter the {type}'s city: ")
        state = super().get_text(f"\nEnter the {type}'s state: ")
        zip = super().get_text(f"\nEnter the {type}'s zip code: ")

        #construct file name
        no_spaces_name = name.replace(" ", "_") #replaces spaces with underscores
        file_name = f"{id_num}_{type}_{no_spaces_name}_profile.txt" #creates text file name

        #create and open the file in write mode
        with open(file_name, 'w') as file:
            file.write(f"{name}\n") #write the name on the second line of the file
            file.write(f"{id_num}\n") #write the id number on the first line of the file
            file.write(f"{street}\n") #write the street to the file
            file.write(f"{city}\n")
            file.write(f"{state}\n")
            file.write(f"{zip}\n")

            if type == "member":
                file.write("Status: Valid") #if it is a member profile, write into the file their valid status
        
        print(f"\n{type.capitalize()} profile created.\n")

        #display file contents, if file not found...
        if not super().display_file_contents(file_name):
            print("Error: file not found in directory after creating doctor profile.")