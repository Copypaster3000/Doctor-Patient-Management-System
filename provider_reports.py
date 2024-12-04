#provider_reports.py
#Doctor Patient Management System
#This file contains the provider_reports class. This class is responsible for generating reports specific to providers.
#Including generating a doctor's weekly service report, generating a provider summary report for all doctors, and generating
#a weekly ETF report. All of which will be available through Manager Mode.

import glob

from parent import parent
from datetime import datetime, timedelta


class provider_reports(parent):

    def __init__(self):
        self.doctor_files = self.get_doctor_files()

    def generate_provider_summary_report(): #high level menu option
        #get date range of the summary report from the user
        #find all doctor profiles will services logged in that range (probably a recursisve algorithim)
        #as services in that range are found, copy service and doctor information to local variables
        return



    def generate_provider_service_report(self): #high level menu option
        return


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
