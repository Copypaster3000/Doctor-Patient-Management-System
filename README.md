# Docotor Patient Management System

## Project Overview
This project is a data management system developed for Chocoholics Anonymous (ChocAn) to streamline member services, billing, and reporting. The software provides two main operational modes, **Manager Mode** and **Provider Mode**, aimed at assisting healthcare providers and managers with tasks like scheduling, logging services, and generating billing reports.

## Purpose and Scope
The ChocAn system is designed to process data to help manage chocolate addiction services for members of Chocoholics Anonymous. The system supports:
- Service scheduling and logging for members.
- Managing doctors and members.
- Generating doctor and member service reports. 
- Managing services provided,

> **Note**: This project focuses solely on building the ChocAn data processing software and does not include server communication, financial processing, or hardware development.

## Features and Functionalities

### 1. Manager Mode
In Manager Mode, the manager can perform key administrative tasks:
- **Generate Billing Reports**:
  - **Doctor Billing Report**: Provides a summary of services a doctor has performed in a billing period, including member details and total fees.
  - **Member Billing Report**: Summarizes services received by a member and calculates total fees owed.
- **Add or Remove Profiles**:
  - **Add New Doctor**: Creates a profile for a doctor with basic contact and identification information.
  - **Add New Member**: Creates a profile for a member, including contact and identification information.
  - **Remove Doctor/Member**: Deletes profiles from the system based on unique identification numbers.
- **Change Member Status**: Updates the status of a member (e.g., to "suspended" for unpaid dues).
- **Service Management**: Adds or removes services that providers can offer.

### 2. Provider Mode
Provider Mode is used by healthcare providers (doctors) to manage services for members:
- **Provider Login**: Authenticates the provider based on their unique ID.
- **Log Member Service**: Logs details of a service provided to a member, updating both the member’s and provider’s profiles.
- **View Services Directory**: Allows providers to view all available services with codes and fees.

### 3. Data Management
The system manages data through a set of organized text files, which store essential information on members, providers, services, and billing reports.
- **Doctor Profile Files**: Stores a doctor’s details and logs of services provided.
- **Member Profile Files**: Tracks each member’s details and logs services received.
- **Billing Report Files**: Generates weekly billing summaries for both doctors and members.
- **Services File**: Maintains a list of available services, editable by the manager.

## File Structure
The system operates with specific file naming conventions:
- `12345_name_doctor_profile.txt`: Doctor profile and log of services.
- `12345_name_member_profile.txt`: Member profile and service history.
- `12345_name_doctor_report.txt`: Doctor's weekly billing report.
- `12345_name_member_report.txt`: Member's weekly billing report.
- `services.txt`: Lists all available services with codes and fees.

