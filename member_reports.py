#member_reports.py
#Doctor Patient Management System
#This file holds the member_reports class. The member_reports class is responsible for generating a member's weekly
#service report which is available in Manager Mode.
#Jordan worked on this :D
from datetime import datetime, timedelta
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

    Things that are off:
    - Status needs to report valid or invalid on one single line                        [X]
    - Only include services that are done within the last week in the report            [X]
    - Something weird is happening with the Fee $$                                      [X]
    - Some services have comments as the last thing to report, some do not              [X]
    - Format for the member report file: 123456789_member_name_report_MM_DD_YYYY.txt: An individual member's weekly billing report      [X]
    """
    def generate_member_report(self):
        # Step 1: Prompt for member ID
        member_id = self.get_9_digits()  # Ensures the user enters a valid 9-digit member ID

        # Step 2: Validate member profile
        profile_file = self.file_exists(member_id, "member", "profile")
        if not profile_file:
            print(f"Error: Member ID {member_id} not found.")
            return None

        # Step 3: Read member profile details
        with open(profile_file, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]  # Remove leading/trailing whitespaces

        # Extract member details
        member_name = lines[0]
        member_id = lines[1]
        address = lines[2:6]
        status = lines[6].capitalize()  # Ensure "valid" or "invalid" is capitalized for consistency
        status_comments = lines[7] if lines[7] else "No comments"

        # Step 4: Retrieve and process service records (only include those from the last week)
        services = []
        service_blocks = []
        current_block = []

        # Use the current date and time dynamically
        today = datetime.now()
        one_week_ago = today - timedelta(days=7)

        # Starting from line 8, parse the service entries
        for line in lines[8:]:
            if line == '':
                if current_block:
                    service_blocks.append(current_block)
                    current_block = []
            else:
                current_block.append(line)
        # Add the last block if it's not empty
        if current_block:
            service_blocks.append(current_block)

        # Process each service block
        for block in service_blocks:
            # Skip incomplete blocks
            if len(block) < 6:
                continue

            # Extract service details
            current_datetime_str = block[0]
            service_date_str = block[1]
            provider_id = block[2]
            member_id_block = block[3]
            service_code = block[4]
            fee = block[5]
            comments = block[6] if len(block) > 6 else ''

            # Parse current datetime
            try:
                current_datetime = datetime.strptime(current_datetime_str, "%m-%d-%Y %H:%M:%S")
            except ValueError:
                try:
                    current_datetime = datetime.strptime(current_datetime_str, "%m-%d-%Y")
                except ValueError:
                    continue  # Skip entries with invalid date formats

            # Check if the current datetime is within the last week
            if one_week_ago <= current_datetime <= today:
                service_details = {
                    "current_datetime": current_datetime_str,
                    "service_date": service_date_str,
                    "provider_id": provider_id,
                    "member_id": member_id_block,
                    "service_code": service_code,
                    "fee": fee,
                    "comments": comments
                }
                services.append(service_details)

        # Step 5: Construct the report
        report = []
        report.append(f"Weekly Service Report for {member_name}")
        report.append(f"Member ID: {member_id}")
        report.append("Address:")
        report.extend(address)
        report.append(f"Status: {status}")
        report.append(f"Status Comments: {status_comments}")
        report.append("\nServices Received (Last 7 Days):")

        if services:
            for service in services:
                # Display the current datetime as the service date
                report.append(f"- Service Date: {service['current_datetime']}")
                report.append(f"  Provider ID: {service['provider_id']}")
                report.append(f"  Service Code: {service['service_code']}")
                report.append(f"  Fee: ${service['fee']}")
                if service['comments']:
                    report.append(f"  Comments: {service['comments']}")
                report.append("")  # Blank line for readability
        else:
            report.append("No services received in the last week.")

        # Step 6: Save report to a file with the new naming convention
        # Replace spaces with underscores in the member's name
        member_name_formatted = member_name.replace(' ', '_')
        # Format the current date as MM_DD_YYYY
        current_date_str = today.strftime("%m_%d_%Y")
        # Construct the report file name
        report_file = f"{member_id}_{member_name_formatted}_report_{current_date_str}.txt"

        with open(report_file, 'w') as file:
            file.write('\n'.join(report))

        print(f"Report successfully generated and saved to {report_file}.")

        # Step 7: Ask user if they want to print the report
        self.print_member_report(report_file)

        return '\n'.join(report)  # Return the report as a string for testing purposes

    def print_member_report(self, report_file):
        """
        Prompts the user to print the generated report.

        Args:
            report_file (str): The filename of the generated report.
        """
        print(f"Would you like to print the member report now?\n1) Yes\n2) No")
        choice = self.get_menu_choice(2)  # 1 for yes, 2 for no

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