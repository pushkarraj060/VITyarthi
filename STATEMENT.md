**1. Problem Statement**

This project tackles a simple but important challenge: creating a realistic environment to demonstrate the basics of financial transaction processing, user authentication, and persistent data storage—all within a console application.

In real-life banking systems, every update to an account (like a withdrawal or PIN change) must be saved permanently. This project focuses on how to make those changes stick beyond the current program session, using an accessible and easy-to-understand approach: storing data in a CSV file and managing it with standard Python tools.

**2. Scope and Goals**

The main goal is to build a fully functional, command-line ATM system that reads and writes account information from a CSV file.

In Scope

**Account Lookup:** Find a user’s account using their unique Account ID.

**Authentication:** Check the user’s PIN before allowing sensitive actions.

**Core Transactions:** Support deposits, withdrawals, and PIN changes.

**Balance Validation:** Prevent withdrawals that exceed the available balance.

**File Persistence:** Load data from accounts.csv at startup and save changes back to the file after any successful transaction.

**Input Validation:** Ensure amounts are numbers and PINs follow required format/length.

Out of Scope (Limitations for Now)

**Security Enhancements:** No encryption or hashing for PINs or balances yet.

**Advanced Error Handling:** No support for concurrency issues or detailed logging.

**User Interface:** No GUI or web interface—command line only.

**Account Creation:** The system can only work with accounts already listed in the CSV file.

**3. Design Rationale**
**A. Data Structure Choices**

CSV File (accounts.csv):
Chosen for its simplicity and because it works perfectly with Python’s built-in csv module. It makes persistent storage easy to understand and manage.

List of Dictionaries in Python:
After loading the CSV, each account becomes a dictionary. This makes it very easy to access fields like 'PIN' or 'BALANCE' using meaningful keys.
The list structure also makes account search simple using functions like find_account().

**B. Modularity**

To keep the code clear and easy to modify, the program is broken into dedicated functions:

load_data() – Reads the CSV and deals with errors like missing files.

save_data() – Writes updated account information back to the file.

find_account() – Locates a specific account in the loaded data.

run_atm() – The main program loop that manages menus, user input, and directs actions to the correct transaction functions.

**C. Transaction Logic**

**All transaction actions—depositing, withdrawing, or changing a PIN—follow the same reliable process:**

Read the current value from the CSV data (as a string).

Convert balances to floats when doing math.

Apply the update or calculation.

Convert the balance back to a properly formatted string (two decimal places).

Call save_data() to make the update permanent.
