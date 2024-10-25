#main.py
#Choc Anon Project

from parent import parent
from manager import manager
from provider import provider


def main():
    choice = -1
    parent_object = parent()
    manager_object = manager()
    provider_object = provider()


    while(choice != 3):
        print("\nChoc Anon Main Menu: ")
        print("1) Manager Mode")
        print("2) Provider Mode")
        print("3) Exit program")
        choice = parent_object.get_menu_choice(3)

        if (choice == 1): manager_object.manager_mode()
        if (choice == 2): provider_object.provider_mode()

    print("\nProgram ended.")






if __name__ == "__main__":
    main()