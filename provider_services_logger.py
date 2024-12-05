chef_boyardrizzy
chef_boyardrizzy
Invisible

chef_boyardrizzy — 11/25/24, 4:19 PM
We have the test doc due December 6th. I think that’s what all the code is due too. We will also have to have our presentation finished around that time.
chef_boyardrizzy — 11/25/24, 4:20 PM
Cool, will review and merge when I get the chance or someone else can
@everyone I think it’s be ideal to get the test plan done ahead of time, he just decided to push the due date back but I think it’d be nice to have it done before the presentation instructions come out so we can just focus on that when it does
JRo — 11/25/24, 4:26 PM
I concur with that plan.
I'll get a Test Plan document template started and share all of you guys in it.
wirehead. — 11/25/24, 4:41 PM
Might I propose December first as a self imposed test plan deadline?
Nat — 11/25/24, 4:43 PM
Sounds good to me
chef_boyardrizzy — 11/25/24, 5:10 PM
Merged it
chef_boyardrizzy — 11/27/24, 5:07 PM
@everyone when you have completed an entire menu function, go ahead and add it to the menus_n_modes class so it can be selected through the menus and let the group know and we will test it out. 

So far the menu options that have been implemented and added to the menu to use are:
from manager mode:
generate_member_report
add_new_doctor_profile
add_new_member_profile
edit_doctor_profile
edit_member_profile
remove_doctor_profile
remove_member_profile
edit_member_status
add_service
remove_service

from provider mode:
view_service_directory
chef_boyardrizzy — 11/27/24, 5:26 PM
@everyone Also fyi, I am willing to trade my section of the test plan doc for anyone's entire coding section, but if you want to do that, let me know asap.
chef_boyardrizzy — 11/27/24, 5:35 PM
@everyone I realized the doctor profiles we had on github had the wrong naming convention. I am changing them. Make sure you pull the updated correct files if you are using them. Refer to the read me for the correct naming convention of files, it's up to date and correct
@everyone Also make absolutely sure you don't push the old version of the files back onto the repo, it's a pain in the butt to go through and delete each one
chef_boyardrizzy — 11/27/24, 6:02 PM
@Catherine This is outlined in the requirements doc fyi
Image
We are coding under the assumption that's how services will be logged
chef_boyardrizzy — 12/2/24, 4:33 PM
I added 20 member profile text file to the repo
chef_boyardrizzy — 12/2/24, 5:36 PM
@wirehead. I am done with my coding part and my test doc part. Is there anything you could use some help with?
chef_boyardrizzy — 12/2/24, 7:06 PM
@everyone be aware, the member profiles on github are missing the state in the profiles, so they will be off by one line. I am fixing it now
@everyone Make sure you pull the corrected member files, will cause issues if you use the old ones and expect them to be the correct format or base your code off the incorrect format of them.
Catherine — 12/2/24, 7:59 PM
Would it be alright if I added a method to services_manager for getting the name of a service (as a string) corresponding to a service code passed as argument?
I can keep this in my own class, if anyone wants, seems more sensible to tie it to services_manager() though
chef_boyardrizzy — 12/2/24, 8:03 PM
You could if you want. I think it’d be easier to add it in your class though so you don’t have to creat the other class object in your function. I think it’d fit better in your class anyways too cause it’s not needed for completing the functionality the services class is responsible for in terms of the menu options
Catherine — 12/2/24, 8:32 PM
I'm already using a service_manager() instance in the provider_services_logger class, for validating service code inputs etc., so I don't think it would be too out of the question to add this new method to service_manager()?
chef_boyardrizzy — 12/2/24, 8:36 PM
Ah okay, yeah makes sense, if say go for it
wirehead. — 12/2/24, 11:33 PM
I emailed chirs to let him know I am sick and it is impacting my work. I would be down to collaborate on a call. or you could take over one of my 3 functions? like the eft report?
chef_boyardrizzy — 12/2/24, 11:36 PM
Thanks for getting ahead of that. Okay, yeah I’ll take over the etf report. If you have any working code for the class done yet could you push it the repo so I can see it for reference
wirehead. — 12/2/24, 11:49 PM
nothing to push atm. Ill set up template reports and push tonight so you have something to work with in the morning.
chef_boyardrizzy — 12/2/24, 11:51 PM
That’d be great thanks
JRo — Yesterday at 5:55 PM
My coding section has been completed. I'm going to wait to push it when we meet on Wednesday. I still need to complete my writing section for the Testplan Document.
chef_boyardrizzy — Yesterday at 6:12 PM
Nice, well done
chef_boyardrizzy — Yesterday at 7:14 PM
Success!!
@wirehead. Finished the ETF report menu option and merged it
@wirehead. I added a data member to the class that upon initialization of the class object is set to a list of all the doctor profile file names in the directory. It may be useful to you 
wirehead. — Yesterday at 7:21 PM
I've been working on provider service report today, haven't made a pull request yet because its not done done. some of your functions look helpful. sweet.
chef_boyardrizzy — Yesterday at 7:23 PM
Sounds good. Yeah you can pull the latest updated code to your local repo at anytime without approval, will be easier to merge when the time comes if you pull locally now, then there won’t be any conflicts when you go to merge
wirehead. — Yesterday at 7:26 PM
I'm actually having an issue with git rn, are you free to hop on a quick call to walk me through this?
wirehead. — Yesterday at 7:39 PM
nvm got it
chef_boyardrizzy — Yesterday at 7:44 PM
Okay cool, just saw this
wirehead. — Yesterday at 8:28 PM
@everyone all of our provider profiles have member number and provider numbers fliped in storage. plus the member numbers are not accurate to the member profile files
chef_boyardrizzy — Yesterday at 8:33 PM
You mean like for a logged service they’re backwards?
chef_boyardrizzy — Yesterday at 8:34 PM
What do you mean the member numbers aren’t accurate to the member number profiles?
chef_boyardrizzy — Yesterday at 8:37 PM
OKay, I see what you mean by the doctor and member ID numbers are switched in each service logged. Would it be easy to change our standard to that? Or should I go through and change them all?
chef_boyardrizzy — Yesterday at 8:40 PM
Oh for the second thing are you saying that the member numbers in the doctor profiles in their services logged aren't of actual members and that makes it not work for a type of report?
wirehead. — Yesterday at 8:48 PM
the provider is in the file name is the number thats currently in the "member number" feild. and a random number starting with 9 is in its place, I assume a generated member number.
chef_boyardrizzy — Yesterday at 8:48 PM
Gotcha, I see
wirehead. — Yesterday at 8:48 PM
the member profile files have different id numbers then the ones listed in the doctor profiles 
wirehead. — Yesterday at 8:49 PM
do u wanna call?
i could use help with the git stuff again rip
chef_boyardrizzy — Yesterday at 8:50 PM
yeah lets do it
chef_boyardrizzy — Yesterday at 9:28 PM
@everyone Be aware that the current profile files have some issues with them. The doctor and member ID number's are switched in the services logged portions of the profiles. Also the member and doctor IDs in services logged are from made up members and doctors. I am going to redo all the files so that they are in the right order and all the service codes member IDs and doctor IDs are of actual ones we have in our data base. Will finish sometime tm, just be aware of that for the time being.
This still is the correct format and order, so base your code on services being logged in this format
Image
chef_boyardrizzy — Today at 5:04 PM
@wirehead. jordan and I decided that the dates for which we base whether a service should be included in a report or not should be the "current date and time" the first line in each service logged, this way all of them end up in weekly service reports. Because if we go by date that service was provided a service could technically be logged a week after it was provided and then not be included inany report
Catherine — Today at 5:39 PM
My finished(?) implementation of provider_services_logger
# provider_services_logger.py
# Doctor Patient Management System
# This file holds the provider_services_logger class. This class handles logging a service provided by a doctor to a member.
# This functionality is available in Provider Mode.

