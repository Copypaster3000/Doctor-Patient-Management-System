#menus_n_modes.py
#CS314
#This class is in charge of displaying all the high level menu options and organizing all the other classes and their functions
#to be called correctly based on the user's menu choices.

from parent import parent
from profile_manager import profile_manager
from services_manager import services_manager
from member_reports import member_reports as mp
from provider_reports import provider_reports


class menus_n_modes(parent):
    #class constructor to initialize other class objects to utilize 
    def __init__(self):
        self.parent_object = parent() #an instance of the parent class to use it's functions
        self.profile_edits = profile_manager() #an instance of profile manager to use it's functions to manage profiles in the data base
        self.services = services_manager() # instance of services manager to use its functions to manager and view services in the data base
        self.member_reports = mp() #JO: an instance of member reports class to use its functions
        self.provider_reports = provider_reports()


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
        while (choice != 14):
            print("\nManger Mode")
            print("Select an option form the menu:")
            print("1) Generate a doctor's weekly services report")
            print("2) Generate a member's weekly services report")
            print("3) Generate a provider summary report for all doctors")
            print("4) Generate a weekly ETF report")
            print("5) Create a new doctor profile")
            print("6) Create a new member profile")
            print("7) Edit an existing doctor profile")
            print("8) Edit an existing member profile")
            print("9) Remove an existing doctor profile")
            print("10) Remove an existing member profile")
            print("11) Change a member's status")
            print("12) Add a service to the services directory")
            print("13) Remove a service from the services directory")
            print("14) Exit Manager Mode")
            choice = self.parent_object.get_menu_choice(14) #get users menu choice

            #call appropriate function based on users menu choice
            if (choice == 2): self.member_reports.generate_member_report() #JO
            if (choice == 4): self.provider_reports.generate_EFT_report()
            if (choice == 5): self.profile_edits.add_new_doctor_profile()
            if (choice == 6): self.profile_edits.add_new_member_profile()
            if (choice == 7): self.profile_edits.edit_doctor_profile()
            if (choice == 8): self.profile_edits.edit_member_profile()
            if (choice == 9): self.profile_edits.remove_doctor_profile()
            if (choice == 10): self.profile_edits.remove_member_profile()
            if (choice == 11): self.profile_edits.edit_member_status()
            if (choice == 12): self.services.add_service()
            if (choice == 13): self.services.remove_service()



        print("\nExited Manager Mode") #notifies user they have exited manager mode


    #displays provider menu and facilitate provider mode functionality 
    def provider_menu(self):
        choice = -1 #stores users menu choice

        #while user hasn't chosen to exit provider mode
        while (choice != 3):
            print("\nProvider Mode")
            print("Select an option from the menu:")
            print("1) Log a member service")
            print("2) View services directory")
            print("3) Exit provider mode")
            choice = self.parent_object.get_menu_choice(3) #gets user's menu choice
            
            if (choice == 2): self.services.view_service_directory()

        print("Exited Provider Mode\n") #notifies user they have exited provider mode

            

        
