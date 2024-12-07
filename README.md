# Doctor Patient Management System

## Overview
The Doctor Patient Management System is a Python-based program designed to manage profiles, log services, and generate reports for healthcare providers and their patients. It provides functionality for both **Manager Mode** and **Provider Mode**, allowing streamlined operations for managing services, profiles, and billing reports.

---

## Features

### Main Menu
1. **Manager Mode**: Access functions for managing profiles, services, and generating reports.  
2. **Provider Mode**: Log services provided to members and view available services.  
3. **Exit Program**: Exit the system.

---

## Prerequisites

1. **Python 3.8+**: Ensure you have Python installed. [Download Python](https://www.python.org/downloads/)
2. **Dependencies**: No additional libraries are required as it uses core Python modules.

---

## How to Download and Run

### **Step 1: Download the Project**
Clone the repository or download the ZIP file:
```bash
git clone https://github.com/Copypaster3000/Doctor-Patient-Management-System.git
cd Doctor-Patient-Management-System
```

### **Step 2: Set Up the Virtual Environment**
Create and activate a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### **Step 3: Run the Program**
Run the main script:
```bash
python main.py
```

---

## Testing Files
The project includes testing files to verify the functionality of various components. Each testing file name starts with 'test' and contains instructions in its comments at the beginning of the file, specifying the command to run it.

---

## Class Overview

### **Parent Class**
- `parent`: Contains reusable utility functions for file management, input validation, and formatting.

### **Child Classes**
1. **`menus_n_modes`**: Manages menu displays and user interactions.  
2. **`profile_manager`**: Handles creating, deleting, and editing doctor and member profiles.  
3. **`member_reports`**: Generates weekly service reports for members.  
4. **`provider_reports`**: Generates reports for providers, including weekly summaries and payment reports.  
5. **`provider_services_logger`**: Allows providers to log services for members.  
6. **`services_manager`**: Manages the services directory.

---

## High-Level Menu Options

### Main Menu
1) Manager Mode  
2) Provider Mode  
3) Exit Program  

### Manager Mode
1) Generate a doctor's weekly service report  
2) Generate a member's weekly service report  
3) Generate a Provider Summary report for all doctors  
4) Generate a weekly ETF report  
5) Create a new doctor profile  
6) Create a new member profile  
7) Edit a doctor profile  
8) Edit a member profile  
9) Remove an existing doctor profile  
10) Remove an existing member profile  
11) Change a member's status  
12) Add a service to the services directory  
13) Remove a service from the services directory  
14) Exit manager mode  

### Provider Mode
1) Log a member service  
2) View services directory  
3) Exit provider mode  

---

## File Structure
The system operates with specific file naming conventions:
- `123456789_doctor_name_profile.txt`: Contains the doctor's contact information and a log of services provided.
- `123456789_member_name_profile.txt`: Contains the member's contact information and log of services received.
- `123456789_doctor_name_provider_service_report_MM_DD_YYYY.txt`: An individual doctor's weekly billing report. List the provider's profile information and list services provided in chronological order of the date the service was provided; at the bottom of the file, a total fee of all services will be provided and the total number of services provided.
- `123456789_member_name_report_MM_DD_YYYY.txt`: A report of an individual member's services received and fees accrued in the last week.
- `provider_summary_report_MM_DD_YYYY` lists every provider to be paid that week, the number of consultations each provider had, and the fee dues to each provider. At the bottom of the file, the total fee due to all providers and the total number of consultations of all providers will be present.
- `etf_report_MM_DD_YYYY.txt`: Summary of weekly payments due to all doctors.
- `services.txt`: Lists all available services with codes and fees.

---

## Contributors

- **Drake Wheeler**: High-level menus and profile management.  
- **Jordan Oliver**: Member reporting functionality.  
- **Natalya Langford**: Service directory management.  
- **Nikki Rudnick**: Provider reporting features.  
- **Catherine Nemec**: Service logging for providers. 
