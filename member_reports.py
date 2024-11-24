#member_reports.py
#Doctor Patient Management System
#This file holds the member_reports class. The member_reports class is responsible for generating a member's weekly
#service report which is available in Manager Mode.
#Jordan worked on this :D
from parent import parent


class member_reports(parent):
    """
    This function generates a weekly service report for a member, and is
        accessed through Manager Mode.
    The report includes:
        - Name      - ID        - Address
        - Date of Service       - The Provider
        - Service Name          - Sevice Code?
    Args:    member_id (string): The ID of the corresponding member
    Returns: The generated report as a formatted string
    """
    def generate_member_report(self):
        #Step 1: Prompt for member ID
        member_id = self.get_9_digits()  # Ensures the user enters a valid 9-digit member ID
        
        #Step 2: Validate member profile
        profile_file = self.file_exists(member_id, "member", "profile")
        if not profile_file:
            print(f"Error: Member ID {member_id} not found.")
            return None
        
        #Step 3: Read member profile details
        with open(profile_file, 'r') as file:
            lines = file.readlines()
            member_name = lines[0].strip()
            member_id = lines[1].strip()
            address = lines[2:6]
            status = lines[6].strip()
            status_comments = lines[7].strip() if len(lines[7].strip()) > 0 else "No comments"
        
        #Step 4: Retrieve and process service records
        services = []
        for i in range(8, len(lines), 7):  #Service entries start after the 8th line, each service block spans 7 lines
            if i + 6 >= len(lines):  #Ensure a complete service block exists
                break
            service_details = {
                "current_datetime": lines[i].strip(),
                "service_date": lines[i + 1].strip(),
                "provider_id": lines[i + 2].strip(),
                "member_id": lines[i + 3].strip(),
                "service_code": lines[i + 4].strip(),
                "fee": lines[i + 5].strip(),
                "comments": lines[i + 6].strip()
            }
            services.append(service_details)

        #Step 5: Construct the report
        report = []
        report.append(f"Weekly Service Report for {member_name}")
        report.append(f"Member ID: {member_id}")
        report.append("Address:")
        report.extend([addr.strip() for addr in address])
        report.append(f"Status: {status}")
        report.append(f"Status Comments: {status_comments}")
        report.append("\nServices Received:")

        if services:
            for service in services:
                report.append(f"- Service Date: {service['service_date']}")
                report.append(f"  Provider ID: {service['provider_id']}")
                report.append(f"  Service Code: {service['service_code']}")
                report.append(f"  Fee: ${service['fee']}")
                if service['comments']:
                    report.append(f"  Comments: {service['comments']}")
                report.append("")  #Blank line for readability
        else:
            report.append("No services received this week.")

        #Step 6: Save report to a file
        report_file = f"{member_id}_member_weekly_report.txt"
        with open(report_file, 'w') as file:
            file.write('\n'.join(report))
        
        print(f"Report successfully generated and saved to {report_file}.")

        #Step 7: Ask user if they want to print the report 
        self.print_member_report(member_id)

        return '\n'.join(report)  #Return the report as a string for testing purposes
    
    #Prompts the user to print the generated report for the specified member
    def print_member_report(self, member_id):
        report_file = f"{member_id}_member_weekly_report.txt"
        print(f"Would you like to print the member report now?\n1) Yes\n2) No")
        choice = self.get_menu_choice(2)  #1 for yes, 2 for no

        if choice == 1:
            try:
                with open(report_file, 'r') as file:
                    print("\n--- Member Report ---\n")
                    print(file.read())
                    print("\n--- End of Report ---\n")
            except FileNotFoundError:
                print(f"Error: Report file '{report_file}' not found.")
        else:
            print("Report was not printed.")