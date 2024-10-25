#manager.py
#Choc Anon Project
#This file contains the manager class. This class facilitates manager mode. It is a child of the 'parent' class.

from parent import parent


class manager(parent):

    #this file organizes all the functions of the manager class into a menu to be used for manager mode
    def manager_mode(self):
        choice = -1 #user's menu choice

        while(choice != 9):
            print("\nManger Mode")
            print("Select an option form the menu:")
            print("1) Generate a doctor billing report")
            print("2) Generate a member billing report")
            print("3) Create a new doctor profile")
            print("4) Create a new member profile")
            print("5) Remove a doctor profile")
            print("6) Remove a member profile")
            print("7) Change a member's status")
            print("8) Generate a summary report for all doctors")
            print("9) Quit to go to Main Menu")
            choice = super().get_menu_choice(9)

            if (choice == 3): self.add_new_profile("doctor")
            if (choice == 4): self.add_new_profile("member")

        print("\nManager Mode has been exited.")



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

