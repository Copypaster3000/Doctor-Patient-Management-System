# Doctor Patient Management System

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


## Class Descriptions

### `parent`
- The parent class of the hierarchy.  
- Contains all reusable functions for handling files and any other small functions reused across classes.  

### `provider_reports(parent)`
- Child of `parent`.  
- Handles generating provider-related reports.  
- Responsible for:  
  - Manager Mode:  
    - Generate a doctor's weekly service report  
    - Generate a Provider Summary report for all doctors  
    - Generate a weekly ETF report  

### `member_reports(parent)`
- Child of `parent`.  
- Handles member-related reports.  
- Responsible for:  
  - Manager Mode:  
    - Generate a member's weekly service report  

### `profile_manager(parent)`
- Child of `parent`.  
- Manages adding/removing and editing doctor and member profiles.
- Responsible for:  
  - Manager Mode:  
    - Create a new doctor profile  
    - Create a new member profile  
    - Edit a doctor profile  
    - Edit a member profile  
    - Remove an existing doctor profile  
    - Remove an existing member profile  
    - Change a member's status  

### `services_manager(parent)`
- Child of `parent`.  
- Manages the services directory.  
- Responsible for:  
  - Manager Mode:  
    - Add a service to the services directory  
    - Remove a service from the services directory  
  - Provider Mode:  
    - View services directory  

### `provider_services_logger(parent)`
- Child of `parent`.  
- Handles providers logging a member service.  
- Responsible for:  
  - Provider Mode:  
    - Log a member service  

### `menus_n_modes(parent)`
- Child of `parent`.  
- Manages high-level menu interactions and user choices.  
- Responsible for displaying menus and calling the appropriate functions based on user input.  


## File Structure
The system operates with specific file naming conventions:
- `123456789_doctor_name_profile.txt`: Doctor profile and log of services.
- `123456789_member_name_profile.txt`: Member profile and service history.
- `123456789_doctor_name_provider_service_report_MM_DD_YYYY.txt`: An individual doctor's weekly billing report. List the provider's profile information and list services provided in chronological order of the date the service was provided; at the bottom of the file, a total fee of all services will be provided and the total number of services provided.
- `123456789_member_name_report_MM_DD_YYYY.txt`: An individual member's weekly billing report. (Needs better description)
- `provider_summary_report_MM_DD_YYYY` lists every provider to be paid that week, the number of consultations each provider had, and the fee dues to each provider. At the bottom of the file, the total fee due to all providers and the total number of consultations of all providers will be present.
- `etf_report_MM_DD_YYYY.txt`: Summary of weekly payments due to all doctors.
- `services.txt`: Lists all available services with codes and fees.

