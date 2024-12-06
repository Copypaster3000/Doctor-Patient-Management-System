# test_provder_services_logger.py
# CS 314
# Doctor Patient Management System 
# This file contains unit tests. Every function is tested for expected operations.
# pythons unittest.mock library is used to help with testing user input functionality
# `python3 -m unittest test_provider_services_logger.py` to run

import datetime
import os  # used for interacting with the operating system
import shutil  # used for file copying
import unittest
from unittest import (
    mock,  # used to replace parts of the services manager system during testing (user input)
)

from provider_services_logger import provider_services_logger


class test_provider_services_logger(unittest.TestCase):
    def setUp(self):
        self.example_original_patient_file = "985165478_member_Grace_Bohlsen_profile.txt"
        self.example_original_doctor_file = "875489247_doctor_Doctor_Drake_profile.txt"
        self.example_patient_ID = "985165478" # ID of Grace Bohlsen, a valid member
        self.example_provider_ID = "875489247"
        self.example_service_code = "654009"

        shutil.copy(self.example_original_patient_file, "test_patient.txt")
        shutil.copy(self.example_original_doctor_file, "test_doctor.txt")
        self.psl = provider_services_logger()

    def tearDown(self):
        if os.path.exists("test_patient.txt"):
            shutil.copy('test_patient.txt', self.example_original_patient_file)
            os.remove("test_patient.txt")
        if os.path.exists("test_doctor.txt"):
            shutil.copy('test_doctor.txt', self.example_original_doctor_file)
            os.remove("test_doctor.txt")

    def test_check_member_status(self):
        result = self.psl.check_member_status(self.example_patient_ID)
        assert result == "valid", f"Expected 'valid', but got {result}"


    def test_check_get_date(self):
        with unittest.mock.patch('builtins.input', side_effect=[
            "12/05/2024",
            "Y"
        ]):
            result = self.psl.get_date().strftime("%m/%d/%Y")
            assert result == "12/05/2024", f"Expected '12/05/2024' but got {result}"
    
    def test_check_log_member_services(self):
        with unittest.mock.patch('builtins.input',side_effect=[
            self.example_provider_ID,
            self.example_patient_ID,
            "12/05/2024",
            "Y",
            self.example_service_code,
            "Example comments",
        ]):
            self.psl.log_member_services()
        example_service_record=f"""{self.example_provider_ID}
{self.example_patient_ID}
{self.example_service_code}"""
        with open(self.example_original_patient_file, 'r') as patient:
            contents = patient.read()
            self.assertIn(example_service_record, contents)
        with open(self.example_original_doctor_file, 'r') as doctor:
            contents = doctor.read()
            self.assertIn(example_service_record, contents)
        
    def test_check_record_service_to_profiles(self):
        timestamp = datetime.datetime.now()
        example_record = {
            "timestamp": timestamp,
            "service_date": timestamp,
            "provider_id": self.example_provider_ID,
            "member_id": self.example_patient_ID,
            "service_code": self.example_service_code,
            "service_fee": 45.00,
            "comments": "Example comment",
        }
        formatted_record= f"""{example_record["timestamp"]}
{example_record["service_date"]}
{example_record["provider_id"]}
{example_record["member_id"]}
{example_record["service_code"]}
{example_record["service_fee"]}
{example_record["comments"]}
"""
        self.psl.record_service_to_profiles(example_record)
        with open(self.example_original_doctor_file, 'r') as doctor:
            contents = doctor.read()
            self.assertIn(formatted_record, contents)
        with open(self.example_original_patient_file, 'r') as patient:
            contents = patient.read()
            self.assertIn(formatted_record, contents)

    def test_check_write_service_to_both_profiles(self):
        timestamp = datetime.datetime.now()
        example_record = {
            "timestamp": timestamp,
            "service_date": timestamp,
            "provider_id": self.example_provider_ID,
            "member_id": self.example_patient_ID,
            "service_code": self.example_service_code,
            "service_fee": 45.00,
            "comments": "Example comment",
        }
        formatted_record= f"""{example_record["timestamp"]}
{example_record["service_date"]}
{example_record["provider_id"]}
{example_record["member_id"]}
{example_record["service_code"]}
{example_record["service_fee"]}
{example_record["comments"]}
"""
        self.psl.write_service_to_profile(example_record, self.example_original_doctor_file)
        self.psl.write_service_to_profile(example_record, self.example_original_patient_file)

        with open(self.example_original_doctor_file, 'r') as doctor:
            contents = doctor.read()
            self.assertIn(formatted_record, contents)
        with open(self.example_original_patient_file, 'r') as patient:
            contents = patient.read()
            self.assertIn(formatted_record, contents)

if __name__ == '__main__':
    unittest.main()
