# test_services_manager.py
# CS314
# Doctor Patient Management System 
# This file contains unit tests. Every function is tested for normal operation and abnormal/invalid inputs
# pythons unittest.mock library is used to help with testing user input functionality

import unittest 
from unittest import mock # used to replace parts of the services manager system during testing (user input)
import shutil # used for file copying
import os # used for interacting with the operating system
from services_manager import services_manager


class test_services_manager(unittest.TestCase):

    # set up for testing
    def setUp(self):
        # original services directory file, dont want to muck with it
        self.original_file = "services.txt"

        # temp file to copy service directory over to, will be testing on this file instead of original to prevent corruption
        self.test_file = "test_services.txt"

        # create a copy of the entire service directory file
        shutil.copy(self.original_file, self.test_file)

        # instance of service manager to use its functions for testing
        self.sm = services_manager()
        # override file being used in service manager for testing
        self.sm.service_directory = self.test_file 


    # remove test file once testing is complete
    def tearDown(self):
        # remove from current directory if the test_services.txt exists 
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    # test 1: adding a valid service
    def test_add_valid_service(self):
       # use unittest patch function to replace input that function will expect from user 
        with unittest.mock.patch('builtins.input', side_effect=[  
            # sequence of values to be returned by the input() calls 
            "Mental Health Counseling",  # service name
            "1",                         # confirmation
            "654006",                    # service code
            "1",                         # confirmation
            "100.00",                    # service fee
            "1"                          # confirmation 
        ]):
            # add a service to the service directory
            self.sm.add_service()

        # assert: check if the service was successfully added to the temp service directory .txt file
        with open(self.test_file, 'r') as file:
            contents = file.read()
            # service name, code and fee should all match
            self.assertIn("Mental Health Counseling,654006,100.00", contents)
            
    # test 2: adding an invalid service as its name already exists 
    def test_add_invalid_service_name(self):
         # use unittest patch function to replace input that function will expect from user 
        with unittest.mock.patch('builtins.input', side_effect=[
            "Aerobics Exercise Session",  # invalid service name
            "1",                          # confirmation
            "ChoAn Group Session",        # valid service name
            "1",                          # confirmation
            "654007",                     # service code
            "1",                          # confirmation
            "40.00",                      # service fee
            "1"                           # confirmation 
        ]):
            # add a service to the service directory
            self.sm.add_service()

        # assert: check if the service was succesfully added
        with open(self.test_file, 'r') as file:
            contents = file.read()
            self.assertIn("ChoAn Group Session,654007,40.00", contents)
            
    # test 3: adding an invalid service as its code already exists 
    def test_add_invalid_service_code(self):
        # use unittest patch function to replace input that function will expect from user 
        with unittest.mock.patch('builtins.input', side_effect=[
            "Personalized Fitness Training",   # service name
            "1",                               # confirmation 
            "654001",                          # invalid service code
            "1",                               # confirmation
            "654008",                          # valid service code
            "1",                               # confirmation
            "50.00",                           # service fee
            "1"                                # confirmation 
        ]):
            self.sm.add_service()

        # assert: check if the service was successfully added
        with open(self.test_file, 'r') as file:
            contents = file.read()
            self.assertIn("Personalized Fitness Training,654008,50.00", contents)


    # test 4: removing a valid service from the service directory
    def test_remove_service(self):
        # use unittest patch function to replace input that function will expect from user 
        with unittest.mock.patch('builtins.input', side_effect=[
            "1",        # confirmation to view menu
            "654002",  # service code to remove
            "1"        # confirmation to remove service
        ]):
            self.sm.remove_service()

        # assert: check if the service was successfully removed
        with open(self.test_file, 'r') as file:
            contents = file.read()
            self.assertNotIn("Aerobics Exercise Session,654002,40.00", contents)
            
    # test 5: removing an invalid service (more than 6 digits) from the service directory
    def test_remove_invalid_service(self):
        # use unittest patch function to replace input that function will expect from user 
        with unittest.mock.patch('builtins.input', side_effect=[
            "1",        # confirmation to view menu
            "6540000",  # service code to remove
            "1",
            "654005",  # service code to remove
            "1"        # confirmation to remove service
        ]):
            self.sm.remove_service()

        # assert: check if the service was successfully removed
        with open(self.test_file, 'r') as file:
            contents = file.read()
            self.assertNotIn("Stress Management Workshop,654005,75.00", contents)
            
    # test 6: removing a nonexistent service from the service directory
    def test_remove_nonexistent_service(self):
        # use unittest patch function to replace input that function will expect from user 
        with unittest.mock.patch('builtins.input', side_effect=[
            "1",       # confirmation to view menu
            "654089",  # service code to remove
            "1",
            "654004",  # service code to remove
            "1"        # confirmation to remove service
        ]):
            self.sm.remove_service()

        # assert: check if the service was successfully removed
        with open(self.test_file, 'r') as file:
            contents = file.read()
            self.assertNotIn("Nutritional Guidance,654004,60.00", contents)
            
    # TODO: unit test for view_service_directory() function
            
    # test 7: checking if a given service code is 6 digits 
    def test_valid_is_6_digits(self):
        # assert it is a valid 6 digit code
        self.assertTrue(self.sm.is_6_digits("654321"))
        
    # test 8: checking if a given invalid service code is 6 digits 
    def test_invalid_is_6_digits(self):
        # assert it is a valid 6 digit code
        self.assertFalse(self.sm.is_6_digits("6543219"))
        
    # test 9: getting the 6 digit service code from the user & validating it
    def test_valid_get_6_digits(self):
         # use unittest patch function to replace input that function will expect from user 
        with unittest.mock.patch('builtins.input', side_effect=[
            "654089",  # valid service code
        ]):
            self.sm.get_6_digits()
            
    # test 10: getting a invalid 6 digit service code from the user 
    def test_invalid_get_6_digits(self):
         # use unittest patch function to replace input that function will expect from user 
        with unittest.mock.patch('builtins.input', side_effect=[
            "6540891",  # invalid service code
            "654089",  # valid service code
        ]):
            self.sm.get_6_digits()

    # test 11: getting a valid service name from the user - should not already exist in the service directory
    def test_get_valid_service_name(self):
         # use unittest patch function to replace input that function will expect from user 
        with unittest.mock.patch('builtins.input', side_effect=[
            "Sports Performance Training",  # valid service name
            "1"
        ]):
            service_name = self.sm.get_valid_service_name()
        
        # Assert: Ensure the returned service name is valid
        self.assertEqual(service_name, "Sports Performance Training")
        
    # test 12: getting a invalid service name from the user 
    def test_invalid_get_valid_service_name(self):
         # use unittest patch function to replace input that function will expect from user 
        with unittest.mock.patch('builtins.input', side_effect=[
            "Nutritional Guidance",  # invalid service name
            "1",
            "Healthy Baking Class",         # valid service name
            "1"
        ]):
            service_name = self.sm.get_valid_service_name()
        
        # Assert: Ensure the returned service name is valid
        self.assertEqual(service_name, "Healthy Baking Class")
        
    # test 13: allowing user to confirm input - 1 (Yes)
    def test_1_confirm_input(self):
        with unittest.mock.patch('builtins.input', side_effect=[
            "1"  # 1 for yes continue, user is happy with their input
            ]):
            result = self.sm.confirm_input("Test")
            
        self.assertTrue(result)
        
    # test 14: allowing user to confirm input - 2 (No)
    def test_2_confirm_input(self):
        with unittest.mock.patch('builtins.input', side_effect=[
            "2"  # 2 for not happy to continue, function will return false
            ]):
            result = self.sm.confirm_input("Test")
            
        self.assertFalse(result)
        
    # test 15: check if a service name exist - it does
    def test_true_service_name_exists(self):
        result = self.sm.service_name_exists("Nutritional Guidance")
        self.assertTrue(result)
    
    # test 16: check if a service name exist - it does not
    def test_false_service_name_exists(self):
        result = self.sm.service_name_exists("Nonexistent Service Name")
        self.assertFalse(result)
        
    # test 17: getting a valid service code - its valid
    def test_valid_get_valid_service_code(self):
        # use unittest patch function to replace input that function will expect from user 
        with unittest.mock.patch('builtins.input', side_effect=[
            "123456",  # valid service name
            "1",       # confirmation
        ]):
            service_code = self.sm.get_valid_service_code()
        
        # Assert: Ensure the returned service name is valid
        self.assertEqual(service_code, "123456")
        
    # test 18: getting a valid service code - its not 6 digits
    def test_invalid_get_valid_service_code(self):
        # use unittest patch function to replace input that function will expect from user 
        with unittest.mock.patch('builtins.input', side_effect=[
            "1234562",  # invalid service name
            "123456",   # valid service code 
            "1"         # confirmation
        ]):
            service_code = self.sm.get_valid_service_code()
        
        # Assert: Ensure the returned service name is valid
        self.assertEqual(service_code, "123456")
    
    # test 19: getting a valid service code - its already in use / unavailable
    def test_unavailable_get_valid_service_code(self):
        # use unittest patch function to replace input that function will expect from user 
        with unittest.mock.patch('builtins.input', side_effect=[
            "654001",   # invalid service name - already in system
            "1",        # confirmation
            "123456",   # valid service code 
            "1"         # confirmation
        ]):
            service_code = self.sm.get_valid_service_code()
        
        # Assert: Ensure the returned service name is valid
        self.assertEqual(service_code, "123456")
        
    # test 20: checks if a service code already exists - its does not
    def test_available_service_code_exists(self):
        result = self.sm.service_code_exists("123456")
        self.assertFalse(result)
        
    # test 21: checks if a service code already exists - it does
    def test_available_service_code_exists(self):
        result = self.sm.service_code_exists("654001")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
