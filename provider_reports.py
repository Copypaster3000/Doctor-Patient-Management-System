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
#def add_labels(self, file_name):#adds labels to report file
from datetime import date, datetime, timedelta
from parent import parent
import shutil
import glob
import os

#123456789_doctor_name_template_provider_service_report_MM_DD_YYYY.txt

class provider_reports(parent):
    def __init__(self):
        self.doctor_files = self.get_doctor_files()



    def generate_provider_summary_report(): #high level menu option
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

    def remove_outdated_services(self, file_name):
        service_date = None 
        one_week_ago = datetime.now() - timedelta(days=7) #calculate the date one week ago
        try:
            lines = []
            with open(file_name, 'r') as file:
                lines = file.readlines()

                if len(lines) <= 7: return #if there arn't more than 7 lines in the file then there are not services so nothing to delete

                #start processing from line 8
                index = 7 
                #length = len(lines)

                while index < len(lines): #while there are still services to check
                    try:
                        service_date = datetime.strptime(lines[index].strip(), "%m-%d-%Y %H:%M:%S")
                    except ValueError: 
                        print(f"{file_name}: Invalid date format on line {index + 1} found while generating Provider Service report. Skipping that service block.")
                        index += 8

                    if service_date < one_week_ago: #if the service is greater than a week old
                        try: 
                            #remove it
                            if index + 8 <= len(lines):# Check if there are at least 8 lines starting from the current line
                                del lines[index:index + 8]
                                #index = index - 8 #de-increment index to acount of the change in position after lines are removed
                        except FileNotFoundError:
                            print(f"Error: File '{file_name}' not found.")
                        except Exception as e:
                            print(f"An error occurred: {e}")
                    else:
                        index += 8
            with open(file_name, 'w') as file:# Write the modified lines back to the file
             file.writelines(lines)

        except FileNotFoundError:
            print(f"File {file_name} not found wile trying to generate provider service report.")
        except Exception as e:
            print(f"An error occurred while processing {file_name}: {e}")

        return
    

    
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
        
        self.remove_outdated_services(new_file_name)

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
    


    def add_labels(self, file_name):#adds labels to report file
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
        comments = "Comments: "
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
            with open(file_name, 'r') as file:
                for line_number, line in enumerate(file, start=1):  # start=1 makes line_number start from 1

                    # starting at line 8 and every 8 lines after that
                    if line_number >= 8 and (line_number - 8) % 8 == 0:
                        temp_date_and_time_service_was_recorded = date_and_time_service_was_recorded + super().get_line_of_file(file_name, line_number)
                        super().overwrite_line_in_file(file_name, line_number, temp_date_and_time_service_was_recorded)
                        #date_and_time_service_was_recorded = "Date and time service recorded: "#reset variable
                    
                    #starting at line 9 and every 8 lines after that
                    if line_number >= 9 and (line_number - 9) % 8 == 0:
                        temp_date_service_was_provided = date_service_was_provided + super().get_line_of_file(file_name, line_number)
                        super().overwrite_line_in_file(file_name, line_number, temp_date_service_was_provided)
                        #date_service_was_provided = "Date service was provided: "#reset variable

                    #starting at line 10 and every 8 lines after that
                    if line_number >= 10 and (line_number - 10) % 8 == 0:
                        temp_provider_num = provider_num + super().get_line_of_file(file_name, line_number)
                        super().overwrite_line_in_file(file_name, line_number, temp_provider_num)
                        #provider_num = "Provider number: "#reset variable

                    #starting at line 11 and every 8 lines after that
                    if line_number >= 11 and (line_number - 11) % 8 == 0:
                        temp_member_num = member_num + super().get_line_of_file(file_name, line_number)
                        super().overwrite_line_in_file(file_name, line_number, temp_member_num)
                        #member_num = "Member number: "#reset variable

                    #starting at line 12 and every 8 lines after that
                    if line_number >= 12 and (line_number - 12) % 8 == 0:
                        temp_service_code = service_code + super().get_line_of_file(file_name, line_number)
                        super().overwrite_line_in_file(file_name, line_number, temp_service_code)
                        #service_code = "Service code: " #reset variable

                    #starting at line 13 and every 8 lines after that
                    if line_number >= 13 and (line_number - 13) % 8 == 0:
                        temp_fee = fee + super().get_line_of_file(file_name, line_number)
                        super().overwrite_line_in_file(file_name, line_number, temp_fee)
                        #fee = "fee: " #reset variable

                    #starting at line 14 and every 8 lines after that
                    if line_number >= 14 and (line_number - 14) % 8 == 0:
                        temp_comments = comments + super().get_line_of_file(file_name, line_number)
                        super().overwrite_line_in_file(file_name, line_number, temp_comments)
                        #comments = "Comments: "#reset variable
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



    def get_provider(self): #get a provider the user wants to generate a provider service report for, and validate user input
        return



    def chronological_sort(self): #sort services in a file by chronological order by day the service was provided
        return



    #generates a weekly etf report from the last week
    def generate_EFT_report(self): #high level menu option
        doctor_name = ""
        doctor_id_num = ""
        fees_owed = False

        if self.doctor_files is None: 
            print("There are no doctor profiles the the data base, there is no data to create an ETF report.")
            return

        current_date = datetime.now().strftime("%m_%d_%Y") #get current date and time in MM_DD_YYYY format

        #create file name
        file_name = f"ETF_REPORT_{current_date}.txt"

        #create and open etf report in write mode
        with open(file_name, 'w') as etf_report:
            for doctor_file in self.doctor_files: #for each doctor file
                doctors_fees = self.calc_weekly_fees(doctor_file) #get the doctors weekly fees

                #if this doctor should be added to etf report
                if doctors_fees > 0:
                    fees_owed = True

                    #get name and id num
                    doctor_name = super().get_line_of_file(doctor_file, 0)
                    doctor_id_num = super().get_line_of_file(doctor_file, 1)

                    #write the info for each doctor that has fees into the etf report
                    etf_report.write(f"{doctor_name}\n")
                    etf_report.write(f"{doctor_id_num}\n")
                    etf_report.write(f"{doctors_fees}\n")
                    etf_report.write(" \n")

            if not fees_owed:
                etf_report.write("No doctors provided any billable services in the last week.\n")

        print("\nETF Report has been created: \n")
        if not super().display_file_contents(file_name): #prints generated etf report file
            print("Error: ETF report file not found.\n")



    #returns the total fees from the last week earned by the doctor whose file name is passed in, also sets name and id_num variables
    def calc_weekly_fees(self, file_name):
        total_fees = 0.0
        service_date = None 
        one_week_ago = datetime.now() - timedelta(days=7) #calculate the date one week ago

        try:
            with open(file_name, 'r') as file:
                lines = file.readlines() #store the lines in the file in variable

                if len(lines) <= 7: return 0.0 #if there arn't more than 7 lines in the file then there are not services so return $0

                #start processing from line 9
                index = 8 #line 8 is the 8th index (0-based)

                while index < len(lines): #while there are still services to check 
                    #get the date
                    try:
                        service_date = datetime.strptime(lines[index].strip(), "%m-%d-%Y")
                    except ValueError: #handle errors from try block
                        print(f"{file_name}: Invalid date format on line {index + 1} found while generating ETF report. Skipping that service block.")
                        index += 8
                        continue #skip to next if improper date format

                    if service_date >= one_week_ago: #if the service is less than a week old
                        try: 
                            #get the fee from that service
                            fee = float(lines[index + 4].strip())
                            total_fees += fee #add that services fee to the total fees
                        except ValueError: #handle errors from try block
                            print(f"{file_name}: Invalid fee format on line {index + 5}. Skipping block.")
                        except IndexError:
                            print(f"{file_name}: Fee line (line {index + 5}) out of bounds. Skipping block.")

                    index += 8 #move to the next service block

        except FileNotFoundError: #handle errors for accessing file
            print(f"File {file_name} not found wile trying to generate ETF report.")
        except Exception as e:
            print(f"An error occurred while processing {file_name}: {e}")

        return total_fees


    
    #returns a list of the doctor profile file names, or None if there are none
    def get_doctor_files(self):
        pattern = "*_doctor_*_profile.txt" #pattern used to identify any doctor profile files in directory

        doctor_files = glob.glob(pattern)

        if not doctor_files: return None

        return doctor_files
