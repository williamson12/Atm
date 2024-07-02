# Atm
simple ATM machine simulation in Python that includes the specified functions: account balance inquiry, cash withdrawal, cash deposit, PIN change, and transaction history. 
Explanation:
Class ATM:

__init__: Initializes the ATM with a balance and a PIN.
check_balance: Prints the current balance and logs the transaction.
deposit_cash: Adds the deposit amount to the balance if it's valid and logs the transaction.
withdraw_cash: Deducts the withdrawal amount from the balance if sufficient funds are available and logs the transaction.
change_pin: Changes the PIN if the old PIN is correct and logs the transaction.
print_transaction_history: Prints the transaction history.
Function main:

Creates an instance of ATM with an initial balance of $1000 and a default PIN.
Provides a menu for the user to interact with the ATM.
Handles user input and calls the appropriate methods on the ATM instance.
How to Run:
Save the script to a file, for example, atm_simulation.py.
Run the script:
sh
Copy code
python atm_simulation.py
Usage:
Check Balance: Prints the current account balance.
Deposit Cash: Prompts for an amount to deposit and updates the balance.
Withdraw Cash: Prompts for an amount to withdraw and updates the balance if sufficient funds are available.
Change PIN: Prompts for the old and new PIN, changes the PIN if the old PIN is correct.
Transaction History: Prints the history of all transactions.
Exit: Exits the ATM simulation.
This script provides a simple yet functional ATM simulation.
