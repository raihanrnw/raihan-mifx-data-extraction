# 🚀 API Data Extraction Utility - Python Framework - Submission QA Engineer in MIFX

**Name:** Raihan Naiwan
**Target API:** https://reqres.in/api/users?page=2
**Framework:** Python 3 + Requests Library

## Automate Result
Automate Result Video can be found on this link https://drive.google.com/file/d/1OZce6k-AzZOFOKgTWDXTIgz7-7CfyaL1/view?usp=sharing

## Overview
This project is an automated data extraction utility developed for the QA Engineer position at MIFX

The framework is built using Python 3, because this framework is most easy to doing extract api to csv file

## Technology Stack
* **Testing Framework:** Python 3.9+

## Framework Architecture
The project demonstrates the ability to interact with REST API, and export results into a standardized CSV format.

## Execution Guide (Running via Terminal)
1. Clone this repository and navigate to the project root directory.
2. Ensure you have Python installed and create a virtual environment
3.  Install the required dependencies with command "pip install requests"
4. Execute the extraction script with command "python3 fetch_users.py"

## Test Reporting
1. Once the tests complete, the script will output "Convert Done! File csv generated successfully, please check the users.csv on root directory"
2. The generated users.csv file will be located in the root directory

```Directory
fetch_users_convert_csv_MIFX/
├── .venv/                        # Virtual env
├── fetch_users.py                # Main execution script
└── README.md                     # Project documentation

