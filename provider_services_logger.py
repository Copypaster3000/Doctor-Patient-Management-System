# provider_services_logger.py
# Doctor Patient Management System
# This file holds the provider_services_logger class. This class handles logging a service provided by a doctor to a member.
# This functionality is available in Provider Mode.

# TODO: define class or struct to contain patient_record data?
import datetime

from parent import parent
from services_manager import services_manager


class provider_services_logger(parent):
    def __init__(self) -> None:
        """Initialize a provider_service_logger.

        Uses a services_manager() to manage services and a parent class for common functionality.
        """  # noqa: E501
        self.services_manager = services_manager()

    def get_date(self) -> datetime: # TODO should we be logging time at all? If not, maybe we could get rid of tzlocal package.
        """Get user input for a date and confirm before returning."""
        choice = "N"
        form = "%m/%d/%y"
        # local_tz = tzlocal.get_localzone()

        while choice.capitalize() != "Y":
            date_input = input(
                "Enter the time and date of the service (MM/DD/YY format): "
            )
            try:
                parse = datetime.datetime.strptime(date_input, form)
            except Exception as e:
                print(f"Invalid date or time format: {e}")
                continue  # Jump to the next iteration
            print(f"Entered: {parse.strftime(form)}")
            choice = input("(Y) to confirm, any other input to re-input.")
        return parse

    def log_member_services(self) -> None:  # noqa: D102
        print("Enter Provider number:")
        provider_id = super().get_9_digits()
        while not super().person_exists( 
            provider_id,
        ):
            print("Invalid. Provider does not exist.")
            provider_id = super().get_9_digits()
        print("Provider validated.\n")


        print("Enter Member number:") # TODO add dheck for valid member status (if not valid, display "Member suspended.")  # noqa: E501
        member_id = super().get_9_digits()
        while not super().person_exists(member_id):
            print("Invalid. Member does not exist")
            member_id = super().get_9_digits()

        current_datetime = datetime.datetime.now()
        print("DEBUG: current_datetime: ", str(current_datetime))

        service_date = self.get_date()

        service_code = self.services_manager.get_6_digits()
        while not self.services_manager.service_code_exists(service_code):
            print("Service code does not exist. Please enter a valid service code.")
            service_code = self.services_manager.get_6_digits()
        (service_name, service_fee) =self.services_manager.get_service_info_from_code(service_code)
        print(f"Service: {service_name}, Fee: {service_fee}") #TODO allow user to reject/confirm code here?  TODO or remove this print.
        # TODO also log service fee.
        comments = input(
            "(Optional) Enter any comments about the provided service, or leave blank: "
        )
        # save service record with data
        # add to servie record
        service_record = {
            "timestamp": current_datetime,
            "service_date": service_date,
            "provider_id": provider_id,
            "member_id": member_id,
            "service_code": service_code,
            "service_fee": service_fee,
            "comments": comments,  # TODO Example patient profile seems to imply a cost of service is also logged? or some other sixth field?
        }
        self.record_service_to_profiles(service_record)
        # self.add_service_to_provider(provider_id, service_record)
        # self.add_service_to_member(member_id, service_record)

    def record_service_to_profiles(self, service_record: dict):  #TODO fix issue with patient number verification.
        """
        Adds the service represented by `service_record` to the patient & provider associated.
        """
        if not super().person_exists(
            service_record['provider_id']
        ) or not super().person_exists(service_record["member_id"]):
            raise NameError
        provider_file = super().file_exists(
            service_record["provider_id"], "doctor", "profile"
        )
        patient_file = super().file_exists(
            service_record["member_id"], "patient", "profile"
        )
        if provider_file is None:
            print(
                f"There is no provider profile corresponding to provider ID: {service_record["provider_id"]}"
            )
            return
        elif patient_file is None:
            print(
                f"There is no patient profile corresponding to patient ID:{service_record["member_id"]}"
            )
            return
        else:  # Both ID's have matching profiles.
            provider_name = super().get_line_of_file(provider_file, 0)
            patient_name = super().get_line_of_file(patient_file, 0)
            print(f"Found profile for provider {provider_name}. Logging service...")
            self.write_service_to_profile(service_record, provider_file)

            print(f"Found profile for member {patient_name}. Logging service...")
            self.write_service_to_profile(service_record, patient_file)
            print("Service logged for provider and member.")
            return

    def write_service_to_profile(self, service_record: dict, file_name: str):
        """Records a new service to the profile corresponding to profile_id. Preserves linebreak formatting."""

        record = f"""
{service_record["timestamp"]}\n
{service_record["service_date"]}\n
{service_record["provider_id"]}\n
{service_record["member_id"]}\n
{service_record["service_code"]}\n
{service_record["comments"]}\n
"""
        with open(file_name, "rw") as f:
            contents = f.readlines()
            contents.insert(8, record)  # Add record at eigth line.
            res = "".join(contents)
            f.write(res)
