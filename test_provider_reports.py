#test_provider_reports.py
#Doctor Patient Management System
#This file contains the unit and integration tests for the provider_reports class.

#run with:
#python -m unittest test_provider_reports.py

#the tests are defined in this file, in the following order:
#def test_count_weekly_consultations(self, doctor_file):
#def test_generate_provider_summary_report(): #high level menu option
#def test_get_name_by_id_num(self, id_number):#returns the name of a doctor based on their id number
#def test_remove_outdated_services(self, file_name):
#def test_generate_provider_service_report(): #high level menu option
#def test_print_report(self, report_file):
#def test_copy_and_rename_file(self, original_file, new_file_name):#copies and re-names a file
#def test_insert_line_in_file(file_path, line_number, new_line):#Inserts a new line at a specific line number in a file without disrupting the rest of the file.

from datetime import date, datetime, timedelta
from io import StringIO
from parent import parent
import shutil
import glob
import sys
import os

import unittest
from unittest.mock import patch, mock_open, MagicMock
from provider_reports import provider_reports

class test_provider_reports(unittest.TestCase):
    def setUp(self):
        #create an instance of Profile_reports for testing
        self.pr = provider_reports()
    
    def test_count_weekly_consultations(self):#counts the number of consultations in the past week
        for file in self.pr.doctor_files:
            if (file[:9] == 120945783):
                assert self.pr.count_weekly_consultations(file) == 3
            if (file[:9] == 123456020):
                assert self.pr.count_weekly_consultations(file) == 2
            if (file[:9] == 342964709):
                assert self.pr.count_weekly_consultations(file) == 3
            if (file[:9] == 345678924):
                assert self.pr.count_weekly_consultations(file) == 2
            if (file[:9] == 666666666):
                assert self.pr.count_weekly_consultations(file) == 1
            if (file[:9] == 375489247):
                assert self.pr.count_weekly_consultations(file) == 2

    def test_generate_provider_summary_report(self):
        # Mock the methods that are called within generate_provider_summary_report
        self.pr.get_9_digits = MagicMock(return_value='345678924')
        self.pr.get_menu_choice = MagicMock(return_value=1)
        
        # assert that the printout has correct contents
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.pr.generate_provider_summary_report()
            self.assertIn('Sum of all weekly fees:', mock_stdout.getvalue())
        
        current_date = datetime.now().strftime("%m_%d_%Y")
        os.remove(f"provider_summary_report_{current_date}.txt")

    def test_get_name_by_id_num(self):#returns the name of a doctor based on their id number
        for file in self.pr.doctor_files:
            if (file[:9] == 120945783):
                assert self.pr.get_name_by_id_num('120945783') == 'Jordan Michael'
            if (file[:9] == 123456020):
                assert self.pr.get_name_by_id_num('123456020') == 'Ruby Perez'
            if (file[:9] == 342964709):
                assert self.pr.get_name_by_id_num('342964709') == 'Erin wheeler'
            if (file[:9] == 345678924):
                assert self.pr.get_name_by_id_num('345678924') == 'John Doe'
            if (file[:9] == 666666666):
                assert self.pr.get_name_by_id_num('666666666') == 'Aubrey Grahm'
            if (file[:9] == 375489247):
                assert self.pr.get_name_by_id_num('375489247') == 'Doctor Drake'
    
    def test_remove_outdated_services(self):
        sys.stdin = MagicMock()
        # Simulate multiple inputs: first the ID, then the menu choice to re-enter the ID
        sys.stdin.readline.side_effect = ['123456020', '1', '1']
        
        # Mock the methods that are called within generate_provider_service_report
        self.pr.get_9_digits = MagicMock(return_value='123456020')
        self.pr.get_menu_choice = MagicMock(return_value=1)
        
        # assert that the printout has correct contents
        provider_report_output = ""
        profile_output = ""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.pr.generate_provider_service_report()
            provider_report_output = mock_stdout.getvalue()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.pr.print_report('123456020_doctor_Ruby_Perez_profile.txt')
            profile_output = mock_stdout.getvalue()
        
        self.assertNotEqual(len(provider_report_output.split('\n')), len(profile_output.split('\n')))

        current_date = datetime.now().strftime("%m_%d_%Y")
        os.remove(f"123456020_Ruby_Perez_provider_service_report_{current_date}.txt")

    def test_generate_provider_service_report(self):
        sys.stdin = MagicMock()
        # Simulate multiple inputs: first the ID, then the menu choice to re-enter the ID
        sys.stdin.readline.side_effect = ['345678924', '1', '1']
        
        # Mock the methods that are called within generate_provider_service_report
        self.pr.get_9_digits = MagicMock(return_value='345678924')
        self.pr.get_menu_choice = MagicMock(return_value=1)
        
        # assert that the file has correct contents
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.pr.generate_provider_service_report()
            self.assertIn('First and last name:', mock_stdout.getvalue())     

        current_date = datetime.now().strftime("%m_%d_%Y")
        os.remove(f"345678924_John_Doe_provider_service_report_{current_date}.txt")

    def test_print_report(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.pr.print_report('654785467_member_Adam_Douglass_profile.txt')
            self.assertIn('Nowhere Street', mock_stdout.getvalue())

    def test_copy_and_rename_file(self):
        # Create a file to copy
        with open('test_file.txt', 'w') as f:
            f.write('test')
        
        # Copy the file
        self.pr.copy_and_rename_file('test_file.txt', 'test_file_copy.txt')
        
        # Check if the file was copied
        self.assertTrue(os.path.exists('test_file_copy.txt'))

        # Remove the copied file
        os.remove('test_file.txt')
        os.remove('test_file_copy.txt')

    def test_insert_line_in_file(self):
        # Create a file to insert a line into
        with open('test_file.txt', 'w') as f:
            f.write('line1\nline3\n')
        
        # Insert a line into the file
        self.pr.insert_line_in_file('test_file.txt', 2, 'line2')
        
        # Check if the line was inserted
        with open('test_file.txt', 'r') as f:
            lines = f.readlines()
            self.assertEqual(lines[1], 'line2\n')

        # Remove the file
        os.remove('test_file.txt')