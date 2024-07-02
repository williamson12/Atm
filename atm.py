import getpass

class ATM:
    def __init__(self, balance=0, pin="0000"):
        self.balance = balance
        self.pin = pin
        self.transaction_history = []

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")
        self.transaction_history.append("Checked balance")

    def deposit_cash(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
            self.transaction_history.append(f"Deposited ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw_cash(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Invalid or insufficient funds for withdrawal.")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully.")
            self.transaction_history.append("Changed PIN")
        else:
            print("Incorrect old PIN.")

    def print_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

def main():
    atm = ATM(balance=1000, pin="1234")
    
    while True:
        print("\nATM Machine")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            atm.check_balance()
        
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            atm.deposit_cash(amount)
        
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw_cash(amount)
        
        elif choice == '4':
            old_pin = getpass.getpass("Enter old PIN: ")
            new_pin = getpass.getpass("Enter new PIN: ")
            atm.change_pin(old_pin, new_pin)
        
        elif choice == '5':
            atm.print_transaction_history()
        
        elif choice == '6':
            print("Exiting... Thank you for using the ATM.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



