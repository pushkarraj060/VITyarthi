ATM System – Feature Overview
# Data Persistence

All account information—Account ID, Name, PIN, and Balance—is stored in an accounts.csv file.
Any updates you make during a session (like deposits, withdrawals, or PIN changes) are immediately saved, so your data is always up to date when you restart the program.

# Main ATM Services

The system provides four essential banking functions:

1. Cash Withdrawal

Verifies available balance

Deducts the withdrawal amount if funds are sufficient

2. Cash Deposit

Accepts a deposit amount

Adds the amount to your current balance

3. Change PIN

Allows you to securely update your 4-digit PIN

4. Account Profile

Displays full account details, including your current balance

# Security & Input Validation

The system includes built-in safety checks:

Account ID + PIN validation is required for sensitive operations like withdrawals or viewing your profile.

Insufficient balance check prevents overdrafts during withdrawals.

Input validation ensures all monetary values are positive and correctly formatted.

# Technologies Used

Programming Language: Python 3.x

Libraries:

csv – for reading/writing account data

sys – for controlled exits

Data Storage: CSV file (simple and lightweight)

# How to Run the Program
1. Setup

The script automatically creates the necessary accounts.csv file with sample data the first time it runs.

Steps:
a. Save the entire code as atm_simulator.py
b. Run it once to generate the CSV file

2. Execution

Open your terminal (or command prompt), navigate to the folder containing the file, and run:

python atm_simulator.py-

3. Sample Login Credentials

Use the following example account to try out the features:
[ACC_ID, NAME, PIN, BALANCE]
[1001, ARYAN, 1204, 10000.00]

# How to Use the Program

1)When the script starts, you’ll see the Main Menu.

2) Choose the service you want using numbers 1–4.

3) Enter your Account ID.

4) For transactions that require identity verification (e.g., withdrawal or viewing account details), enter your PIN.

5) Follow the on-screen instructions to complete your action.
