ATM System – Feature Overview
# Data Persistence

All account information—Account ID, Name, PIN, and Balance—is stored in an accounts.csv file.
Any updates you make during a session (like deposits, withdrawals, or PIN changes) are immediately saved, so your data is always up to date when you restart the program.

# Main ATM Services

The system provides four essential banking functions:

**1. Cash Withdrawal**

Verifies available balance

Deducts the withdrawal amount if funds are sufficient

**2. Cash Deposit**

Accepts a deposit amount

Adds the amount to your current balance

**3. Change PIN**

Allows you to securely update your 4-digit PIN

**4. Account Profile**

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

**Screenshots / Results**

<img width="644" height="267" alt="image" src="https://github.com/user-attachments/assets/fc8a4aef-cad3-4800-9e69-1e10b41bb567" />
<img width="643" height="244" alt="image" src="https://github.com/user-attachments/assets/36b14366-cdb8-41b1-a3a8-cc9749782cfa" />
<img width="675" height="246" alt="image" src="https://github.com/user-attachments/assets/fd4d1fb5-5e2f-42d2-a7eb-2bbd19eff5b8" />
<img width="616" height="248" alt="image" src="https://github.com/user-attachments/assets/377c5b11-acba-4e1e-85f4-c5fb4187dd4f" />

# How to Use the Program

1)When the script starts, you’ll see the Main Menu.

2) Choose the service you want using numbers 1–4.

3) Enter your Account ID.

4) For transactions that require identity verification (e.g., withdrawal or viewing account details), enter your PIN.

5) Follow the on-screen instructions to complete your action.
