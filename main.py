#main.py
#Doctor Patient Management System
#This is the main file of the program, responsible for organizing the program on the highest level
#nikki's comment for test commit

from parent import parent
from menus_n_modes import menus_n_modes


def main():
    choice = -1 #to hold menu choices 
    menus = menus_n_modes()

    #loops while the user hasn't chosen to exit the program
    while(choice != 3):
        choice = menus.main_menu() #displays main menu to user and stores menu choice

        #goes to manager menu if use chose that, where all manager mode functionality will be handled
        if (choice == 1): menus.manager_menu()

        #goes to provider menu if user chose that, where all provider mode functionality will be handled
        if (choice == 2): menus.provider_menu()

    #Lets user know the program has officially ended after the exited the while loop by enter 3 to exit the program
    print("\nThe program has ended.\n")





if __name__ == "__main__":
    main()