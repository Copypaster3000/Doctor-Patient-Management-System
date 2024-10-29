#menus_n_modes.py
#CS314
#This class is in charge of displaying all the high level menu options and organizing all the other classes and their functions
#to be called correctly based on the user's menu choices.


from parent import parent
from profile_manager import profile_manager

class menus_n_modes(parent):
    #class constructor to initialize other class objects to utilize 
    def __init__(self):
        self.parent_object = parent() #an instance of the parent class to use it's functions
        self.profile_edits = profile_manager() #an instance of profile manager to use it's functions to manage profiles in the data base

    #displays main menu and returns the user's menu choice
    def main_menu(self):
        choice = -1 
        print("\nChoc Anon Main Menu: ")
        print("1) Manager Mode")
        print("2) Provider Mode")
        print("3) Exit program")
        choice = self.parent_object.get_menu_choice(3)

        return choice


    #displays manger menu and facilitates manager mode functionality
    def manager_menu(self):
        choice = -1 #to hold users menu choice

        #while the user hasn't chosen to exit manager mode
        while (choice != 12):
            print("\nManger Mode")
            print("Select an option form the menu:")
            print("1) Generate a doctor's weekly services report")
            print("2) Generate a member's weekly services report")
            print("3) Generate a provider summary report for all doctors")
            print("4) Generate a weekly ETF report")
            print("5) Create a new doctor profile")
            print("6) Create a new member profile")
            print("7) Remove an existing doctor profile")
            print("8) Remove an existing member profile")
            print("9) Change a members status")
            print("10) Add a service to the services directory")
            print("11) Remove a service from the service directory")
            print("12) Exit Manager Mode")
            choice = self.parent_object.get_menu_choice(12) #get users menu choice

            #call appropriate function based on users menu choice
            if (choice == 5): self.profile_edits.add_new_doctor_profile()
            if (choice == 6): self.profile_edits.add_new_member_profile()

        print("Exited Manager Mode\n") #notifies user they have exited manager mode


    #displays provider menu and facilitate provider mode functionality 
    def provider_menu(self):
        choice = -1 #stores users menu choice

        #while user hasn't chosen to exit provider mode
        while (choice != 3):
            print("Provider Mode")
            print("Select an option from the menu:")
            print("1) Log a member service")
            print("2) View services directory")
            print("3) Exit provider mode")
            choice = self.parent_object.get_menu_choice(3) #gets user's menu choice

        print("Exited Provider Mode\n") #notifies user they have exited provider mode

            

        
