#provider_reports.py
#Doctor Patient Management System
#This file contains the provider_reports class. This class is responsible for generating reports specific to providers.
#Including generating a doctor's weekly service report, generating a provider summary report for all doctors, and generating
#a weekly ETF report. All of which will be available through Manager Mode.

#def generate_provider_summary_report(): #high level menu option
#def generate_provider_service_report(): #high level menu option
#def generate_EFT_report(): #high level menu option
#def get_provider(): #get a provider the user wants to generate a provider service report for, and validate user input
#def chronological_sort(): #sort services in a file by chronological order by day the service was provided
#def display_provider_service_report() #displays the provider service report text file
#def display_proiver_summary_report(): #displays the provider summary report
#def get_name_by_id_num(self, id_number):#returns the name of a doctor based on their id number
#def copy_and_rename_file(self, original_file, new_file_name):#copies and re-names a file
#def insert_line_in_file(file_path, line_number, new_line):#Inserts a new line at a specific line number in a file without disrupting the rest of the file.

import shutil
import os
from parent import parent
from datetime import date

    #123456789_doctor_name_template_provider_service_report_MM_DD_YYYY.txt

class provider_reports(parent):
    def generate_provider_summary_report(self): #high level menu option
        #get date range of the summary report from the user
        #find all doctor profiles will services logged in that range (probably a recursisve algorithim)
        #as services in that range are found, copy service and doctor information to local variables

        return
    def get_name_by_id_num(self, id_number):#returns the name of a doctor based on their id number
        # Get the current working directory
        current_directory = os.getcwd()

        try:
            # List all files in the current directory
            files = os.listdir(current_directory)

            # Iterate through the files to find a match
            for file in files:
                # Check if the first 9 characters of the filename match the id_number
                if file[:9] == id_number:
                    # Extract the portion of the filename between the first '_' and '_profile'
                    if "_profile" in file:
                        name_with_role = file[file.find("_") + 1:file.rfind("_profile")]
                        # Remove the role (e.g., "doctor_") from the start of the name
                        name = name_with_role.split("_", 1)[1]
                        return name

            # Return False if no file matches the id_number
            return False
        except FileNotFoundError:
            print("Error: Directory not found.")
            return False
    
    def generate_provider_service_report(self): #high level menu option
        #get provider from user
        print("please enter the ID number of the provider you wish to generate a service report for:")
        id_num = super().get_9_digits()
        while(super().person_exists(id_num) == False):
            print("there is not provider in the system with that ID number.")
            print("what would you like to do?")
            print("1) re-enter ID number")
            print("2) return to menu")
            choice = super().get_menu_choice(2)
            if(choice == 1):
                print("please enter the ID number of the provider you wish to generate a service report for:")
                id_num = super().get_9_digits()
            if(choice == 2):
                return
        #get current date from system for the report file name
        current_date = date.today()
        #format date
        formatted_date = current_date.strftime("%Y_%m_%d")  # Example: "2024-12-02"
        name = self.get_name_by_id_num(id_num)#returns the name of a doctor based on their id number

        #format the file name of the newly generated report
        new_file_name = f"{id_num}_{name}_provider_service_report_{formatted_date}.txt" #creates text file name
        #use file_exisits to get the path to the current doctor profile
        old_file = super().file_exists(id_num, "doctor", "profile")
        #copy doctor profile and rename it as a report
        self.copy_and_rename_file(old_file, new_file_name)
        self.add_labels(new_file_name)

    def copy_and_rename_file(self, original_file, new_file_name):#copies and re-names a file
        # Get the current working directory
        current_directory = os.getcwd()

        # Full paths for the original and new file
        original_path = os.path.join(current_directory, original_file)
        new_file_path = os.path.join(current_directory, new_file_name)
        try:
            # Copy the original file and rename it
            shutil.copy(original_path, new_file_path)
            print(f"File copied and renamed to: {new_file_name}")
            return new_file_path
        except FileNotFoundError:
            print(f"Error: {original_file} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
            #check if provider exists
        return
    
    def add_labels(self, file_name):
        #define labels to insert infront of data 
        name = "First and last name: "
        id_num = "ID number: "
        adress = "Adress: "
        date_and_time_service_was_recorded = "Date and time service recorded: "
        date_service_was_provided = "Date service was provided: "
        provider_num = "Provider number: "
        member_num = "Member number: "
        service_code = "Service code: "
        fee = "Fee: "
        commments = "Comments: "
        #get name from file and add it to string with label
        name = name + super().get_line_of_file(file_name, 0)
        #rewrite line in file with new string
        super().overwrite_line_in_file(file_name, 0, name)
        #get id number from file and add it to a string with label
        id_num = id_num + super().get_line_of_file(file_name, 1)
        #rewrite line in file with new string
        super().overwrite_line_in_file(file_name, 1, id_num)

        # Get the current working directory
        current_directory = os.getcwd()
        # get full path for the file
        file_path = os.path.join(current_directory, file_name)
        #insert a new line before the adress with the adress label
        self.insert_line_in_file(file_path, 3, adress)

       #iterate through file adding labels to any services listed 
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            with open(file_name, 'r') as file:
                for line_number, line in enumerate(file, start=1):  # start=1 makes line_number start from 1
                    # starting at line 9 and every 8 lines after that
                    if line_number >= 9 and (line_number - 9) % 8 == 0:
                        date_and_time_service_was_recorded = date_and_time_service_was_recorded + super().get_line_of_file(file_name, line_number)
                        super().overwrite_line_in_file(file_name, line_number, date_and_time_service_was_recorded)
        except FileNotFoundError:
                print(f"Error: File '{file_path}' not found.")
        except Exception as e:
                print(f"An error occurred: {e}")

    def insert_line_in_file(self, file_path, line_number, new_line):#Inserts a new line at a specific line number in a file without disrupting the rest of the file.
        try:
            # Open the file for reading and store its contents in a list
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Insert the new line at the desired position
            lines.insert(line_number - 1, new_line + '\n')  # Adjust for 1-based indexing

            # Write the modified contents back to the file
            with open(file_path, 'w') as file:
                file.writelines(lines)
                return True
        #print(f"Line inserted at position {line_number} successfully.")
        except FileNotFoundError:
         print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def generate_EFT_report(self): #high level menu option
        return
    def get_provider(self): #get a provider the user wants to generate a provider service report for, and validate user input
        return
    def get_date_range(self):#get date range from user for the report
        return
    def chronological_sort(self): #sort services in a file by chronological order by day the service was provided
        return
    def display_provider_service_report(self): #displays the provider service report text file
        return
    def display_proiver_summary_report(self): #displays the provider summary report
        return
    
