#test_member_reports.py
#Jordan's Test Cases for Member Reports
#Dependencies: pytest-mock (pip install this), unittest, datetime, io
#To Run Test File: python -m unittest test_member_reports.py
import unittest
from member_reports import member_reports
from unittest.mock import patch, mock_open, MagicMock
from datetime import datetime
import io

#Sample member profile content
member_profile_content = """Rose Martinez
279562441
690 Maple Avenue
Salem
OR
97030
valid
no comments

11-08-2024
11-06-2024
972903252
279562441
654020
55.00
 

11-04-2024 10:21:15
10-30-2024
963800953
279562441
654010
80.00
Routine service completed successfully.

11-21-2024 17:59:20
11-17-2024
565336738
279562441
654013
65.00
Routine service completed successfully.

11-03-2024 11:52:59
10-31-2024
394258256
279562441
654014
90.00
 

11-27-2024 21:38:22
11-22-2024
200188489
279562441
654004
60.00
 

11-08-2024 02:46:23
11-04-2024
892591649
279562441
654006
100.00
 

11-03-2024 21:51:02
10-30-2024
342550297
279562441
654016
50.00
Routine service completed successfully.
"""

class TestMemberReports(unittest.TestCase):
    @patch('builtins.open')
    @patch('os.path.exists')
    def test_generate_member_report(self, mock_exists, mock_open_func):
        #Mock the os.path.exists() method to always return True
        mock_exists.return_value = True

        #Mock the open() function
        m = mock_open(read_data=member_profile_content)
        mock_open_func.side_effect = [m.return_value, m.return_value]

        #Instantiate the member_reports class
        member_reports_instance = member_reports()
        member_reports_instance.get_9_digits = MagicMock(return_value='279562441')
        member_reports_instance.get_menu_choice = MagicMock(return_value=2)
        member_reports_instance.file_exists = MagicMock(return_value='279562441_profile.txt')
        member_reports_instance.print_member_report = MagicMock()

        #Run the generate_member_report method
        with patch('member_reports.datetime') as mock_datetime:
            #Mock datetime to control the current date
            mock_datetime.now.return_value = datetime(2024, 12, 3)
            mock_datetime.strptime.side_effect = lambda *args, **kwargs: datetime.strptime(*args, **kwargs)

            report = member_reports_instance.generate_member_report()

        #Assertions to check if the report contains expected content
        self.assertIn('Weekly Service Report for Rose Martinez', report)
        self.assertIn('Member ID: 279562441', report)
        self.assertIn('Services Received (Last 7 Days):', report)
        self.assertIn('- Service Date: 11-27-2024 21:38:22', report)
        self.assertIn('Provider ID: 200188489', report)
        self.assertIn('Fee: $60.00', report)
        self.assertNotIn('No services received in the last week.', report)

        #Verify that the report file was written with the correct name
        expected_date_str = datetime(2024, 12, 3).strftime("%m_%d_%Y")
        expected_filename = f"279562441_Rose_Martinez_report_{expected_date_str}.txt"
        mock_open_func.assert_any_call(expected_filename, 'w')

        #Verify that print_member_report was called with the correct filename
        member_reports_instance.print_member_report.assert_called_with(expected_filename)

    @patch('builtins.open')
    @patch('os.path.exists')
    def test_generate_member_report_no_services(self, mock_exists, mock_open_func):
        #Mock the os.path.exists() method to always return True
        mock_exists.return_value = True

        #Modify the member_profile_content to have no recent services
        member_profile_no_services = member_profile_content.replace('11-27-2024 21:38:22', '11-20-2024 21:38:22')

        #Mock the open() function
        m = mock_open(read_data=member_profile_no_services)
        mock_open_func.side_effect = [m.return_value, m.return_value]

        #Instantiate the member_reports class
        member_reports_instance = member_reports()
        member_reports_instance.get_9_digits = MagicMock(return_value='279562441')
        member_reports_instance.get_menu_choice = MagicMock(return_value=2)
        member_reports_instance.file_exists = MagicMock(return_value='279562441_profile.txt')
        member_reports_instance.print_member_report = MagicMock()

        #Run the generate_member_report method
        with patch('member_reports.datetime') as mock_datetime:
            #Mock datetime to control the current date
            mock_datetime.now.return_value = datetime(2024, 12, 3)
            mock_datetime.strptime.side_effect = lambda *args, **kwargs: datetime.strptime(*args, **kwargs)

            report = member_reports_instance.generate_member_report()

        #Assertions to check if the report contains expected content
        self.assertIn('Weekly Service Report for Rose Martinez', report)
        self.assertIn('Member ID: 279562441', report)
        self.assertIn('Services Received (Last 7 Days):', report)
        self.assertIn('No services received in the last week.', report)
        self.assertNotIn('- Service Date: 11-27-2024 21:38:22', report)

    @patch('builtins.open')
    @patch('os.path.exists')
    def test_generate_member_report_invalid_member_id(self, mock_exists, mock_open_func):
        #Mock the os.path.exists() method to return False (profile does not exist)
        mock_exists.return_value = False

        #Mock the open() function (it shouldn't be called in this test)
        m = mock_open(read_data='')
        mock_open_func.side_effect = [m.return_value, m.return_value]

        #Instantiate the member_reports class
        member_reports_instance = member_reports()
        member_reports_instance.get_9_digits = MagicMock(return_value='000000000')  #Invalid member ID
        member_reports_instance.get_menu_choice = MagicMock(return_value=2)
        member_reports_instance.file_exists = MagicMock(return_value=None)  #Simulate file not found
        member_reports_instance.print_member_report = MagicMock()

        #Capture the output to verify error message
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            report = member_reports_instance.generate_member_report()
            output = mock_stdout.getvalue()

        #Assertions to check that the report is None and error message is printed
        self.assertIsNone(report)
        self.assertIn('Error: Member ID 000000000 not found.', output)
        #Ensure that print_member_report was not called
        member_reports_instance.print_member_report.assert_not_called()

if __name__ == '__main__':
    unittest.main()
