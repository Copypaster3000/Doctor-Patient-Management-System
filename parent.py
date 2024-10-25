#system_user.py
#Choc An project
#This class holds all of the reusable functions, mainly for accessing files. This class is also the parent class to the manager and provider class which will facilitate manager and provider mode.

import os

class parent:
    #get's and returns an int as a menu choice from user. pass in the number of valid menu choices
    #make sure to display the menu options BEFORE calling this function
    def get_menu_choice(self, choices):
        valid = False #to hold wether input is valid
        
        
        while not valid:
            try: 
                #get user input and convert to int
                choice = int(input("Enter menu choice as an integer: "))

                #check if the choice is valid (between 1 and choices)
                if 1 <= choice <= choices:
                    valid = True
                else:
                    print(f"Invalid input. Enter a number between 1 and {choices}.")
            except ValueError:
                #if the input was not an int, catch the exception
                print("Invalid input. Please enter a valid integer.")

        return choice #return valid menu choice as an int

    #this function display the contents of a file, returns true for success or false for file not found
    def display_file_contents(self, file_name):
        try:
            #open the file in read mode and display its contents
            with open(file_name, 'r') as file:
                contents = file.read()
                print(contents)
                return True #for success
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
            return False #for file not found

    #This function is not needed as a function, it's one line just use that line
    #def file_exists(self, file_name):
        #return os.path.exists(file_name)


    #this gets a valid ID number from the user and returns it, pass in "doctor" or "member" depending on who the ID number is for
    def get_id_num(self, user):
        done = False #variable used to confirm if the user is happy with the ID number
        choice = 0 #used to hold users choice to enter id number again or continue

        #prompts for ID number
        id_num = input(f"\nEnter the {user}'s ID number: ")

        while not done:
            if not self.is_9_digits(id_num):
                id_num = input("The ID number must be nine digits, enter a valid ID number: ")
            elif self.person_exists(id_num):
                id_num = input("That ID number is already in use, enter another ID number: ")
            else: #if id num is not taken and is 9 digits set done to true
                done = True

            if done: 
                print(f"You entered: {id_num}")
                print("Would you like to continue and use that ID number or enter a different ID number?")
                print("1) Continue")
                print("2) Enter a different ID number")
                choice = self.get_menu_choice(2)

                if choice == 2:
                    done = False
                else:
                    done = True

        return id_num

    
    #this class returns true is a profile exists with the identification number passed in and false if not
    def person_exists(self, id_number):
        #get the current working directory
        current_directory = os.getcwd()

        #put all files in current directory into a list
        try: 
            files = os.listdir(current_directory)
            #iterate through the files and chick if any already has the id number
            for file in files:
                if (file[:5] == id_number): return True #return true if a match is found
            
            return False #id number not in use
        except FileNotFoundError:
            print("Error searching directory for file.")
            return False


    #used to check that an ID number is 9 digits in a string, nothing more or less, returns true if it is, false if not 
    def is_9_digits(self, num_str):
        #check if the string length is 5 and all characters are digits
        return len(num_str) == 9 and num_str.isdigit()
            
    

    #pass in the prompt to get text from the user
    #this function will use the prompt to get the correct input and check with the user until they are satisfied with the input
    #and then will return in
    def get_text(self, prompt):
        choice = 0 #to hold user's menu choice
        to_return = "" #to hold user input

        #loops while the user is not happy with their input
        while(choice != 1):
            to_return = input(prompt)
            print(f"You entered '{to_return}'")
            print("1) Continue")
            print("2) Re-enter info")
            choice = self.get_menu_choice(2)

        #returns string of user input they are happy with
        return to_return 

