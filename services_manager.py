#services_manager.py
#Doctor Patient Management System
#This file holds the services_manager class. The services_manager class enables adding and remove a service from the 
#service directory, options available in Manager Mode and viewing the service directory, possible in Provider Mode.


from parent import parent 
import os


# manages the service directory, which is stored as a single .txt file
# allows for adding a new service, remove an existing service, and viewing the service directory
class services_manager(parent):

    # initialize class and ensure the service directory text file exists, if not, create it
    def __init__(self):
        self.service_directory = "services.txt" # txt file where service directory is stored

        # if a service directory does not exists yet, need to create one
        if not os.path.isfile(self.service_directory):
            with open(self.service_directory, 'w') as file: # create an empty service directory file, not writing anything into it 
                pass  
         
         
    # checks if the given service code is a valid 6 digit number
    def is_6_digits(self, service_code): 
        # return true if service code has 6 numbers, false if not
        return len(service_code) == 6 and service_code.isdigit()
        
        
    # gets the 6 digit service code 
    def get_6_digits(self): 
        service_code = input("Enter 6 digit service code: ") # get user input

        # while the service code entered isnt 6 digits, reprompt
        while not self.is_6_digits(service_code):
            service_code = input("Invalid input: Enter 6 integers: ")

        # return 6 digit validated service code 
        return service_code
        
        
    # ads a new service (name, fee, & cost) to the service directory
    def add_service(self):
        print("\nYou have selected to add a new service ")
        service_name = self.get_valid_service_name() # get and validate a service name
        service_code = self.get_valid_service_code()  # get and validate a service code 
        service_fee = super().get_text("Lastly, enter the service fee: ")

        # add the new service to the directory
        with open(self.service_directory, 'a') as file:
            file.write(f"{service_name},{service_code},{service_fee}\n")

        # display added service back to user
        print(f"ChocAn service '{service_name}' added successfully")


    # removes an existing service 
    def remove_service(self):
        # manager may want to view service directory before removing anything
        print("\nWould you like to view the service directory before proceeding?\n 1) Yes \n 2) No")
        choice = super().get_menu_choice(2)
        if choice == 1: self.view_service_directory()
        
        print("\nTime to remove a service")
        
        valid = False  # used to validate service code before removal
        # loop until valid service code is entered 
        while not valid:
            service_code = self.get_6_digits()  # get service code to remove

            # check if the service already exists in directory
            if not self.service_code_exists(service_code):
                print(f"No service found that matches code {service_code}. Please try again.")
            else:
                valid = True  # exit loop once valid service code is provided

        # load all services and find service that has correspodning service code
        updated_services = []
        # open service directory text file to read
        with open(self.service_directory, 'r') as file:
            # each line aka a sercive 
            for line in file:
                # strip the name, code and fee 
                service_name, code, fee = line.strip().split(',')
                
                # allow user to reconsider removal of a service
                if code == service_code:
                    print(f"\nService Found: {service_name} (Code: {service_code}, Fee: {fee})")
                    print("Are you sure you want to delete this service? \n 1) Yes \n 2) No")
                    choice = self.get_menu_choice(2)
                    
                    # user changed their mind, quit removal process
                    if choice == 2:
                        print("Removal of service has been cancelled")
                        return
                else:
                    # add to updated list of service 
                    updated_services.append(line.strip())

        # rewrite to the service directory with the updated list of services after removal
        with open(self.service_directory, 'w') as file:
            for service in updated_services: # each "service" contains the name,code,fee
                file.write(service + '\n')
                
        # confirmation message of service removed
        print(f"Service, {service_name} with code {service_code} removed successfully.")


    # display the entire ChocAn service directory
    def view_service_directory(self):
        # read the service directory (a .txt file)
        with open(self.service_directory, 'r') as file: 
            services = file.readlines()

        # handles rare case of the service directory being empty
        if not services:
            print("The ChocAn service directory is empty. Proceed to Manager Mode to add some services.")
            return

        print("\nAvailable ChocAn Services:")
        # loop through each line and display the services
        for line in services:
            service_name, service_code, service_fee = line.strip().split(',')
            print(f" - {service_name} (Code: {service_code}, Fee: ${service_fee})")
            
    
    # gets a valid service name from the user 
    def get_valid_service_name(self):
        valid = False # used to confirm if service name is valid

        # while the service name the user entered is still invalid, keep prompting and validating
        while not valid:
            service_name = super().get_text("Enter the service name: ")
            # check if the service name already exists
            if self.service_name_exists(service_name):
                print(f"A service under the name '{service_name}' already exists. Try adding a new one.")
            else:
                valid = True # service name is valid, end loop

        # return validated service name
        return service_name 
    
    
    # simply confirms if user is happy with their input ~ used throughout this class
    def confirm_input(self, user_input):
        # while the user correctly enters 1 or 2
        while True:
            print(f'You entered "{user_input}".')
            print("1) Continue")
            print("2) Re-enter info")
            choice = super().get_menu_choice(2)
            
            if choice == 1: return True # true if user is satisfied with their input
            else: return False # false if user is not satisfied

    
    # checks if a service is already provided 
    def service_name_exists(self, service_name):
        # open the service directory text file to read 
        with open(self.service_directory, 'r') as file:
            # loop through each line ( a service  )
            for line in file:
                # strip the first value aka name from the line
                name, _, _ = line.strip().split(',')
                # check if names match
                if name.lower() == service_name.lower(): 
                    return True # return true if the service name already exists
                
        return False # return false if the name doesnt exist


    # this function gets a valid 6 digit code, ensuring it doesnt already exists in the directory
    def get_valid_service_code(self):
        valid = False # false till valid & user satisfied service code is entered 

        # while the service code is still invalid, keep prompting and validating
        while not valid:
            # get service code & make sure its 6 digits
            service_code = self.get_6_digits()
            # confirm with user
            if not self.confirm_input(service_code):
                print("Let's try again.")
                continue

            # check if service code already exists in directory
            if self.service_code_exists(service_code):
                print(f"A service with the code {service_code} already exists. Please try again.")
            else:
                valid = True # service code is valid, end loop

        return service_code # return the validated service code
    
    
    # checks if a service code is already in use
    def service_code_exists(self, service_code):
        # read the service directory text file 
        with open(self.service_directory, 'r') as file:
            # for each line aka service
            for line in file:
                _, code, _ = line.strip().split(',') # only care about service code
                
                if code == service_code: # compare 
                    return True # return true if the service code is already in use
                
        return False # return false it the code is not in use
    
    # Get the details of a service corresponding to the code passed as argument.
    def get_service_info_from_code(self, service_code): #TODO is iterating thru every line like this too computationally ridiculous?
        with open(self.service_directory, 'r') as  file:
            for line in file:
                (name,code, fee) = line.strip().split(',')
                if code == service_code:
                    return (name, fee) # Return the service name
        return None
