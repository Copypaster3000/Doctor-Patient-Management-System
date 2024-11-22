#test_profile_manager.py
#CS 314
#Doctor Patient Management System
#This file test profile manager class
#Enter 'python3 -m unittest test_profile_manager.py' to run

import os
import unittest
from unittest import mock
from profile_manager import profile_manager


class TestProfileManager(unittest.TestCase):

    #runs before each test function
    def setUp(self):
        #create an instance of ProfileManager for testing
        self.pm = profile_manager()
        #expected file names for the profiles being tested
        self.doctor_file = "435869389_doctor_Dr._John_Doe_profile.txt"
        self.member_file = "549837813_member_Jane_Smith_profile.txt"
        #remove any existing files to ensure clean test environment
        if os.path.exists(self.doctor_file): os.remove(self.doctor_file)
        if os.path.exists(self.member_file): os.remove(self.member_file)



    #cleans up after each test function is ran
    def tearDown(self):
        #clean up the created files after each test
        if os.path.exists(self.doctor_file): os.remove(self.doctor_file)
        if os.path.exists(self.member_file): os.remove(self.member_file)



    #tests creating a new doctor profile with the user passing in valid input for each prompt
    #tests for proper file name created and correct file contents
    @mock.patch('builtins.input', side_effect=["Dr. John Doe", "1", "435869389", "1", "123 Elm Street", "1", "Springfield", "1", "IL", "1", "62704", "1"]) #acts as user input
    def test_add_new_doctor_profile(self, mock_input):
        #test adding a new doctor profile
        self.pm.add_new_doctor_profile()
        #verify the file was created
        self.assertTrue(os.path.exists(self.doctor_file), f"File {self.doctor_file} was not created.")
        #verify the contents of the file
        with open(self.doctor_file, 'r') as f:
            lines = f.readlines()
            assert lines[0].strip() == "Dr. John Doe"
            assert lines[1].strip() == "435869389"
            assert lines[2].strip() == "123 Elm Street"
            assert lines[3].strip() == "Springfield"
            assert lines[4].strip() == "IL"
            assert lines[5].strip() == "62704"



    #tests creating a new doctor profile with the user entering three invalid ID numbers, the only input that has specified requirements and then valid input when prompted to enter again
    #tests for proper file name created and correct file contents
    @mock.patch('builtins.input', side_effect=["Dr. John Doe", "1", "11111111111", "asdfkj", "1234", "435869389", "1", "123 Elm Street", "1", "Springfield", "1", "IL", "1", "62704", "1"]) #acts as user input
    def test_invalid_add_new_doctor_profile(self, mock_input):
        #test adding a new doctor profile
        self.pm.add_new_doctor_profile()
        #verify the file was created
        self.assertTrue(os.path.exists(self.doctor_file), f"File {self.doctor_file} was not created.")
        #verify the contents of the file
        with open(self.doctor_file, 'r') as f:
            lines = f.readlines()
            assert lines[0].strip() == "Dr. John Doe"
            assert lines[1].strip() == "435869389"
            assert lines[2].strip() == "123 Elm Street"
            assert lines[3].strip() == "Springfield"
            assert lines[4].strip() == "IL"
            assert lines[5].strip() == "62704"



    #tests creating a new member profile with the user passing in valid input for each prompt
    #tests for proper file name created and correct file contents
    @mock.patch('builtins.input', side_effect=["Jane Smith", "1", "549837813", "1", "456 Oak Avenue", "1", "Metropolis", "1", "NY", "1", "10001", "1"]) #acts as user input
    def test_add_new_member_profile(self, mock_input):
        #call function that is being tested
        self.pm.add_new_member_profile()
        #verify the correct member file was created
        self.assertTrue(os.path.exists(self.member_file), f"File {self.member_file} was not created.")
        #verify the contents of the file
        with open(self.member_file, 'r') as f:
            lines = f.readlines()
            assert lines[0].strip() == "Jane Smith"
            assert lines[1].strip() == "549837813"
            assert lines[2].strip() == "456 Oak Avenue"
            assert lines[3].strip() == "Metropolis" 
            assert lines[4].strip() == "NY"
            assert lines[5].strip() == "10001"
            assert lines[6].strip() == "valid"
            assert lines[7].strip() == "no comments"



    #tests creating a new member profile with the user entering three invalid ID numbers, the only input with specified requirements, and then valid inputs when re-prompted
    #tests for proper file name created and correct file contents
    @mock.patch('builtins.input', side_effect=["Jane Smith", "1", "1111111111", "hkj234k3", "1234", "549837813", "1", "456 Oak Avenue", "1", "Metropolis", "1", "NY", "1", "10001", "1"]) #acts as user input
    def test_invalid_add_new_member_profile(self, mock_input):
        #call function that is being tested
        self.pm.add_new_member_profile()
        #verify the correct member file was created
        self.assertTrue(os.path.exists(self.member_file), f"File {self.member_file} was not created.")
        #verify the contents of the file
        with open(self.member_file, 'r') as f:
            lines = f.readlines()
            assert lines[0].strip() == "Jane Smith"
            assert lines[1].strip() == "549837813"
            assert lines[2].strip() == "456 Oak Avenue"
            assert lines[3].strip() == "Metropolis" 
            assert lines[4].strip() == "NY"
            assert lines[5].strip() == "10001"
            assert lines[6].strip() == "valid"
            assert lines[7].strip() == "no comments"
            


    #tests removing an existing doctor profile
    @mock.patch('builtins.input', side_effect=["435869389", "1", "1"]) #acts as user input
    def test_remove_doctor_profile(self, mock_input):
        #create file first to remove
        with open(self.doctor_file, 'w') as f:
            f.write("Dr. John")

        #make sure file was successfully created
        self.assertTrue(os.path.exists(self.doctor_file))

        #test removing the doctor profile, the file was created during set up
        self.pm.remove_doctor_profile()
        # Verify the file was removed
        self.assertFalse(os.path.exists(self.doctor_file), f"File {self.doctor_file} was not deleted.")



    #test removing an existing member profile
    @mock.patch('builtins.input', side_effect=["549837813", "1", "1"]) #acts as user input
    def test_remove_member_profile(self, mock_input):
        #create file first to remove
        with open(self.member_file, 'w') as f:
            f.write("Jane Doe")

        #make sure file was successfully created
        self.assertTrue(os.path.exists(self.member_file))

        #test removing the member profile that was created during setup()
        self.pm.remove_member_profile()
        #verify the file was removed
        self.assertFalse(os.path.exists(self.member_file), f"File {self.member_file} was not deleted.")




    #tests editing an existing doctor profile
    @mock.patch('builtins.input', side_effect=["435869389", "1", "1", "a", "1", "1", "b", "1", "1", "c", "1", "1", "d", "1", "1", "e", "1"]) #acts as user input
    def test_edit_doctor_profile(self, mock_input):
        #write info into doctor file to then edit
        with open(self.doctor_file, 'w') as file:
            file.write("Dr. John Doe\n")
            file.write("435869389\n")
            file.write("123 Elm Street\n")
            file.write("Springfield\n")
            file.write("IL\n")
            file.write("62704\n")

        #confirm the content of the file after setting it with initial values
        with open(self.doctor_file, 'r') as f:
            lines = f.readlines()
            assert lines[0].strip() == "Dr. John Doe"
            assert lines[1].strip() == "435869389"
            assert lines[2].strip() == "123 Elm Street"
            assert lines[3].strip() == "Springfield"
            assert lines[4].strip() == "IL"
            assert lines[5].strip() == "62704"

        #run doctor profile editing function
        self.pm.edit_doctor_profile()

        #check that the profile has been properly edited with the values passed in as user input with mock
        with open(self.doctor_file, 'r') as f:
            lines = f.readlines()
            assert lines[0].strip() == "a"
            assert lines[1].strip() == "435869389" #ID number should not be changed, it cannot be edited
            assert lines[2].strip() == "b"
            assert lines[3].strip() == "c"
            assert lines[4].strip() == "d"
            assert lines[5].strip() == "e"



    #tests editing an existing member profile
    @mock.patch('builtins.input', side_effect=["549837813", "1", "1", "a", "1", "1", "b", "1", "1", "c", "1", "1", "d", "1", "1", "e", "1", "1", "invalid", "1", "1", "f", "1"]) #acts as user input
    def test_edit_member_profile(self, mock_input):
        #write info into member file to then edit it
        with open(self.member_file, 'w') as file:
            file.write("Jane Smith\n")
            file.write("549837813\n")
            file.write("456 Oak Avenue\n")
            file.write("Metropolis\n")
            file.write("NY\n")
            file.write("10001\n")
            file.write("valid\n")
            file.write("no comments\n")

        #verify the contents of the file before editing
        with open(self.member_file, 'r') as f:
            lines = f.readlines()
            assert lines[0].strip() == "Jane Smith"
            assert lines[1].strip() == "549837813"
            assert lines[2].strip() == "456 Oak Avenue"
            assert lines[3].strip() == "Metropolis" 
            assert lines[4].strip() == "NY"
            assert lines[5].strip() == "10001"
            assert lines[6].strip() == "valid"
            assert lines[7].strip() == "no comments"

        #run member editing function that is being tested
        self.pm.edit_member_profile()
        
        #check that the profile has been properly edited with the values passed in as user input with mock
        with open(self.member_file, 'r') as f:
            lines = f.readlines()
            assert lines[0].strip() == "a"
            assert lines[1].strip() == "549837813" #ID number should not be changed, it cannot be edited
            assert lines[2].strip() == "b"
            assert lines[3].strip() == "c"
            assert lines[4].strip() == "d"
            assert lines[5].strip() == "e"
            assert lines[6].strip() == "invalid"
            assert lines[7].strip() == "f"



    #tests editing the status of an existing member profile
    @mock.patch('builtins.input', side_effect=["549837813", "1", "1", "f", "1"]) #acts as user input
    def test_edit_member_status(self, mock_input):
        #write initial information into the member file
        with open(self.member_file, 'w') as file:
            file.write("Jane Smith\n")
            file.write("549837813\n")
            file.write("456 Oak Avenue\n")
            file.write("Metropolis\n")
            file.write("NY\n")
            file.write("10001\n")
            file.write("valid\n")
            file.write("no comments\n")

        #verify the contents of the file before editing
        with open(self.member_file, 'r') as f:
            lines = f.readlines()
            assert lines[0].strip() == "Jane Smith"
            assert lines[1].strip() == "549837813"
            assert lines[6].strip() == "valid"
            assert lines[7].strip() == "no comments"

        #run the edit_member_status function
        self.pm.edit_member_status()

        #verify the status and comments have been updated
        with open(self.member_file, 'r') as f:
            lines = f.readlines()
            assert lines[6].strip() == "invalid"  #check the updated status
            assert lines[7].strip() == "f"        #check the updated comments




if __name__ == '__main__':
    unittest.main()




    