import datetime
Expand
provider_services_logger.py
7 KB
wirehead. — Today at 5:40 PM
hmm, I see. that makes sense to me
﻿
# provider_services_logger.py
# Doctor Patient Management System
# This file holds the provider_services_logger class. This class handles logging a service provided by a doctor to a member.
# This functionality is available in Provider Mode.

import datetime

from parent import parent
from services_manager import services_manager


class provider_services_logger(parent):
    def __init__(self) -> None:
        """Initialize a provider_service_logger.

        Uses a services_manager() to manage services and a parent class for common functionality.
        """  # noqa: E501
        self.services_manager = services_manager()

    def check_member_status(self, member_id):
        if not super().person_exists(member_id):
            raise ValueError("Cannot check status of non-existent member.")

        file_name = super().file_exists(member_id, "member", "profile")
        if file_name is None:
            print(f"There is no member profile with that ID number.")
        else:
            status = super().get_line_of_file(file_name, 5)
            print(f"Member status: {status}")
            return status

    def get_date(
        self,
    ) -> datetime:
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

        print("Enter Member number:")
        member_id = super().get_9_digits()
        while not super().person_exists(member_id):
            print("Invalid. Member does not exist")
            member_id = super().get_9_digits()
        member_status = self.check_member_status(member_id)
        if member_status != "valid":
            print("Member suspended.")
            return
        print("Patient validated.")

        current_datetime = datetime.datetime.now()
        print("DEBUG: current_datetime: ", str(current_datetime))

        service_date = self.get_date()

        service_code = self.services_manager.get_6_digits()
        while not self.services_manager.service_code_exists(service_code):
            print("Service code does not exist. Please enter a valid service code.")
            service_code = self.services_manager.get_6_digits()
        (service_name, service_fee) = self.services_manager.get_service_info_from_code(
            service_code
        )
        print(
            f"Service: {service_name}, Fee: {service_fee}"
        )  # TODO allow user to reject/confirm code here?  TODO or remove this print.
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

    def record_service_to_profiles(
        self, service_record: dict
    ):  # TODO fix issue with patient number verification.
        """
        Adds the service represented by `service_record` to the patient & provider associated.
        """
        if not super().person_exists(
            service_record["provider_id"]
        ) or not super().person_exists(service_record["member_id"]):
            raise NameError

        provider_file = super().file_exists(
            service_record["provider_id"], "doctor", "profile"
        )
        patient_file = super().file_exists(
            service_record["member_id"], "member", "profile"
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
{service_record["timestamp"]}
{service_record["service_date"]}
{service_record["provider_id"]}
{service_record["member_id"]}
{service_record["service_code"]}
{service_record["service_fee"]}
{service_record["comments"]}
"""
        contents = []
        with open(file_name, "r") as f:
            contents = f.readlines()

        with open(file_name, "w") as f:
            contents.insert(8, record)  # Add record at eigth line.
            res = "".join(contents)
            f.write(res)
provider_services_logger.py
7 KB

