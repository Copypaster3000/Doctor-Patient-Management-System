#test_profile_manager.py
#CS 314
#Doctor Patient Management System
#This file test profile manager class

import os
import pytest
from unittest.mock import patch
from profile_manager import profile_manager


#this test the add new doctor function by simulating user input and verifying the creation
#and contents of the created doctor profile
def test_add_new_doctor_profile():
    #create instance of profile manager
    pm = profile_manager()
    #expected file name
    expected_file_name = "435869389_doctor_Dr._John_Doe_profile.txt"

    #delete profile file to be created if it already exists
    if os.path.exists(expected_file_name): os.remove(expected_file_name)

    #mock user input responses 
    user_inputs = ["Dr. John Doe", "1", "435869389", "1", "123 Elm Street", "1", "Springfield", "1", "IL", "1", "62704", "1"]

    input_iterator = iter(user_inputs)

    #mock the input function to return values from user_input sequentially
    with patch('builtins.input', lambda _: next(input_iterator)):
        #call function to test
        pm.add_new_doctor_profile()


    #verify that the file was created
    assert os.path.exists(expected_file_name), f"File {expected_file_name} was not created."

    #verify the contents of the file
    with open(expected_file_name, 'r') as f:
        lines = f.readlines()
        assert lines[0].strip() == "Dr. John Doe", "Doctor name in file does not match expected value."
        assert lines[1].strip() == "435869389", "Doctor ID in file does not match expected value."
        assert lines[2].strip() == "123 Elm Street", "Street in file does not match expected value."
        assert lines[3].strip() == "Springfield", "City in file does not match expected value."
        assert lines[4].strip() == "IL", "State in file does not match expected value."
        assert lines[5].strip() == "62704", "Zip code in file does not match expected value."

    # Clean up: Remove the created file
    os.remove(expected_file_name)




    



