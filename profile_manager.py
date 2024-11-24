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
        self.add_new_profile("member")


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
        status = "valid\n" #the status for member's
        notes = "no comments\n" #notes for member's status

        print(f"You selected to create a new {type} profile.")
        #store id number entered from manager in id_num
        name = super().get_text(f"\nEnter the {type}'s full name: ")
        id_num = super().get_unused_id_num(type) #makes sure id is not already taken and is valid
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
                file.write(status) #if it is a member profile, write into the file their valid status
                file.write(notes)
        
        print(f"\n{type.capitalize()} profile created.\n")

        #display file contents, if file not found...
        if not super().display_file_contents(file_name):
            print("Error: file not found in directory after creating doctor profile.")


    #removes a doctor's profile based on user input
    def remove_doctor_profile(self):
        self.remove_profile("doctor")

        return


    #removes a member's profile
    def remove_member_profile(self):
        self.remove_profile("member")

        return


    #this function removes an existing profile, pass in "member" or "doctor" for the type of profile you wish to remove
    def remove_profile(self, type):
        choice = -1 #to holds user's menu choices for the function
        file_name = "" #store entire file name
        name = "" #to store doctor's name

        #prompt user to enter ID num
        print(f"\nEnter the ID number of the {type} whose profile you want to remove.")
        id_num = super().get_9_digits() #get valid 9 digits from user

        #check that a match doctor profile exists, store file name
        file_name = super().file_exists(id_num, type, "profile")

        #if there is no matching doctor profile
        if file_name is None:
            print(f"There is no {type} profile with that ID number.") 
        else: 
            name = super().get_line_of_file(file_name, 0)
            print(f"Profile for {id_num} found.")
            print(f"\nAre you sure you want to delete {type} {name}'s profile?")
            print(f"1) Yes, delete {type} {name}'s profile")
            print(f"2) No, do not delete the {type} profile and return to the manager menu")
            choice = super().get_menu_choice(2)

        if (choice == 2): return  #exit function and return to manager menu if user doesn't want to remove this profile

        if file_name is not None:
            super().delete_file(file_name) #delete profile
            print(f"\n{name}'s {type} profile has successfully been deleted.\n")
        else: 
            print("No profile was deleted.") 

        return

    #allows user to edit all the personal details of a doctors profile
    def edit_doctor_profile(self):
        self.edit_profile("doctor")

        return

    
    #allows user to edit all the personal details of a member profile
    def edit_member_profile(self):
        self.edit_profile("member")

        return


    #to edit a profile pass in "doctor" or "member" for the type of profile to edit
    def edit_profile(self, type):
        print(f"\nEnter the ID number of the {type} whose profile you want to edit.")
        id_num = super().get_9_digits()

        file_name = super().file_exists(id_num, type, "profile")

        if file_name is None: #if there is not an existing profile with that ID number and type
            print(f"There is no profile with that ID number.") #let user know
            return #and return to manager menu

        name = super().get_line_of_file(file_name, 0) #get the name of the profile considering being edited
        #confirm the user wants to edit that persons profile
        print(f"Profile for {id_num} found.")
        print(f"\nAre you sure you want to edit {type} {name}'s profile?")
        print(f"1) Yes, edit {type} {name}'s profile")
        print(f"2) No, do not edit the {type} profile and return to the manager menu")
        choice = super().get_menu_choice(2)

        if (choice == 2):
            print("Okay, returning to manager menu.")
            return

        #allow editing of the following profile details
        super().edit_file_line(0, "name", file_name)
        #the ID number is not allowed to be edited
        super().edit_file_line(2, "street address", file_name)
        super().edit_file_line(3, "city", file_name)
        super().edit_file_line(4, "state", file_name)
        super().edit_file_line(5, "zip code", file_name)

        #if editing a member profile, allow editing of status and comments
        if type == "member": 
            super().edit_file_line(6, "status", file_name)
            super().edit_file_line(7, "comments", file_name)


        print("\nHere is the updated profile: ")

        if type == "member":
            super().display_lines_up_to(file_name, 8)
        else:
            super().display_lines_up_to(file_name, 6)
        


    #allows editing a member's status
    def edit_member_status(self):
        print("\nEnter the ID number of the member whose profile you want to edit.")
        id_num = super().get_9_digits()

        file_name = super().file_exists(id_num, "member", "profile")

        if file_name is None: #if there is not an existing profile with that ID number and type
            print(f"There is no profile with that ID number.") #let user know
            return #and return to manager menu

        name = super().get_line_of_file(file_name, 0) #get the name of the profile considering being edited
        status = super().get_line_of_file(file_name, 6)
        #confirm the user wants to edit that persons profile
        print(f"Profile for {id_num} found, member {name}.")
        print("Profile statuses can only be changed between valid and invalid, choosing to edit will change the status to what is in not.")
        print(f"\nAre you sure you want to change member {name}'s profile status is is currently {status}?")
        print(f"1) Yes, change {name}'s profile status")
        print(f"2) No, do not change {name}'s status")
        choice = super().get_menu_choice(2)

        if (choice == 1): #if the user selected to change the status
            if (status == "valid"): new_status = "invalid"
            else: new_status = "valid"

            #change users status
            super().overwrite_line_in_file(file_name, 6, new_status)
            print(f"\n{name}'s status has been updated to {new_status}.")

        #get status comments from file
        comments = super().get_line_of_file(file_name, 7)
        print(f"\nWould you like to edit the user's status comments? Current comments: '{comments}'.  ")
        print("1) Replace comment with a new comment")
        print("2) No not edit comment, go back to manager menu")
        choice = super().get_menu_choice(2)

        if (choice == 1): #if the user wants to edit the status comments
            #get the replacement comment from the user
            new_comment = super().get_text("\nEnter the new status comment: ")
            super().overwrite_line_in_file(file_name, 7, new_comment)

        print(f"\n{name}'s status and comments: ")
        print(f"Status: {super().get_line_of_file(file_name, 6)}")
        print(f"Comments: {super().get_line_of_file(file_name, 7)}")
        
        

        





        




            



